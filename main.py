"""
---> HTML tags to grab and change index (ex: #test):
- #output: check for "outputTemp" text on the page; this can be changed with updates from the python file
- #loadingFace: A cute lil face that just sits there
- #loading: Text to display a loading state
- #token: The bot token that is inputted into the website to run the bot
- #key: the decryption key (undecided whether to use or not)
- #inputPrompt: a prompt for input below it
"""

import discord
import pyscript

from contextlib import contextmanager, suppress
import asyncio
import requests
import nest_asyncio

############# an attempt to get SSL to work
import socket
import ssl
############# an attempt to get SSL to work
    
# global variables
global key
global token

# Bot essentials
intents = discord.Intents.all()
client = discord.Client(command_prefix="!", intents=intents)

@client.event
async def on_ready():
    eDiv('output','bot is on ready')

@client.event
async def on_message(message):
    print(message)

###################################################################################################################################################

def grabInfo():
    global token
    global key
    key = pyscript.document.querySelector("#key")
    key = key.value
    token = pyscript.document.querySelector("#token")
    token = token.value
    eDiv('displayInfo', f'key: {key} \n token: {token}')
    eDiv('output', 'grabInfo/status: starting runBot function with asyncio', add=True)
    eDiv('output', f'--> token: {token}', add=True)
    eDiv('output', f'    --> type: {type(token)}', add=True)
    asyncio.create_task(runBot(str(token)))
    eDiv('output', 'grabInfo/status: runBot asyncio loop started', add=True)


async def runBot(token): 
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:  # 'RuntimeError: There is no current event loop...'
        loop = None
    if loop and loop.is_running():
        #print('Async event loop already running. Adding coroutine to the event loop.')
        #eval(client.start(token))
        tsk = loop.create_task(client.run(token)) 
        eDiv('output', 'runBot/status: async already running, adding crouton to event loop', add=True)
        
        # ^-- https://docs.python.org/3/library/asyncio-task.html#task-object
        # Optionally, a callback function can be executed when the coroutine completes
        # tsk.add_done_callback(
        #    print(f'Task done with result=()  << return val of main()'))

    else:
        #print('Starting new event loop')
        #eval(client.start(token))
        result = asyncio.run(client.run(token))
        eDiv('output', 'runBot/status: starting new event loop', add=True)


def SSLsetup():
    hostname = 'https://sketcheddoughnut.github.io/SendOut/'
    context = ssl.create_default_context()

    with socket.create_connection((hostname, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            eDiv('output', ssock.version(), add=True)

            
def eDiv(tag, input, add=False):
    div = pyscript.document.querySelector(f"#{tag}")
    if add == True:
        div.innerText += f'\n {input}'
    elif add == False:
        div.innerText = input


def sysRun(event):
    clear = True
    if clear == True:
        eDiv('output', " ")
    eDiv('output', 'sysRun/status: grabbing info', add=True)
    eDiv('inputPrompt', " ")
    grabInfo()
    # eDiv('output', 'sysRun/status: setting up SSL', add=True)
    # SSLsetup()