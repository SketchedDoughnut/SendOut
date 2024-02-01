import discord
from pyscript import display

# Bot essentials
intents = discord.Intents.all()
client = discord.Client(command_prefix="!", intents=intents)

@client.event
async def on_ready():
    print('on ready')

@client.event
async def on_message(message):
    print(message)

client.run(str(input()))
###################################################################################################################################################
class test:
    def __init__(self, event):
        print('hello!')
        
    def test(self, event):
        display('hello again!')

TEST = test()