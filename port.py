import socket
import ctypes
from concurrent import futures
from colorama import Fore
from time import sleep

def check_port(client, port, timeout):
   TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
   TCPsock.settimeout(timeout)
   try:
       TCPsock.connect((client, port))
       return(port)
   except:
       return

def port_scanner(client, timeout):
   threadPoolSize = 500
   portsToCheck = 10000

   executor = futures.ThreadPoolExecutor(max_workers=threadPoolSize)
   checks = [
       executor.submit(check_port, client, port, timeout)
       for port in range(0, portsToCheck, 1)
   ]

   for response in futures.as_completed(checks):
       if (response.result()):
           print(' [>] Listening on port: {}'.format(response.result())) # can't use colorama module because it messes up the braces for the port

def main():
   ctypes.windll.kernel32.SetConsoleTitleW('github.com/lxws')
   print('')
   client = input(f" [{Fore.RED}?{Fore.RESET}] Enter IP Address: ")
   timeout = int(input(f" [{Fore.RED}?{Fore.RESET}] Time out: "))
   print('')
   port_scanner(client, timeout)

if __name__ == "__main__":
   main()

main()