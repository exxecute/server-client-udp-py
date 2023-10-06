from terminal.pages.page import TerminalPage
from yaml_reader.yaml_reader import YamlServerConfigAPI
from udp.client import UDPClient

PAGE_BANNER = \
'''
Client for zynq server'''

CLIENT_OPTIONS = \
'''
Client options:
0 - Exit client page
1 - Test sending to zynq server
'''
ZYNQ_SERVER_PATH = "./zynq-config.yaml"

MAX_BYTE = 255

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
                socket = UDPClient()
                parser = YamlServerConfigAPI(ZYNQ_SERVER_PATH)
                socket.new_connection(parser.get_ip(), parser.get_port())

                while True:
                    test_byte = int(input("input test byte: "))
                    if(test_byte <= MAX_BYTE):
                        break

                # test_protocol = TestProtocol(test_byte)  
                # socket.send_message(test_protocol.get_request())

                # print("recieved data:", socket.receive_message())