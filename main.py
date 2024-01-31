from pyweb import pydom
#import threading
import os
#import time

class Functions:

    ### merged init from TicTacToe template and my own code
    def __init__(self):
        
        ### init code from TicTacToe that I For some reason need
        self.board = pydom["table#board"]
        self.status = pydom["h2#status"]
        self.console = pydom["script#console"][0]

        ### Init code I made
        print('Bot setup')
        print('---')
        print('now calling on runner')
        self.exec()

    def called(self): # Only needed to test, calling did work
        print('This is a test run of the function "called" in the class "Functions"')

    def exec(self): 
        print(0)
        file_path = ('SendOut/Online Bot/Master/botMaster.py')
        print(1)
        try:
            os.system(f'python {file_path}')
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' does not exist.")
        print(2)

    #def click(self, event):
    #    i = int(event.target.getAttribute('data-x'))
    #    j = int(event.target.getAttribute('data-y'))
    #    print(f'Cell {i}, {j} clicked: ', end='')
    #    return

    def clear_terminal(self):
        self.console._js.terminal.clear()
    
    def toggle_terminal(self, event):
        hidden = self.console.parent._js.getAttribute("hidden")
        if hidden:
            self.console.parent._js.removeAttribute("hidden")
        else:
            self.console.parent._js.setAttribute("hidden", "hidden")

FUNCTIONS = Functions()
