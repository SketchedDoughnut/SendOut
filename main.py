from pyweb import pydom
#import threading
import time
import os # Code import start to run bot program
from subprocess import call
from cryptography.fernet import Fernet # Code import end to run bot program

# Encrypt test file and print it
#key = Fernet.generate_key()
#fernet = Fernet(key)
#f = open('Online Bot/Master/Log.txt', 'rb')
#f = open('links.txt', 'rb')
#original = f.read()
#f.close()
#encrypted = fernet.encrypt(original)

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
        print('calling on exec')
        self.exec()

    def called(self, event): # Only needed to test, calling did work
        print('This is a placeholder function named "called" in the class "Functions" triggered by the "Run Code" button')

    def exec(self): 
        print('exec running')
        print(0)
        file_path = '/workspaces/SendOut/Online Bot/Master/botMaster.py'
        file_path = '/workspaces/SendOut/test.py'
        print(1)
        try:
            print('intry')
            #os.system(f'python3 {file_path}')
            #os.system(f'python /workspaces/SendOut/test.py')
            #os.system(f'python {file_path}')
            #execfile(f'{file_path}.py')
            #os.system('date')
            #call([f"python", "SendOut/Online Bot/Master/botMaster.py"])
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' does not exist.")
        print(2)

    #def click(self, event):
    #    i = int(event.target.getAttribute('data-x'))
    #    j = int(event.target.getAttribute('data-y'))
    #    print(f'Cell {i}, {j} clicked: ', end='')
    #    return

    def clear_terminal(self, event):
        self.console._js.terminal.clear()
    
    def toggle_terminal(self, event):
        hidden = self.console.parent._js.getAttribute("hidden")
        if hidden:
            self.console.parent._js.removeAttribute("hidden")
        else:
            self.console.parent._js.setAttribute("hidden", "hidden")

FUNCTIONS = Functions()
