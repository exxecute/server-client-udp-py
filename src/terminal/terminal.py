from terminal.terminal_pages import TerminalSelectPage

BANNER = "UDP client"

class Terminal():
    def __init__(self):
        print(BANNER)
        self.flag_terminal_loop = True

    def wait_input(self):
        option = input("input: ")
        tsp = TerminalSelectPage()
        page = tsp.get_page(option)  
        page(self)   

    def terminal_loop(self):
        while self.flag_terminal_loop:
            self.wait_input()