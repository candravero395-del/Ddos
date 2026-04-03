DDOS-AKINCI (HTTP Stress Tool)
​A high-performance, multi-threaded HTTP request tool designed for web server stress testing and network security auditing on Linux environments. This tool allows users to evaluate the resilience of a web infrastructure by simulating high-traffic scenarios.
​🚀 Key Features
​Multi-Threaded Engine: Execute hundreds of concurrent requests for maximum stress testing.
​Smart Proxy Scraper: Integrated automatic HTTP proxy retrieval via API for anonymity.
​Custom HTTP Methods: Support for GET, POST, HEAD, PUT, DELETE, and randomized modes.
​Real-time Analytics: Monitor success/failure rates and response times live.
​User-Agent Spoofing: Randomized headers to simulate real browser traffic.
​🛠️ Linux Installation (From Scratch)
​To set up the environment and run the tool on any Linux distribution, follow these steps:

# 1. Update system packages
sudo apt update && sudo apt upgrade -y

# 2. Install Python and Git
sudo apt install python3 python3-pip git -y

# 3. Clone this repository
git clone https://github.com/candravero395-del/Ddos

# 4. Enter the directory
cd Ddos

# 5. Install required Python libraries
pip3 install requests

# 6. Run the tool
python3 DdosAkıncı-AIC.py

💻 How to Use
​Once the tool is launched:
​Target URL: Enter the full address (e.g., http://example.com).
​Mode: Select 1 for Direct (High Speed) or 2 for Proxy (Stealth).
​Method: Type GET, POST, or ALL.
​Threads: Set the number of concurrent workers (e.g., 100).
​Delay: Set to 0 for maximum intensity.
​📝 About the Tool
​This script is a specialized network security component. It functions by flooding a target server with HTTP requests to identify its "Breaking Point." By utilizing an automated proxy scraper, it distributes the origin of the traffic, making it a valuable tool for testing firewall configurations, load balancers, and DDoS mitigation strategies.
​⚠️ Legal Disclaimer
​This tool is for educational purposes and authorized security testing only. Using this tool against targets without prior written consent is illegal. The developer assumes no liability for any misuse or damage caused by this software.
