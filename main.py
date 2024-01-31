from pyweb import pydom
import threading
import os
import time

def click(self, event):
    i = int(event.target.getAttribute('data-x'))
    j = int(event.target.getAttribute('data-y'))
    print(f'Cell {i}, {j} clicked: ', end='')
    if self.current_player == "":
        print('game ended, nothing to do')
        return
    
def clear_terminal(self):
    self.console._js.terminal.clear()

def toggle_terminal(self, event):
    hidden = self.console.parent._js.getAttribute("hidden")
    if hidden:
        self.console.parent._js.removeAttribute("hidden")
    else:
        self.console.parent._js.setAttribute("hidden", "hidden")