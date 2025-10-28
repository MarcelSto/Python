import socket

HOST = '185.243.132.214'
PORT = 80

message_to_send = "hello server!"
print(f"[*]try connect server {HOST}:{PORT}...")

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print(f"[+] success server connect!!!!!")
        
        print(f"[>] sending our message'{message_to_send}'")
        s.sendall(message_to_send.encode())
        
        # waiting response
        data = s.recv(1024)
        received_message = data.decode()
        print(f"[>] answer from server: '{received_message}'")

except ConnectionRefusedError:
    print("[!] error connect server xo ")
except Exception as e:
    print(f"[!] unexpected error happens!  {e}")

print("[*]connection closed")