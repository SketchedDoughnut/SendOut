from pyweb import pydom
import threading
import os
import time
# ---------------------------------------------------------
class Functions:
    self.filePath = 'bot/botMaster.py'

    def __init__(self):
        self.console = pydom["script#console"][0]
        print('This is a test init run of the class "Functions"')
        print('now calling on "called"')
        self.called()

    def called(self):
        print('This is a test run of the function "called" in the class "Functions"')

    def runner(self):
        try:
            os.system(self.filePath)
        except:
            print(f'File {self.filePath} does not exist.')

    def click(self, event):
        i = int(event.target.getAttribute('data-x'))
        j = int(event.target.getAttribute('data-y'))
        print(f'Cell {i}, {j} clicked: ', end='')
        #return

    def clear_terminal(self):
        self.console._js.terminal.clear()

    def toggle_terminal(self, event):
        hidden = self.console.parent._js.getAttribute("hidden")
        if hidden:
            self.console.parent._js.removeAttribute("hidden")
        else:
            self.console.parent._js.setAttribute("hidden", "hidden")

FUNCTIONS = Functions()