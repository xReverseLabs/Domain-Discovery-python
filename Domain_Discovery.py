# where is your shame, if you recode this, and don't include my credit

import requests
import time
from fake_useragent import UserAgent
from colorama import init, Fore, Style

init(autoreset=True)

API_URL = "https://api.xreverselabs.org/api/discover_domain?apiKey=FREE-TRIAL"

user_agent = UserAgent()

banner = """
______ _                              ______                      _       
|  _  (_)                             |  _  \                    (_)      
| | | |_ ___  ___ _____   _____ _ __  | | | |___  _ __ ___   __ _ _ _ __  
| | | | / __|/ __/ _ \ \ / / _ \ '__| | | | / _ \| '_ ` _ \ / _` | | '_ \ 
| |/ /| \__ \ (_| (_) \ V /  __/ |    | |/ / (_) | | | | | | (_| | | | | |
|___/ |_|___/\___\___/ \_/ \___|_|    |___/ \___/|_| |_| |_|\__,_|_|_| |_|

Domain Discovery Engine - Real Time Update                                                
Owner : https://t.me/xxyz4
API : https://api.xreverselabs.org
"""

unique_domains = set()

def scrape_domains():
    headers = {
    }

    try:
        response = requests.get(API_URL, headers=headers, timeout=10)

        if response.status_code == 200:
            data = response.json()
            domains = data.get('domains', [])

            if domains:
                new_domains = [domain for domain in domains if domain not in unique_domains]

                unique_domains.update(new_domains)

                if new_domains:
                    print(Fore.LIGHTGREEN_EX + f"{len(new_domains)} new domains found.")

                    with open('result_discover.txt', 'a') as f:
                        for domain in new_domains:
                            f.write(domain + '\n')

                    print(Fore.LIGHTCYAN_EX + "New results saved to result_discover.txt")
                else:
                    print(Fore.LIGHTYELLOW_EX + "No new domains found in this request.")
            else:
                print(Fore.LIGHTYELLOW_EX + "No domains found in this request.")
        else:
            print(Fore.LIGHTRED_EX + f"Failed to fetch data: Status Code {response.status_code}")

    except Exception as e:
        print(Fore.LIGHTRED_EX + "An error occurred while connecting to the API!", e)

def main():
    print(f"{Fore.LIGHTCYAN_EX}{banner}")

    repeats = int(input(Fore.YELLOW + "Enter how many times to scrape: "))

    delay = int(input(Fore.YELLOW + "Enter delay between requests (in seconds): "))

    for i in range(repeats):
        print(Style.BRIGHT + Fore.LIGHTCYAN_EX + f"\n[Scraping Attempt {i+1}]")
        scrape_domains()
        
        time.sleep(delay)

if __name__ == "__main__":
    main()
