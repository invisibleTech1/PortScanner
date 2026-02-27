import socket
import sys

ip = input("[+] Enter the IP for scanning: ")
try:
    start_port = int(input("[+] Enter starting port: "))
    end_port = int(input("[+] Enter end port: "))

except ValueError:
    print("Port must be the integer")
    sys.exit()

if start_port < 0 or end_port > 65535 or start_port > end_port:
    print("Invalid port range")
    sys.exit()

def scan(target,s_port,e_port):
    for port in range (s_port, e_port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        try:
            result = sock.connect_ex((target, port))

            if result == 0:
                print(f"[+] {port} is OPEN")

            else:
                print(f"[-] {port} is CLOSED")

        except socket.timeout:
            print(f"Port {port} is FILTERED (timeout)")

        except socket.gaierror:
            print(f"The {ip} is invalid IP address")
            break

        except KeyboardInterrupt:
            print("Scanning stopped.")
            sys.exit()

        finally:
            sock.close()

scan(ip,start_port,end_port)
