import socket
import sys

def check_port(host, port, timeout=0.5):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        try:
            result = s.connect_ex((host, port))
            return result == 0
        except socket.gaierror:
            raise RuntimeError(f"Hostname error: Could not resolve '{host}'.")
        except socket.error as e:
            raise RuntimeError(f"Socket error: {e}")

def scan_until_open(host, start_port=1, end_port=65535, timeout=0.5):
    """Scan ports from start_port up to end_port (inclusive) and stop at first open port.
       Returns the first open port number, or None if none found."""
    if not (1 <= start_port <= 65535) or not (1 <= end_port <= 65535) or start_port > end_port:
        raise ValueError("Ports must be in range 1..65535 and start_port <= end_port")

    print(f"Scanning {host} from port {start_port} to {end_port} (timeout {timeout}s) ...")
    for port in range(start_port, end_port + 1):
        try:
            if check_port(host, port, timeout):
                print(f"✓ Open: Port {port} on {host}")
                return port
            else:
                # optional: comment out the next line to make output quieter
                print(f"- Closed: Port {port}", end="\r")
        except RuntimeError as e:
            print(f"\nFehler beim Prüfen von Port {port}: {e}")
            return None
    print("\nKein offener Port gefunden im angegebenen Bereich.")
    return None

if __name__ == "__main__":
    try:
        host = input("Bitte Host (IP oder Domain, z.B. 127.0.0.1): ").strip()
        # Beispiel: stoppe beim ersten offenen Port (1..1024) — passe Bereich an
        first_open = scan_until_open(host, start_port=1, end_port=65535, timeout=0.3)
        if first_open is not None:
            print(f"Erster gefundener offener Port: {first_open}")
        else:
            print("Kein offener Port gefunden.")
    except KeyboardInterrupt:
        print("\nAbgebrochen vom Benutzer.")
        sys.exit(0)
    except ValueError as ve:
        print(f"Fehler: {ve}")
        sys.exit(1)


#Ende 