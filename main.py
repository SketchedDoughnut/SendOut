import discord
import pyscript
import asyncio
import threading

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
    output_div.innerText = (f'{key}, {token}')

    # run the bot below
    #await asyncio.gather(client.run(token))
    client.run(token)

def running(event):
    t1 = threading.Thread(target=grabInfo,)
    t1.start()

test = 'MTE1MDg2NzE3OTk1NzQwNzkwNQ.GxeGJv.UMrOq2DyGHVDRoU9GI0CGNQYv1HudTJXp5OlnI'