from udp.socket import SocketAPI

class UDPClient():
    def __init__(self):
        pass

    def new_connection(self, IP, port):
        self.socket = SocketAPI(IP, port)

    def send_message(self, message):
        self.socket.send_to(message)

    def receive_message(self):
        return self.socket.recieve_from()