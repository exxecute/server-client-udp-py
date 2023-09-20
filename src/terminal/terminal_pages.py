from enum import Enum
from terminal.pages.page_none import PageNone
from terminal.pages.page_help import PageHelp
from terminal.pages.page_exit import PageExit
from terminal.pages.page_client import PageClient


HELP = ["-h", "help"]
EXIT = ["-e", "exit"]
CLIENT = ["-c", "client"]

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
        for option in CLIENT:
            if option == input:
                return PageClient
        return PageNone