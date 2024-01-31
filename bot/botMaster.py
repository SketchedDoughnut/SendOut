import discord
import requests
from multiprocessing import Process
import multiprocessing
import time
import typing  # For typehinting
import functools
import os

# other .py files
import channelFunctionsMaster
from channelFunctionsMaster import dmList
from channelFunctionsMaster import nameList

#from channelFunctionsMaster import channel

#import termCheck

# Chat GPT
import selectors
import sys
import threading
import asyncio

# Bot essentials
intents = discord.Intents.all()
client = discord.Client(command_prefix="!", intents=intents)


# All globals and defaults
global viewState
viewState = 'n'
global prevMessageID
prevMessageID = 0
global sendoffMsg
sendoffMsg = 'n'
global respond
respond = 'n'
global username
username = 'n'
global channel
channel = channelFunctionsMaster.init() ####################################################################
channel = client.get_channel(int(channel))

# Functions
def logger(msg, test):  # For logging all messages to log.txt
  if test == True:
    f = open("Online Bot/Master/log.txt", "w", encoding = 'utf8')
    f.write('clear\n----------\n')
    f.close()
    print('Logs cleared.')

    print('logging function is working.')
  else:
    f = open("Online Bot/Master/log.txt", "a", encoding = 'utf8')
    f.write(msg + '\n')
    f.close()
