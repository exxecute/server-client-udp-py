import socket

class SocketAPI():
    def __init__(self, IP, port):
        self.create_socket(IP, port)

    def create_socket(self, IP, port):
        self.server_address_port = (IP, port)
        self.client_socket = socket.socket(family= socket.AF_INET, type= socket.SOCK_DGRAM)

    def send_to(self, bytes_to_send):
        self.client_socket.sendto(bytes_to_send, self.server_address_port)

    def recieve_from(self):
        return self.client_socket.recvfrom(1024)