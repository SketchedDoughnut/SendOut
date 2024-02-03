import discord
import pyscript

from contextlib import contextmanager, suppress
import asyncio
import requests
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

async def runBot(token):                                                                      ####### Attempted ideas below, tagged out
    #nest_asyncio.apply(client.run(token))
    #asyncio.get_event_loop().run_until_complete(client.run(token))
    #nest_asyncio.apply(asyncio.get_event_loop().run_until_complete(client.run(token)))
    #nest_asyncio.apply(asyncio.run(client.run(token)))
    #nest_asyncio._patch_asyncio()
    # loop = asyncio.get_event_loop()
    # loop.set_debug(False)
    # task = asyncio.ensure_future(client.run(token))
    # with suppress(asyncio.CancelledError):
    #     loop.run_until_complete(task)
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:  # 'RuntimeError: There is no current event loop...'
        loop = None
    if loop and loop.is_running():
        print('Async event loop already running. Adding coroutine to the event loop.')
        tsk = loop.create_task(client.start(token))
        # ^-- https://docs.python.org/3/library/asyncio-task.html#task-object
        # Optionally, a callback function can be executed when the coroutine completes
        #tsk.add_done_callback(
        #    print(f'Task done with result={t.result()}  << return val of main()'))
    else:
        print('Starting new event loop')
        result = asyncio.run((client.start(token)))
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
    asyncio.create_task(runBot(token))
    # loading = pyscript.document.querySelector("#loading")
    # loading.innerText = " "



# for JSON
    # ,"ports": ["53:53", "53:53/udp"]