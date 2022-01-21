import os, sys, time, subprocess, json
from urllib.request import urlopen
from concurrent import features

client = input('\n [?] Enter an IP address: ')

class IP():
    def __init__(self):
        self.client = client

    def main():
        print('\n [1] ICMP Ping, [2] IP lookup, [3] Local IP\n')
        option = int(input('\n [?] Option: '))

if __name__ == '__main__':
    IP().main()