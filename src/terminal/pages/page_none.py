from terminal.pages.page import TerminalPage

PAGE_BANNER = "Error syntax"

class PageNone(TerminalPage):
    def __init__(self, terminal):
        super().__init__(PAGE_BANNER, terminal)