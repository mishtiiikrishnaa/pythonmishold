import socket
import threading

# Global variables
HOST = 'localhost'  # Server IP address (use '0.0.0.0' for all available interfaces)
PORT = 12345         # Server port number
clients = []

# Function to handle client connections
def handle_client(client_socket, address):
    print(f"Accepted connection from {address}")
    clients.append(client_socket)

    # Loop to receive and broadcast messages
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"Received message from {address}: {message}")
                broadcast(message, client_socket)
        except Exception as e:
            print(f"Connection from {address} closed: {e}")
            clients.remove(client_socket)
            client_socket.close()
            break

# Function to broadcast message to all clients
def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.sendall(message.encode('utf-8'))
            except Exception as e:
                print(f"Error broadcasting message: {e}")

# Main server setup
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))  # Bind server to specified host and port
server.listen(5)            # Listen for incoming connections

print(f"Server listening on {HOST}:{PORT}...")

# Main loop to accept incoming connections
while True:
    client_socket, address = server.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
    client_thread.start()
