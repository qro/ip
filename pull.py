import os, subprocess, json

class IP():
    def __init__(self):
        self.client = client

    def valid(self): 
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
        option = (input('\n [?] Option: '))
        if option == '1':
            IP().ping()
        elif option == '2':
            IP().lookup()
        elif option == '3':
            IP().portscan()

    def ping(self):
        print('test')
        while True:
            try:
                subprocess.check_call(f"PING {self.client} -n 1 | FIND \"TTL=\" > NUL",shell=True)
                print(f' [>] {self.client} is online!')
            except subprocess.CalledProcessError:
                print(f' [>] {self.client} is offline!')
            except KeyboardInterrupt:
                IP().main()

if __name__ == '__main__':
    client = input('\n [?] Enter an IP address: ')
    while not IP().valid():
        exit()
    else:
        IP().main()