from enum import Enum

HELP = ["-h", "help"]

class TerminalPages(Enum):
    none = 0
    help = 1

class TerminalSelectPage():
    def get_page(self, input):
        for option in HELP:
            if option is input:
                return TerminalPages.help
        return TerminalPages.none