# ===========================================================
@client.event
async def on_ready():
  global viewState
  global username
  global message
  global channel
  #global username
  #global priv
  #global teal
  global billybob

  def termCheck(msg):
    global username
    global billybob

    # return 23 only for changing username
    # return 0 for all other cases, acts as a return "True" which means this function did something and other operations aren't needed.

    # - Checking for username swapping
    msgList = [str(i) for i in msg]
    if msgList[0] == '=':
      for i in range(2):
        msgList.pop(0)
      msg = "".join(msgList)
      username = msg
      print('---------------------')
      print('Username changed to: ' + username)
      logger('username changed to: ' + username, False)
      print('---------------------')
      return 23

    
    # - Checking for quit and help commands
    elif msgList[0] == '~':
      if msg == '~ quit':
        print('ending program')
        client.close
        print(client.is_closed)
        try:
          stop()
        except:
          print('fq at prompt to quit.')
          time.sleep(1)
          exit(1)

      if msg == '~ help':
        channelFunctionsMaster.commands()
        return 0
      
      if msg == '~ clear-image':
          channelFunctionsMaster.clearImage()

      if msg == '~ clear':
        channelFunctionsMaster.ccp() 
        return 0
      
      if msg == '~ export':
        channelFunctionsMaster.export()
      
      if msg == '~ clear-export':
        channelFunctionsMaster.clearExport()

      if msg == '~ lam':
        channelFunctionsMaster.lam()

      #if msg == '~ delete':
        #prevMessageID.delete()

      if msg == '~ mute':
        channelFunctionsMaster.muter()

      if msg == '~ unmute':
        channelFunctionsMaster.unmuter()
    

    # - Checking for channel category inputs, and passing on data
  
    ## - inputting list  
    elif msgList[0] == '-':  # narrows down to prompts for channel functions
      if msgList[1] == 'l': # narrows down to inputting list
        #print('FA1: ' + str(channelFunctionsMaster.formattingAgent(1, msgList, 'x')))
        channelFunctionsMaster.formattingAgent(1, msgList, 'x')
        return 0
        
      elif msgList[1] == 'r':
        print('Channel reset to: ' + str(client.get_channel(channelFunctionsMaster.reset())))
        print('---------------------')
        return 0

      elif msgList[1] == 'c':
        os.system('clear')
        print('---<cc-s 2-1>---')
      
      elif msgList[1] == 's':
        if msgList[2] == 'l':
          CHL = channelFunctionsMaster.listAll()
          print('Channels: ')
          for i in range(len(CHL)):
            print('  -' + str(client.get_channel(int(CHL[i]))) + ', ' + channelFunctionsMaster.nameList[i] + ', ' + str(i))
          print('---------------------')
          return 0
        #elif msgList[1] == 's':
        else:
          print('---------------------')
          print('transferring to second file under FA2.')
          temp1 = "".join(msgList)
          temp1 = temp1.split()
          for i in range(1):
            temp1.pop(0)
          print('current id: ' + str(client.get_channel(int(channelFunctionsMaster.formattingAgent(3, 'x', int(temp1[0]))))))
          #print('FA2: ' + str(channelFunctionsMaster.formattingAgent(2, 'x', str(msgList))))
          channelFunctionsMaster.formattingAgent(2, 'x', int(temp1[0]))
          print('new id: ' + str(client.get_channel(int(channelFunctionsMaster.formattingAgent(3, 'x', int(temp1[0]))))))
          billybob = client.get_channel(int(channelFunctionsMaster.formattingAgent(3, 'x', int(temp1[0]))))
          print('server: ' + billybob.guild.name)
          print('---------------------')
          return 0


    else: # If all are false, then it returns this to continue
      return False

              
  async def keyDetect(test, num, msg):  # For detecting when the key is pressed to send messages
    #global sending
    global channel
    global username
    if test == True:
      print('Key detecting function is working.')
      print('<n>')
    
    if num == 0:
      while True:
        print('<wl>')
        break
    check = termCheck(msg)
    
    if check == 23:
      channel = channelFunctionsMaster.formattingAgent(3, 'x', 'x')
      #print(2)
      #channel = client.get_channel(channel)
      channel = client.get_channel(channelFunctionsMaster.dmList[0])
      await channel.send('Username changed to: ' + username)
    if check == False or (check == 0) == True:
      if num == 1:

        if viewState == "M":
          msgList = [str(i) for i in msg]
          #print(msgList)
          if msgList[0] == "+":
            print('You are in monitor mode, response is not available.')

        if viewState == "R":
          msgList = [str(i) for i in msg]
          #print(msgList)
          #bob = True
          #while bob == True:
          bobby = False
          if msgList[0] == "/":
              bobby = True
          if msgList[0] == "+" or msgList[0] == "/":
            print('---------------------')
            print('<rh>')
            #sendoffMsg = input()
            for i in range(2):
              msgList.pop(0)
            sendoffMsg = "".join(msgList)
            channel = channelFunctionsMaster.formattingAgent(3, 'x', 'x')
            channel = client.get_channel(channel)
            if bobby == True:
              print('msg is (tagless): ' + sendoffMsg)
              logger('---> Msg (tagless)(' + channel.guild.name + '): ' + username + ': ' + sendoffMsg, False)
            else:
              print('msg is: ' + sendoffMsg)
              logger('---> Msg(' + channel.guild.name + '): ' + username + ': ' + sendoffMsg, False)
            #bob = False
          #print(channel)
          channel = channelFunctionsMaster.formattingAgent(3, 'x', 'x')
          #print(3)
          channel = client.get_channel(channel)
          if bobby == False:
            await channel.send('**' + username + ' said:** ' + sendoffMsg)
          else:
            await channel.send(sendoffMsg)
          await queue.put(sendoffMsg) # chat GPT
          channel = channelFunctionsMaster.formattingAgent(3, 'x', 'x')
          channel = client.get_channel(channel)
          #print('channel is: ' + str(client.get_channel(channel)))
          print('channel is: ' + str((channel)))
          print('server is: ' + str(((channel.guild.name))))
          print('sent!')
          print('---------------------')
        # await message.channel.send(userInfo + ' said: ' + sendoffMsg)

    # Chat GPT 
  def console_input_checker():
    sel = selectors.DefaultSelector()
    sel.register(sys.stdin, selectors.EVENT_READ)
    
    while True:
        # Check for events (input from console)
        events = sel.select()
        for key, mask in events:
            if key.fileobj == sys.stdin and mask & selectors.EVENT_READ:
              sendChoice = input()
              # x = await keyDetect(False, 1, sendChoice)
              # loop = asyncio.get_event_loop()
              # asyncio.set_event_loop(loop) # fixes no loop in this function issue?
              # loop = asyncio.new_event_loop()
              asyncio.run_coroutine_threadsafe(keyDetect(False, 1, sendChoice), client.loop)
              # asyncio.set_event_loop(loop)
              tasks = list()
              #tasks.append(asyncio.create_task(keyDetect(False, 1, sendChoice)))
              tasks.append(keyDetect(False, 1, sendChoice))
              try:
                loop.run_until_complete(asyncio.wait(tasks))
              except:
                try:
                  #print('1 fail, 2 try') PRINT ---------------
                  loop.run_until_complete(asyncio.wait(keyDetect(False, 1, sendChoice, queue)))
                  asyncio.run(keyDetect(False, 1, sendChoice))
                except:
                  #print('1 fail, 2 fail') PRINT ----------------------
                  break
                
              # loop.close()

              
              #print(f"Received console input: {sendChoice}") PRINT ----------------------
  try:
    os.system('cls')
    print('cc-s 1')
    console.clear
  except:
    try:
      os.system('clear')
      print('---<cc-s 2-1>---')
    except:
      print('cc f')
        
    
  print('---------------------')
  logger('x', True)

  #async def constantLoopSend(sendoff):
    #global channel
    #global priv
    #print('loop send started.')
    #while True:~ 
      #if len(sendoff) < 0:
        #channel = client.get_channel(priv)
        #print('channel is: ' + str(channel))
        #await channel.send(username + ' said: ' + sendoff)
        #print('msg send')

  #sendProc = Process(target=await constantLoopSend(sendoffMsg))
  #sendProc.start()
  
  #if __name__ == "__main__":  # confirms that the code is under main function
    #keyProc = Process(target=keyDetect(True))  # instantiating without any argument
    # Establish keyboard check for test
    #keyProc.start()
    #time.sleep(2)
    #keyProc.terminate()
    #keyProc.close()
    #keyProc = Process(target=keyDetect(False))
    #keyProc.start()

    # Establish inputCheck for test
    #inputCheck = Process(target=await getInput(150))
    #inputCheck.start()
    #time.sleep(2)
    #inputCheck.terminate()
    #inputCheck.close()
    #inputCheck = Process(target=await getInput(1))
  queue = asyncio.Queue() # CHAT GPT GAHDGSS#######################################
  channelFunctionsMaster.formattingAgent(0, 'x', 'x')
  await keyDetect(True, 0, 'n')
  #getInput(150)

  print("Number of cpu : ", multiprocessing.cpu_count())  # Info, CPU cores(?)

  time.sleep(0.15)
  print('Bot is ready.')
  print('---------------------')
  # Get ID's from every single server the bot is in
  activeservers = client.guilds
  for guild in activeservers:
    print('Server: ' + str(guild.name))
    activechannels = guild.channels
    for channels in activechannels:
      print(' -' + str(channels.name))
      #client.get_channel(channels)
      channelFunctionsMaster.dmList.append(channels.id) # channels id
      channelFunctionsMaster.nameList.append(guild.name)
    print(" ")
  print(channelFunctionsMaster.dmList) # move this forward to print every cycle for debug
  print(channelFunctionsMaster.nameList) # move this forward to print every cycle for debug
  #time.sleep(120)
  time.sleep(0.25)
  try:
    os.system('cls')
    print('cc-s 1')
    console.clear
  except:
    try:
      os.system('clear')
      print('---<cc-s 2-2>---')
      print('You are using the master version of the bot. Full abilities available.')
    except:
      print('---<cc f>---')

  # Get info from user
  username = input('Please input your name below: ')
  viewState = input(
      'Do you want to monitor or respond during this session? (M/R)- ')

  # Viewstate - respond notes
  if viewState.lower() == "R":
    print('Enter "+", then your message (like "+ test" to send a message.')

  # First msg
  #firstV = input('Do you want first msg? (Y/N) \n')
  #if firstV == "Y":
    #print('>response>')
    #firstMsg = input()
  #print('default channel is priv.')
  #channel = client.get_channel(1081794985466273942) # is default, priv
  channel = channelFunctionsMaster.init()
  channel = client.get_channel(channel)
  print('default channel: ' + str(channel))
  print('---------------------')
  print('Setup complete. For help, ~ help')
  print('---------------------')

  # Send message alerting others of bot mode and what to expect
  
  #channel = client.get_channel(priv) ##########################################################################################################################
  #if viewState == "M":
    #await channel.send('```Bot is online. User is: ' + username + '\n' +
                       #'Mode is monitor. Wont respond.```')
  if viewState == "R":
    channel = (channelFunctionsMaster.formattingAgent(3, 'x', 'x'))
    #print(1)
    channel = client.get_channel(channel)
    await channel.send('```Bot is online. User is: ' + username + '\n' +
                       'Mode is respond. Will respond.```')
    #print('online message sent.')

  #if firstV == "Y":  
    #channel = client.get_channel(teal)
    #await channel.send('From ' + username + ': ' + firstMsg)

  # Chat GPT
   #Start the console input checking thread - WORKS TO GET INPUT
  console_thread = threading.Thread(target=console_input_checker)
  console_thread.daemon = True
  console_thread.start()
