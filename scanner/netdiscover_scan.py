import os

def run_netdiscover(interface='eth0'):
    print("[*] Running Netdiscover (requires sudo)...")
    os.system(f"sudo netdiscover -i {interface} -r 192.168.1.0/24 -P")
