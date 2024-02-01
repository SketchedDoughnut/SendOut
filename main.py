import discord
from pyscript import document
import asyncio

# global variables
global key
global token

# Bot essentials
intents = discord.Intents.all()
client = discord.Client(command_prefix="!", intents=intents)

@client.event
async def on_ready():
    print('on ready')

@client.event
async def on_message(message):
    print(message)
###################################################################################################################################################

async def grabInfo(event):
    global token
    global key
    key = document.querySelector("#key")
    key = key.value
    token = document.querySelector("#token")
    token = token.value
    output_div = document.querySelector("#output")
    output_div.innerText = str(token) + str(key)

    # run the bot below
    await asyncio.gather(client.run(token))