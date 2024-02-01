import discord
import pyscript

from contextlib import contextmanager, suppress
import asyncio
#asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
import nest_asyncio

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

def runBot(token):
    #nest_asyncio.apply(client.run(token))
    #asyncio.get_event_loop().run_until_complete(client.run(token))
    #nest_asyncio.apply(asyncio.get_event_loop().run_until_complete(client.run(token)))
    #nest_asyncio.apply(asyncio.run(client.run(token)))
    #nest_asyncio._patch_asyncio()
    loop = asyncio.get_event_loop()
    loop.set_debug(False)
    task = asyncio.ensure_future(client.run(token))
    with suppress(asyncio.CancelledError):
        loop.run_until_complete(task)
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
    #asyncio.get_event_loop().run_until_complete(runBot(token))
    #nest_asyncio.apply()(r)
    runBot(token)
    # loading = pyscript.document.querySelector("#loading")
    # loading.innerText = " "