from terminal_help import HELP_TEXT
from terminal_pages import TerminalPages
from terminal_pages import TerminalSelectPage

BANNER = "UDP client"

class Terminal():
    def __init__(self):
        print(BANNER)

    def wait_input(self):
        option = input("input: ")
        tsp = TerminalSelectPage()
        page = tsp.get_page(option)
