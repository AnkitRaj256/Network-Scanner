# 🔍 LAN Network Scanner

A lightweight Python-based LAN network scanner that identifies **live hosts**, their **open ports**, and **operating systems** on a local subnet using powerful tools like **Nmap** and **Netdiscover**.

---

## 📌 Project Summary

**Use Case:**  
An IT or cybersecurity team wants to monitor their local network to detect unauthorized (rogue) devices and gain visibility into connected systems. This tool provides fast or detailed scans based on user choice.

**Features:**
- Detect live hosts on a subnet
- Identify open TCP ports
- Guess remote OS and device types
- Export results in JSON format
- Easy CLI interface

---

## ⚙️ Tools Used

| Tool           | Purpose                           |
|----------------|---------------------------------|
| **Python 3**   | Core scripting language          |
| **Nmap**       | Detailed scanning (ports, OS)   |
| **Netdiscover**| Quick live host discovery (ARP) |
| **json**       | Exporting results programmatically |

---

## 🖥️ Environment Setup

- **OS:** Windows 11
- **Python:** 3.10+
- **Network Mode:** Host LAN or bridged (to scan real subnet)
- **Privileges:**  
  - `Netdiscover` requires **administrator/sudo** privileges  
  - `Nmap` works without root for basic scans, but some features need it

### ✅ Requirements
Install dependencies:
```bash
pip install python-nmap tabulate
```

Ensure `nmap` and `netdiscover` are installed and added to your system PATH:
```bash
# Example (Linux/WSL)
sudo apt install nmap netdiscover
```

---

## 🚀 How to Use

Run the script:

```bash
python main.py
```

### User Options:

1. **Netdiscover (Fast Scan)**  
   - Lists live hosts in your subnet using ARP.
   - Requires elevated permissions (sudo).

2. **Nmap (Detailed Scan)**  
   - Scans IP range for live hosts.
   - Detects open ports and tries OS detection.

---

## 📄 Example Output

### Netdiscover (Fast)

```bash
[*] Live Hosts Found:
- 192.168.1.1
- 192.168.1.5
```

### Nmap (Detailed)

```plaintext
╒════════════╤══════════════╤════════════════════════════════╤════════════════════╕
│ IP         │ Hostname     │ OS                             │ Open Ports         │
╞════════════╪══════════════╪════════════════════════════════╪════════════════════╡
│ 192.168.1.5│              │ Microsoft Windows 10 - 11      │ 80/tcp, 135/tcp    │
│ 192.168.1.10│             │ Linux 2.6.18                   │ 22/tcp, 3306/tcp   │
╘════════════╧══════════════╧════════════════════════════════╧════════════════════╛
```

---

## 📂 Output Files

All scan results are saved in the `results/` directory as timestamped JSON files:
```
results/
├── scan_20250413_105426.json
```

---

## 📈 Project Objectives

- ✅ Identify live hosts on a LAN
- ✅ Perform fast scans using ARP (Netdiscover)
- ✅ Perform detailed scans using Nmap (ports + OS)
- ✅ Export and log results in readable format

---

## ⚠️ Limitations & Notes

- `Netdiscover` needs elevated privileges to send ARP requests.
- OS detection in Nmap may not always be accurate, especially for firewalled devices.
- The scanner only works on **private LANs** or **internal test networks**.

---

## 🔐 Security Relevance

This tool simulates basic **network reconnaissance**, a phase used by both security professionals and attackers. It is useful for:

- Ethical hacking / Red teaming
- Network audits
- Penetration testing labs

---


## 📜 License

This project is open-source and available under the MIT License.
