#Start


import socket
import sys

def is_port_open(host: str, port: int, timeout: float = 0.3) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        try:
            return s.connect_ex((host, port)) == 0
        except (socket.gaierror, socket.error):
            return False

def full_scan(host: str, start: int = 1, end: int = 1024, timeout: float = 0.2):
    if not (1 <= start <= end <= 65535):
        raise ValueError("Ungültiger Portbereich")
    open_ports = []
    print(f"Starte Vollscan {host} von {start} bis {end} ...")
    for port in range(start, end + 1):
        if is_port_open(host, port, timeout):
            print(f"✓ Offen: {port}")
            open_ports.append(port)
        else:
            print(f"- Geschlossen: {port}", end="\r")
    print("\nScan abgeschlossen.")
    return open_ports

if __name__ == "__main__":
    host = input("Host (z.B. 127.0.0.1): ").strip()
    try:
        # Standard hier 1..1024 (well-known), den Bereich anpassen falls nötig
        opens = full_scan(host, start=1, end=1024, timeout=0.2)
        if opens:
            print("Offene Ports:", opens)
        else:
            print("Keine offenen Ports im Bereich gefunden.")
    except KeyboardInterrupt:
        print("\nAbgebrochen.")
        sys.exit(0)


#Ende