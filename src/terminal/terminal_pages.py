from enum import Enum
from terminal.pages.page_none import PageNone
from terminal.pages.page_help import PageHelp
from terminal.pages.page_exit import PageExit

HELP = ["-h", "help"]
EXIT = ["-e", "exit"]

class TerminalPages(Enum):
    none = 0
    help = 1
    exit = 2

class TerminalSelectPage():
    def get_page(self, input):
        for option in HELP:
            if option == input:
                return PageHelp
        for option in EXIT:
            if option == input:
                return PageExit
        return PageNone