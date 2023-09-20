class TerminalPage():
    def __init__(self, page_banner, terminal):
        self.page_banner = page_banner
        self.terminal = terminal

        self.print_banner()

    def print_banner(self):
        print(self.page_banner)