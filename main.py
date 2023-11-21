import os, subprocess, json, datetime, socket
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
        os.system('cls & mode 70, 12')
        option = input('\n [1] ICMP Ping, [2] IP lookup, [3] Local IP\n\n [?] Option: ')
        if option == '1':
            IP().ping()
        elif option == '2':
            IP().lookup()
        elif option == '3':
            IP().localip()
        else: 
            IP().main()

    def ping(self):
        os.system('cls & mode 70, 40')
        while True:
            try:
                subprocess.check_call(f"PING {self.client} -n 1 | FIND \"TTL=\" > NUL",shell=True)
                print(f' [>] {self.client} is online!')
            except subprocess.CalledProcessError:
                print(f' [>] {self.client} is offline!')
            except KeyboardInterrupt: # ctrl + c 
                IP().main()

    def lookup(self):
        os.system('cls & mode 70, 20')
        url = 'http://ip-api.com/json/'
        ip = urlopen(url + (self.client))
        data = ip.read()
        values = json.loads(data)
        input(f'\n [>] IP: ', values['query'], '\n [>] City: ', values['city'], '\n [>] Country: ', values['country'], '\n [>] Name of the region: ', values['regionName'], '\n [>] Region: ', values['region'], '\n [>] ISP: ', values['isp'], '\n [>] ZIP Code: ', values['zip'], '\n [>] Organisation: ', values['org'], '\n')
        IP().main()

    def localip(self):
        os.system('cls & mode 70, 12')
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        input(f'\n [>] Hostname: {hostname}\n [>] Local IP: {ip_address}\n')
        IP().main()

if __name__ == '__main__':
    os.system('cls & mode 70, 12')
    client = input(f'\n [?] Enter an IP address: ')
    while not IP().valid():
        exit()
    else:
        f = open("ip.txt", "a")
        f.write(t.strftime("%H:%M:%S %d/%m/%Y : ") + '"' + client + '"' + '\n')
        f.close()
        IP().main()