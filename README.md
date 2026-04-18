# Network Guardian: Asset Discovery & Security Auditing 🇨🇭

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Security Framework](https://img.shields.io/badge/Framework-NIST%20CSF-red)](https://www.nist.gov/cyberframework)

## 📌 Project Overview
Network Guardian is a professional-grade network security tool developed to identify and catalog assets within a Local Area Network (LAN). Using advanced packet manipulation, it provides visibility into the network's physical layer, helping security teams identify **Shadow IT** and unauthorized devices.

This project is part of a career roadmap focused on the Swiss Cybersecurity market, emphasizing technical depth, documentation, and compliance with international security standards.

## 🛡️ Problem Statement & Mitigation
In modern corporate environments (especially in highly regulated sectors like Swiss Banking and Fintech), you cannot protect what you cannot see. 

* **Problem:** Traditional ICMP (Ping) scans are often blocked by local firewalls (Windows Defender, iptables), leading to incomplete asset inventories.
* **Solution:** Network Guardian utilizes **ARP (Address Resolution Protocol)** requests. Since ARP is mandatory for L2-to-L3 mapping, devices cannot easily hide from this scan without losing network connectivity.

## ⚙️ Technical Architecture
The tool is built using **Python** and the **Scapy** library for low-level packet crafting.



### Key Features (Module 1):
- **Ethernet Broadcast Encapsulation:** Sends frames to `ff:ff:ff:ff:ff:ff`.
- **ARP Payload Crafting:** Direct manipulation of ARP OpCodes and Target Protocol Addresses.
- **Exception Handling:** Robust error management for network interface issues.
- **Logging:** Integrated logging for audit trails.

## 🚀 Getting Started

### Prerequisites
- Python 3.10 or higher
- Npcap (Windows) or Libpcap (Linux/Mac)
- Administrative/Root privileges (required for raw socket manipulation)

### Installation & Usage
1. **Clone the repository:**
   git clone [https://github.com/](https://github.com/)[SEU-USUARIO]/Network-Guardian.git
   cd Network-Guardian
Install dependencies:


pip install -r requirements.txt
Run the scanner:

# On Linux/Mac
sudo python3 main.py

# On Windows (Run as Administrator)
python main.py
📊 Roadmap & Future Enhancements
This project is under active development:

[x] Module 1: Layer 2 Asset Discovery (Current)

[ ] Module 2: SQLite Database Persistence for "Authorized Devices" list.

[ ] Module 3: Vendor Identification via OUI API.

[ ] Module 4: Real-time Telegram Alerts for unknown device detection.

📄 Compliance & Standards
This tool is designed to assist with the following controls:

CIS Control 1.1: Establish and Maintain Detailed Enterprise Asset Inventory.

ISO/IEC 27001: Asset Management (A.8).
