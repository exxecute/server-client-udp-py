from terminal.pages.page import TerminalPage
from terminal.terminal_help import HELP_TEXT

PAGE_BANNER = HELP_TEXT

class PageHelp(TerminalPage):
    def __init__(self, terminal):
        super().__init__(PAGE_BANNER, terminal)