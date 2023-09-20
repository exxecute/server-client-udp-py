from terminal.pages.page import TerminalPage

PAGE_BANNER = \
'''
Client for zynq server'''

CLIENT_OPTIONS = \
'''
Client options:
1 - Test sending
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
                print("Test sending")
            