# ===========================================================
@client.event
async def on_message(message):
  global viewState
  global username
  global sendoffMsg
  global channel
  global prevMessageID

  if message.author == client.user:
    prevMessageID = message.id
    return
  else: 
    if channelFunctionsMaster.mute == True:
      if message.channel.id != channelFunctionsMaster.currentChannel:
        #print('Message is not from the current channel; ignoring')
        return
  
    
  # Get message from Discord and send it into console
  GetUser = message.author.id
  try:
    GetUser2 = await client.fetch_user(GetUser)
  except:
    print('GU2 error')
    print(GetUser)
    GetUser2 = 0
  consoleMsg = 'Msg (' + str(client.get_channel(message.channel.id)) + ')(' + str(client.get_guild(message.guild.id)) + '): ' + str(GetUser2) + ': ' + message.content
  if len(message.attachments) > 0:
    print('!! ATTACHMENT FOUND !!')
    try:
      try:
        counter = 0
        for image in message.attachments:
          tempspaghetti = await client.fetch_user(message.author.id)
          channelFunctionsMaster.downloadImage(image.url, tempspaghetti)
          counter += 1
      except:
        pass
      print(f'Downloaded image to "Images" folder ({counter})')
    except:
      pass
  print(consoleMsg)  # Print message from discord
  print('------')
  if len(message.attachments) > 0:
    logger('!! ATTACHMENT FOUND !!', False)
    logger(consoleMsg, False)
  else:
    logger(consoleMsg, False)  # Log message from Discord
  
  # inputCheck.start()

# run below
var = input('a: ')
if var == 'fq':
  client.close
  print(client.is_closed)
  try:
    stop()
  except:
    print('quitting.')
elif var == 'x':
  try:
    #client.run(os.getenv('uwu'))
    tempIDEK = input('enter token: ')
    client.run(tempIDEK)
  except:
    print('Wrong code inputted.')
