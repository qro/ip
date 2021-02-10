import json, os
import time
import ctypes
from colorama import Fore
from urllib.request import urlopen

def main():
    ctypes.windll.kernel32.SetConsoleTitleW('github.com/lxws')
    client = 1

    while True:
        try:
            print('')
            client = input(f" [{Fore.RED}?{Fore.RESET}] Enter IP Address: ")
            url = "http://ip-api.com/json/"
            trackedip = urlopen(url + client)
            data = trackedip.read() 
            values = json.loads(data)
            
            print('')
            print(f" [{Fore.RED}>{Fore.RESET}] {Fore.GREEN}City: " + values[f'city'])
            print(f" {Fore.RESET}[{Fore.RED}>{Fore.RESET}] {Fore.GREEN}Country: " + values['country'])
            print(f" {Fore.RESET}[{Fore.RED}>{Fore.RESET}] {Fore.GREEN}Name of the region: " + values['regionName'])
            print(f" {Fore.RESET}[{Fore.RED}>{Fore.RESET}] {Fore.GREEN}Region: " + values['region'])
            print(f" {Fore.RESET}[{Fore.RED}>{Fore.RESET}] {Fore.GREEN}ISP: " + values['isp'])
            print(f" {Fore.RESET}[{Fore.RED}>{Fore.RESET}] {Fore.GREEN}ZIP Code: " + values['zip'])
            print('')
            print(f' {Fore.RESET}[{Fore.RED}!{Fore.RESET}] Check "https://check-host.net/ip-info?host=' + client + '" for more info')
            
        except:
            print(f" [{Fore.RED}!{Fore.RESET}] {Fore.RED}Make sure you entered a correct IP Address...{Fore.RESET}")
            break
        main()

if __name__ == "__main__":
   main()

main() 