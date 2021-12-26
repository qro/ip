import os, sys, time, subprocess, json, socket
from urllib.request import urlopen
from concurrent import futures

def icmp():
    os.system('cls & mode 70, 40')
    client = input('\n [?] Enter IP address: ')
    ping(client)

def lookup():
    os.system('cls & mode 70, 40')
    client = 1
    client = input(f'\n [?] Enter IP Address: ')
    url1 = "http://ip-api.com/json/"
    url2 = "http://extreme-ip-lookup.com/json/"
    trackedip1 = urlopen(url1 + client)
    trackedip2 = urlopen(url2 + client)
    data1 = trackedip1.read() 
    data2 = trackedip2.read()
    values1 = json.loads(data1)
    values2 = json.loads(data2)
    
    print(f'\n [>] IP: ' + values1['query'])
    print(f' [>] City: ' + values1['city'])
    print(f' [>] Country: ' + values1['country'])
    print(f' [>] Name of the region: ' + values1['regionName'])
    print(f' [>] Region: ' + values1['region'])
    print(f' [>] ISP: ' + values1['isp'])
    print(f' [>] ZIP Code: ' + values1['zip'])
    print(f' [>] IP Type: ' + values2['ipType'])
    print(f' [>] Organisation: ' + values2['org'])
    print(f' [>] City: ' + values2['city'])
    print(f' [>] Latitude: ' + values2['lat'])
    print(f' [>] Longitude: ' + values2['lon'])

    x = input('\n [?] x to go to menu: ')
    if x == 'x':
        main()
    else:
        print('\n [!] Invalid option')
        time.sleep(0.5)
        lookup()

def localip():
    os.system('cls & mode 70, 12')
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    
    print(f'\n [>] Hostname: {hostname}')
    print(f' [>] IP Address: {ip_address}')
    
    x = input('\n [?] x to go to menu: ')
    if x == 'x':
        main()
    else:
        print('\n [!] Invalid option')
        time.sleep(0.5)
        localip()

def portscan():
    os.system('cls & mode 70, 30')
    client = input('\n [?] Enter IP Address: ')
    timeout = int(input(" [?] Timeout: "))
    print("")
    scan(client, timeout)

def validip(client): # stack
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
    while not validip(client):
        client = input(" [!] Invalid, please try again: ")
    else:
        print('\n [!] Press ctrl + c to stop')
        time.sleep(1)
        while True:
            try:
                subprocess.check_call(f"PING {client} -n 1 | FIND \"TTL=\" > NUL",shell=True)
                print(f' [>] {client} is online!')
            except subprocess.CalledProcessError:
                print(f' [>] {client} is offline!')
            except KeyboardInterrupt:
                icmp()

def check_port(client, port, timeout):
   TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
   TCPsock.settimeout(timeout)
   try:
       TCPsock.connect((client, port))
       return(port)
   except:
       return

def scan(client, timeout):
   threadPoolSize = 500
   portsToCheck = 10000

   executor = futures.ThreadPoolExecutor(max_workers=threadPoolSize)
   checks = [
       executor.submit(check_port, client, port, timeout)
       for port in range(0, portsToCheck, 1)
   ]

   for response in futures.as_completed(checks):
       if (response.result()):
           print(" [>] Listening on port: {} ".format(response.result()))


def main():
    if len(sys.argv) < 2:
        os.system('cls & mode 70, 12 & title ip multi tool │ by lozza (github.com/qro)')
        sys.stdout.write('''
        
    [1] ICMP Ping
    [2] IP lookup
    [3] What is my local ip?
    [4] Portscan
        
    ''')
    
    choice = input("[?] Option: ")
    if choice == '1':
        icmp()
    elif choice == '2':
        lookup()
    elif choice == '3':
        localip()
    elif choice == '4':
        portscan()
    else:
        print('\n[!] Invalid option')
        time.sleep(0.5)
        main()

main(