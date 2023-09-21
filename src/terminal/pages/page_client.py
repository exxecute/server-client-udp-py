from terminal.pages.page import TerminalPage
from yaml_reader.yaml_reader import YamlServerConfigAPI
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
ZYNQ_SERVER_PATH = "./zynq-config.yaml"

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
                parser = YamlServerConfigAPI(ZYNQ_SERVER_PATH)
                test_socket.new_connection(parser.get_ip(), parser.get_port()) 
                test_socket.send_message(1)
            