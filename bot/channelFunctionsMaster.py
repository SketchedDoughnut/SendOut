import discord
import requests
import os
import shutil
import random
import json
import time
import voiceClient


global currentChannel
global dmList
global default
global deleteLog
global counter
global mute
mute = False
counter = 0
deleteLog = []


# dmList = []
#dmList = os.getenv('cl')
#1157059983876296816 = Buffer
#1081794985466273942 = Priv
#1151174223465824357 = Teal
#1090524701744431197 = Taco
#Sketched ID: <@604883421742891130>
#Teal ID: <@513597434732085273>
#dmList = 1157059983876296816, 1081794985466273942, 1151174223465824357, 1090524701744431197
default = 1157059983876296816 # buffer
dmList = [default]
nameList = ['BotServerTesting']

# Bot essentials
intents = discord.Intents.all()
client = discord.Client(command_prefix="!", intents=intents)

# Set up default for setup 
def init():
  # globals
  global currentChannel
  currentChannel = default 
  return default
  



def formattingAgent(mode, listIn, num):
  # globals
  global currentChannel
  global dmList
  global client
  
  # mode 0: test
  # mode 1: input list
  # mode 2: select which channel
  # mode 3: output selected channel

 # Proof of function working
  if mode == 0:
    print('Channel formatter is working.')

  if mode == 1:
    print('---------------------')
    dmList = listIn
    #print('recieved listIn: ' + str(dmList))
    #msgList.replace(",", "")
    for i in range(dmList.count(',')):
      target_index = dmList.index(",")
      dmList[target_index] = " "
    for i in range(3):
      dmList.pop(0)
    msg = "".join(dmList)
    dmList = msg.split()
    print('formatted: ' + str(dmList))
    print('Defaulting to first: ' + dmList[0])
    currentChannel = int(dmList[0])
    print('---------------------')
    return int(currentChannel)
    #channel = client.get_channel(msgList[0])

  if mode == 2: 
    # Debugger below to split up the list into their individual characters. 

    #for i in range(len(num)):
      #print('i: ' + str(i) + ' index: ' + str(num[i]))
    #currentChannel = int(dmList[int(num[17])])
    try:                                                                    ###########
      currentChannel = int(dmList[num]) #17
      print('Channel changed to: ' + str(dmList[num])) #17
    except:                                                                ############
      print('Channel was not changed - an error occured, please try again.') ########
    return currentChannel
      

  if mode == 3:
    #print('<<FA3>>')
    #print(currentChannel)
    return currentChannel #client.get_channel(currentChannel)


def reset():
  global currentChannel
  print('---------------------')
  currentChannel = default
  return int(currentChannel)


def listAll():
  global dmList
  print('---------------------')
  return dmList
  


def commands():
  print('--------------------')
  print('For channels: ')
  print('  -l for importing a list (cmd format: (item1), (item2), (item3), etc. Enter default first. System does not have handling for other characters besides commas, so please refrain from using those')
  print('  -s for selecting a channel (from 0 to the highest number in list, 0 being the first one.0')
  print('      (cmd format: -s x (x being your number))')
  print('  -sl to show the list of available channels.')
  print('  -r to reset to default ID, hardcoded into system.')
  print(' ')
  print('for user settings: ')
  print('  + for sending a message (cmd format: + testMsg).')
  print('  = for changing your username (cmd format: "= newUsername).')
  print('  / for sending a message without the tag(cmd format:/ testMsg).')
  print(' ')
  print('Extra features: ')
  print('  ~ quit to end program (if program restarts, enter fq).')
  print('  ~ help to access this menu.')
  print('  ~ export to export image and log data.')
  print("  ~ clear to clear the console of all messages (Can't be undone.).")
  print("  ~ clear-image to clear the image log")
  print("  ~ clear-export to clear the exported data and reset the .json counter (Can't be undone).")
  print('--------------------')

def ccp():
  os.system('clear')

