import socket
import threading
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = "127.0.0.1"
server_port = 12345
server_socket.bind((server_ip, server_port))
server_socket.listen(5)
print(f"{server_ip}:{server_port}")
clients = []
def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                print("Клиент отключился")
                clients.remove(client_socket)
                client_socket.close()
                break
            else:
                print(f"{message}")

                for client in clients:
                    if client != client_socket:
                        client.send(message.encode('utf-8'))
        except Exception as e:
            print(f"Ошибка при обработке сообщения: {str(e)}")
            clients.remove(client_socket)
            client_socket.close()
            break

while True:
    client_socket, client_address = server_socket.accept()
    print(f"new{client_address}")
    clients.append(client_socket)
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()