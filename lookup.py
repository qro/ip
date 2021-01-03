import json, os
import time
import ctypes
from colorama import Fore
from urllib.request import urlopen

def main():
    client = 1

    while True:
        ctypes.windll.kernel32.SetConsoleTitleW("github.com/purelxw")
        try:
            print('')
            client = input(f"{Fore.LIGHTBLACK_EX} [{Fore.RED}?{Fore.LIGHTBLACK_EX}] Enter IP Address: {Fore.LIGHTWHITE_EX}")
            url = "http://ip-api.com/json/"
            trackedip = urlopen(url + client)
            data = trackedip.read() 
            values = json.loads(data)
            
            print('')
            print(f"{Fore.LIGHTBLACK_EX} [{Fore.RED}>{Fore.LIGHTBLACK_EX}] {Fore.GREEN}City: " + values['city'])
            print(f"{Fore.LIGHTBLACK_EX} [{Fore.RED}>{Fore.LIGHTBLACK_EX}] {Fore.GREEN}Country: " + values['country'])
            print(f"{Fore.LIGHTBLACK_EX} [{Fore.RED}>{Fore.LIGHTBLACK_EX}] {Fore.GREEN}Name of the region: " + values['regionName'])
            print(f"{Fore.LIGHTBLACK_EX} [{Fore.RED}>{Fore.LIGHTBLACK_EX}] {Fore.GREEN}Region: " + values['region'])
            print(f"{Fore.LIGHTBLACK_EX} [{Fore.RED}>{Fore.LIGHTBLACK_EX}] {Fore.GREEN}ISP: " + values['isp'])
            print(f"{Fore.LIGHTBLACK_EX} [{Fore.RED}>{Fore.LIGHTBLACK_EX}] {Fore.GREEN}ZIP Code: " + values['zip'])
            print('')
            print(f'{Fore.LIGHTBLACK_EX} [{Fore.RED}!{Fore.LIGHTBLACK_EX}] Check "https://check-host.net/ip-info?host=' + client + '" for more info')
            
        except:
            print(f"{Fore.LIGHTBLACK_EX} [{Fore.RED}!{Fore.LIGHTBLACK_EX}] {Fore.RED}Make sure you entered a correct IP Address...{Fore.RESET}")
            break
        main()

if __name__ == "__main__":
   main()

main() 