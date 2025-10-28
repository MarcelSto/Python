#Start - portscanner

import socket
import sys

def check_port(host, port):
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mySocket.settimeout(1)

    try:
        result = mySocket.connect_ex((host, port))

        if result == 0:
            print(f"Port {port} on {host} is open.")
        else:
            print(f"No {port} on Host {host} is closed.")
    

    except socket.gaierror:
        print(f"Hostname error: Could not resolve '{host}'.")
    except socket.error as e:
        print(f"Connection error: {e}")
    finally:
        mySocket.close()



if __name__ == "__main__":

    hostIP = input("Please enter host ip adress or domain (e.g., 4.2.2.4): ")

    try:
        targetPort_str = input(f"Please enter port to check on {hostIP} (e.g., 80): ")
        targetPort = int


