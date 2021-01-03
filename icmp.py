# client is the ip that is needed to be entered.
# noted...

import subprocess
import os
from os import system, name 
import ctypes
import sys
from colorama import Fore
import time
from time import sleep

def main():
    ctypes.windll.kernel32.SetConsoleTitleW("github.com/purelxw")
    print('')
    client = input(f"{Fore.LIGHTBLACK_EX} [{Fore.RED}?{Fore.LIGHTBLACK_EX}] Enter IP Address: {Fore.LIGHTWHITE_EX}")
    print('')
    ping(client)

def validation(client): # i love you soverflow
    i = 0
    valid = True
    for element in client:
        if element == '.':
            i += 1
        else:
            try:
                int(element)
            except:
                valid = False
                pass
    if not i == 3:
        valid = False
    return valid 

def ping(client):
    while not validation(client):
        client = input(f"{Fore.LIGHTBLACK_EX} [{Fore.RED}!{Fore.LIGHTBLACK_EX}] {Fore.RED}Make sure you entered a correct IP Address...{Fore.RESET}")
    else:
        while True:
            try:
                subprocess.check_call(f"PING {client} -n 1 | FIND \"TTL=\" > NUL",shell=True)
                print(f"{Fore.LIGHTBLACK_EX} [{Fore.RED}>{Fore.LIGHTBLACK_EX}] {Fore.GREEN}{client} is online!")
            except subprocess.CalledProcessError:
                print(f"{Fore.LIGHTBLACK_EX} [{Fore.RED}>{Fore.LIGHTBLACK_EX}] {Fore.RED}{client} is offline!")
            except KeyboardInterrupt:
                main()

main()
