import socket

class NetworkManager:
    def __init__(self, host="127.0.0.1", port=12345):
        self.host = host
        self.port = port
        self.client_socket = None

    def connect(self):
        """
        Connects the client to the server.
        """
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))
        print(f"Connected to server at {self.host}:{self.port}")

    def send_data(self, data):
        """
        Sends data to the server.
        :param data: Data to send.
        """
        if self.client_socket:
            self.client_socket.sendall(data.encode("utf-8"))
            print("Data sent to server.")

    def receive_data(self):
        """
        Receives data from the server.
        :return: Received data.
        """
        if self.client_socket:
            data = self.client_socket.recv(1024)
            print(f"Received data from server: {data.decode('utf-8')}")
            return data.decode("utf-8")

    def close_connection(self):
        """
        Closes the connection to the server.
        """
        if self.client_socket:
            self.client_socket.close()
            print("Connection closed.")

# Example usage
if __name__ == "__main__":
    network_manager = NetworkManager()
    network_manager.connect()
    network_manager.send_data("Hello, Server!")
    response = network_manager.receive_data()
    network_manager.close_connection()