import os, subprocess, json, datetime
from urllib.request import urlopen
t = datetime.datetime.now()

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
        os.system('cls & mode 70, 12 & title ip │ by lozza (github.com/qro)')
        print('\n [1] ICMP Ping, [2] IP lookup, [3] Local IP\n')
        option = (input('\n [?] Option: '))
        if option == '1':
            IP().ping()
        elif option == '2':
            IP().lookup()
        elif option == '3':
            IP().localip()
        else: 
            IP().main()


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

    def lookup(self):
        os.system('cls & mode 70, 40')
        url = 'http://ipwhois.app/json/'
        ip = urlopen(url + self.client)
        data = ip.read()
        values = json.load(data)
        print(f'''

        ''')


if __name__ == '__main__':
    client = input('\n [?] Enter an IP address: ')
    while not IP().valid():
        exit()
    else:
        f = open("ip.txt", "a")
        f.write(client + '\n')
        f.close()
        IP().main()