#def delete(mode, id):
#  global deleteLog 
#  if mode == 1: # to set the log to empty, run at the start
#    deleteLog = []
#    print(deleteLog)
#    print('delete log cleared.')
#  if mode == 2: # to add to the log
#    deleteLog.append(id)
#    print(deleteLog)
#    print('appended to log.')
#  if mode == 3: # to delete the most recent and cycle back
#    print(1)
#    deleteLog.remove(deleteLog[len(deleteLog) - 1])
#    print(deleteLog)
#    print('removed most recent')

def downloadImage(url, user):
  global counter
  query_parameters = {"downloadformat": "png"}
  response = requests.get(url, params=query_parameters)
  #print(response.status_code)
  with open("Online Bot/Master/Images/image: " + str(user) + " :" + str(random.randint(0,1000)) + "." + str(counter) + ".png", mode="wb") as file:
    file.write(response.content)
    file.close()
    counter += 1

def clearImage():
  #os.rmdir('Online Bot/Master/Images/')
  #print('directory removed')
  shutil.rmtree('Online Bot/Master/Images/')
  print('image tree removed')
  os.mkdir('Online Bot/Master/Images/')
  print('image tree made')
  print('------')


def export():
  # establishing counter
  counter = 0

  # getting number to make export folder
  with open('Online Bot/Master/data.json', 'r') as file:
    tempNum = json.load(file)
    file.close()

  # making export folder
  print('creating export folder...')
  #exportPath = (f'Online Bot/Master/export/exportPackage{random.randint(0, 1000)}.{random.randint(0,10)}')
  exportPath = f'Online Bot/Master/export/exportPackage{tempNum}'
  os.mkdir(exportPath)
  print(f'dir: {exportPath}')

  # making image folder
  print('creating image folder in export...')
  imagePath = (f'{exportPath}/Images/')
  os.mkdir(imagePath)
  print(f'image dir: {imagePath}')
  print('/creating temp>image.txt')
  f = open(f'{imagePath}/temp.txt', 'w')
  f.write(" ")
  f.close()

  # export text file
  print('/exporting text file into export...')
  f = open('Online Bot/Master/log.txt', 'r')
  temp = f.read()
  f.close()
  with open('Online Bot/Master/data.json', 'r') as file:
    tempNum = json.load(file)
    file.close()
  print(f'-current counter: {tempNum}')
  #print('file contents:')
  #print(temp)
  f = open(f'{exportPath}/exportLog' + str(tempNum) + '.txt', 'w')
  f.write(temp)
  f.close()
  print('/created and wrote to log')
  tempNum += 1
  print(f'-current counter: {tempNum}')
  with open('Online Bot/Master/data.json', 'w') as file:
    json.dump(tempNum, file)
    file.close()
  #print('counter updated')
  
  # exporting all images
  print('/compiling images into export...')
  for imageName in os.listdir('Online Bot/Master/Images/'):
    imageFile = os.path.join('Online Bot/Master/Images/', imageName)
    print(f'transferring image: {imageFile}')
    f = open(f'{imageFile}', 'rb')
    temp = f.read()
    f.close()
    f = open(f'{imagePath}/{imageName}', 'wb')
    f.write(temp)
    f.close()
    print(f'/transferred: {imageFile}')
  print(f'//export done')
  print('-----------------------------------------------------------------------------')

def clearExport():
  shutil.rmtree('Online Bot/Master/export/')
  print('export tree removed')
  os.mkdir('Online Bot/Master/export/')
  print('export tree made')
  print('------')
  print('resseting counter')
  tempNum = 0
  print(f'new counter: {tempNum}')
  with open('Online Bot/Master/data.json', 'w') as file:
    json.dump(tempNum, file)
    file.close()
  print('json reset.')


def lam():
   try:
    guilds = client.get_guild(currentChannel)
    for member in guilds.members:
      print(f'Member: {member}')
   except:
     print('error in lam')

def muter():
  global mute
  mute = True
  print('Mute has been enabled. Messages will not be logged')


def unmuter():
  global mute
  mute = False
  print('Mute has been disabled. Logging has returned to normal.')