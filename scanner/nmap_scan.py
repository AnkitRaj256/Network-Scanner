import nmap
from tabulate import tabulate
import socket

def get_hostname(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except socket.herror:
        return "N/A"

def scan_network(ip_range='192.168.1.0/24'):
    print(f"[*] Scanning {ip_range} with Nmap...")
    
    nm = nmap.PortScanner()
    nm.scan(hosts=ip_range, arguments='-T4 -F -O -R')

    devices = []

    for host in nm.all_hosts():
        os_info = nm[host]['osmatch'][0]['name'] if 'osmatch' in nm[host] and nm[host]['osmatch'] else "Unknown"
        
        ports = []
        for proto in nm[host].all_protocols():
            lport = nm[host][proto].keys()
            for port in lport:
                ports.append(f"{port}/{proto}")
        
        hostname = nm[host].hostname() if nm[host].hostname() else get_hostname(host)
        
        devices.append([
            host,
            hostname,
            os_info,
            ', '.join(ports)
        ])

    print("\nScan Results:\n")
    print(tabulate(devices, headers=["IP", "Hostname", "OS", "Open Ports"], tablefmt="fancy_grid"))

    return devices

if __name__ == "__main__":
    ip_range = input("Enter IP range (default: 192.168.1.0/24): ") or "192.168.1.0/24"
    scan_network(ip_range)
