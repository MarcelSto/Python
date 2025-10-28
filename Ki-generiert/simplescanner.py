#Start


import socket
import sys

def is_port_open(host: str, port: int, timeout: float = 0.5) -> bool:
    """Gibt True zurück, wenn Port offen ist."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        try:
            return s.connect_ex((host, port)) == 0
        except (socket.gaierror, socket.error):
            return False

def scan_until_first_open(host: str, start: int = 1, end: int = 65535, timeout: float = 0.3):
    if not (1 <= start <= end <= 65535):
        raise ValueError("Ungültiger Portbereich")
    print(f"Scanning {host} von {start} bis {end} (stoppt beim ersten offenen Port)...")
    for port in range(start, end + 1):
        if is_port_open(host, port, timeout):
            print(f"✓ Offen: Port {port} auf {host}")
            return port
        else:
            # Optional: Anzeige leiser machen; hier schreiben wir mit \r
            print(f"Prüfe Port {port}...", end="\r")
    print("\nKein offener Port gefunden.")
    return None

if __name__ == "__main__":
    host = input("Host (IP oder Domain, z.B. 127.0.0.1): ").strip()
    try:
        found = scan_until_first_open(host, start=1, end=65535, timeout=0.25)
        if found:
            print(f"Erster gefundener offener Port: {found}")
        else:
            print("Kein offener Port gefunden.")
    except KeyboardInterrupt:
        print("\nAbgebrochen.")
        sys.exit(0)


#End