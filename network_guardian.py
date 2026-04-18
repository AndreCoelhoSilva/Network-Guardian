import scapy.all as scapy
import time

class NetworkGuardian:

    def __init__(self, interface):
        self.interface = interface
        self.authorized_devices = []

    def build_arp_request(self, target_ip):
        arp = scapy.ARP(pdst=target_ip)
        ether = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

        return ether / arp
    
    def perform_scan(self, network_range):

        packet = self.build_arp_request(network_range)

        answered, _ = scapy.srp(packet, timeout=2, retry=1, verbose=False)

        discovered_List = []
        for sent, received in answered:
            device = {
                "ip": received.psrc,
                "mac": received.hwsrc,
                "discovery_time": time.ctime()
            }
            discovered_List.append(device)
        
        return discovered_List