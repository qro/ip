import os
from os import system, name
import sys
import time
import colorama
import ctypes
from colorama import Fore

if os.name == "nt":
    OS = "WINDOWS"

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def main():
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW('ip multi tool by lozza')
    if len(sys.argv) < 2:
        os.system("clear || cls")
        sys.stdout.write(f'''{Fore.RESET}

    Author: lozza
    '''+Fore.RESET)

    print('')
    choice = input(f" [{Fore.RED}?{Fore.RESET}] Option: {Fore.LIGHTWHITE_EX}")

    if choice == "1":
        print(f" [{Fore.RED}!{Fore.RESET}] {Fore.GREEN}Forwarding...{Fore.RESET}")
        time.sleep(0.3)
        import icmp
    elif choice == "2":
        print(f" [{Fore.RED}!{Fore.RESET}] {Fore.GREEN}Forwarding...{Fore.RESET}")
        time.sleep(0.3)
        import lookup
    elif choice == "3":
        print(f" [{Fore.RED}!{Fore.RESET}] {Fore.GREEN}Forwarding...{Fore.RESET}")
        time.sleep(0.3)
        import port
    else:
        print(f" [{Fore.RED}!{Fore.RESET}] {Fore.RED}Invalid option, please try again...{Fore.RESET}")
        time.sleep(1)
        main()

main()