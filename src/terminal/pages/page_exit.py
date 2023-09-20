from terminal.pages.page import TerminalPage

PAGE_BANNER = "Exit from client for zynq server"

class PageExit(TerminalPage):
    def __init__(self, terminal):
        super().__init__(PAGE_BANNER, terminal)
        self.terminal.flag_terminal_loop = False