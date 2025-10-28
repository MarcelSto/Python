#Start



import socket
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

def is_port_open(host: str, port: int, timeout: float = 0.25) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        try:
            return s.connect_ex((host, port)) == 0
        except (socket.gaierror, socket.error):
            return False

def threaded_scan(host: str, start: int = 1, end: int = 65535, timeout: float = 0.25, max_workers: int = 200):
    if not (1 <= start <= end <= 65535):
        raise ValueError("Ungültiger Portbereich")
    if max_workers < 1:
        raise ValueError("max_workers muss >= 1 sein")
    ports = range(start, end + 1)
    open_ports = []

    print(f"Starte parallelen Scan {host} von {start} bis {end} (workers={max_workers}) ...")
    with ThreadPoolExecutor(max_workers=max_workers) as exe:
        future_to_port = {exe.submit(is_port_open, host, p, timeout): p for p in ports}
        for future in as_completed(future_to_port):
            port = future_to_port[future]
            try:
                if future.result():
                    print(f"✓ Offen: {port}")
                    open_ports.append(port)
            except Exception as e:
                # Fehler protokollieren, aber Scan fortsetzen
                print(f"\nFehler bei Port {port}: {e}")
    open_ports.sort()
    print("Scan abgeschlossen.")
    return open_ports

if __name__ == "__main__":
    host = input("Host (z.B. 127.0.0.1): ").strip()
    try:
        # Beispiel: scanne 1..65535 mit 200 Threads (anpassen je nach Maschine & Netzwerk)
        found = threaded_scan(host, start=1, end=65535, timeout=0.2, max_workers=200)
        print("Gefundene offene Ports:", found)
    except KeyboardInterrupt:
        print("\nAbgebrochen.")
        sys.exit(0)


#Ende