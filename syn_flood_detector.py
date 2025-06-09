from scapy.all import sniff, TCP, IP

def detect_syn(pkt):
    if TCP in pkt and pkt[TCP].flags == "S":
        print(f"[!] Possible SYN Flood from {pkt[IP].src}")

print("[*] Monitoring for SYN Flood (Ctrl+C to stop)")
sniff(filter="tcp", prn=detect_syn, store=0)