import socket


def start_client():
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('localhost', 8080))
        message = client_socket.recv(1024)
        print(message.decode())
        client_socket.close()
    except ConnectionRefusedError:
        print("Error: Could not connect to the server.")

# Uncomment to run the client
# start_client()