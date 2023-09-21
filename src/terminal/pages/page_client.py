from terminal.pages.page import TerminalPage
from udp.client import UDPClient

PAGE_BANNER = \
'''
Client for zynq server'''

CLIENT_OPTIONS = \
'''
Client options:
1 - Test sending to zynq server
0 - Exit client page
'''

class PageClient(TerminalPage):
    def __init__(self, terminal):
        super().__init__(PAGE_BANNER, terminal)
        self.flag_client_loop = True
        self.client_loop()

    def client_loop(self):
        while self.flag_client_loop:
            print(CLIENT_OPTIONS)

            option = input("input: ")

            if option == '0':
                self.flag_client_loop = False

            elif option == '1':
                test_socket = UDPClient()
                server_ip = "192.168.122.115"
                server_port = 22
                test_socket.new_connection(server_ip, server_port) 
                test_socket.send_message(1)
            