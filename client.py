import socket
import threading

name = input("Введите свое имя: ")
server_ip = "127.0.0.1"
server_port = 12345
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))
def send_message():
    while True:
        message = f"{name}: {input()}"
        client_socket.send(message.encode('utf-8'))

def receive_message():
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        print(message)

send_thread = threading.Thread(target=send_message)
receive_thread = threading.Thread(target=receive_message)
send_thread.start()
receive_thread.start()