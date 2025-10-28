import socket
import sys
# host is ip address for example 214.15.18.4
def check_port(host, port):
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mySocket.settimeout(1)
    
    try:
        result = mySocket.connect_ex((host, port))
        
        if result == 0:
            print(f"success Port {port} on {host} is open.")
        else:
            print(f"no {port} on {host} is close.")
            
    except socket.gaierror:
        print(f"Hostname error: Could not resolve '{host}'.")
    except socket.error as e:
        print(f"Connection error: {e}")
    finally:
        mySocket.close()


if __name__ == "__main__":
    
    hostIp = input("Please enter host ip address or domain (e.g., 4.2.2.4): ")
    
    try:
        targetPort_str = input(f"Please enter port to check on {hostIp} (e.g., 80): ")
        targetPort = int(targetPort_str)
        
        if not (0 < targetPort <= 65535):
            raise ValueError("Port must be between 1 and 65535")
            
        print(f"\nChecking {hostIp} on port {targetPort}...")
        check_port(hostIp, targetPort)
        
    except ValueError as ve:
        print(f"Error: Invalid port. Please enter a number between 1 and 65535. ({ve})")
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit()