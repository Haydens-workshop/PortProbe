import sys
import socket
from datetime import datetime

def scan_ports(host, ports):
    try:
        ip = socket.gethostbyname(host)
    except socket.gaierror:
        print("Hostname could not be resolved.")
        sys.exit()

    print("Scanning host", ip)

    start_time = datetime.now()
    for port in range(ports[0], ports[1] + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port}: Open")
        sock.close()

    end_time = datetime.now()
    total_time = end_time - start_time
    print("Scanning completed in", total_time)

def main():
    if len(sys.argv) < 4:
        print("Usage: python port_scanner.py <host> --ports <start>-<end>")
        sys.exit()

    host = sys.argv[1]
    port_range = sys.argv[3].split('-')
    start_port = int(port_range[0])
    end_port = int(port_range[1])

    scan_ports(host, (start_port, end_port))

if __name__ == "__main__":
    main()
