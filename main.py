import discord
import pyscript
import asyncio
import threading
import time

# global variables
global key
global token

# Bot essentials
intents = discord.Intents.all()
client = discord.Client(command_prefix="!", intents=intents)

@client.event
async def on_ready():
    output_div.innerText = 'bot is on ready'

@client.event
async def on_message(message):
    print(message)

def runBot():
    global token
    token = ' '
    client.run(token)
###################################################################################################################################################
#@pyscript_executor
def grabInfo(event):
    global token
    global key
    global output_div
    key = pyscript.document.querySelector("#key")
    key = key.value
    token = pyscript.document.querySelector("#token")
    token = token.value
    output_div = pyscript.document.querySelector("#output")
    output_div.innerText = (f'key: {key} \n token: {token}')

    # loading = pyscript.document.querySelector("#loading")
    # loading.innerText = " "
    runBot()
    # run the bot below
    #await asyncio.gather(client.run(token))
