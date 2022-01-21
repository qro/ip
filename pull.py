import os, sys, time, subprocess, json
from urllib.request import urlopen
from concurrent import features

class IP():
    def __init__(self):
        self.client = client

    def valid(self): # stack
        i = 0
        valid = True
        for element in self.client:
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

    def main(self):
        print('\n [1] ICMP Ping, [2] IP lookup, [3] Local IP\n')
        option = int(input('\n [?] Option: '))
        if option == '1':
            ping(self.client)
        elif option == '2':
            IP().lookup()
        elif option == '3':
            IP().portscan()

    def ping(self):

if __name__ == '__main__':
    client = input('\n [?] Enter an IP address: ')
    IP().valid()
    while not IP().valid():
        input(client)
    else:
        IP().main()