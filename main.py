from scanner import nmap_scan, netdiscover_scan
from scanner.utils import save_results

def main():
    print("====== LAN Network Scanner ======")
    choice = input("Choose Scan Type:\n1. Netdiscover (fast)\n2. Nmap (detailed)\n> ")

    if choice == '1':
        interface = input("Enter network interface (default: eth0): ") or "eth0"
        netdiscover_scan.run_netdiscover(interface)
    elif choice == '2':
        ip_range = input("Enter IP range (default: 192.168.1.0/24): ") or "192.168.1.0/24"
        results = nmap_scan.scan_network(ip_range)
        save_results(results)
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
