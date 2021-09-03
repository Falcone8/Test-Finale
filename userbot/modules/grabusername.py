import os
import asyncio
import json
from telethon.tl.functions.channels import CreateChannelRequest, CheckUsernameRequest, UpdateUsernameRequest
from telethon.tl.types import InputChannel, InputPeerChannel
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.account import UpdateUsernameRequest as UUpdateUsernameRequest
from telethon import functions, types
from userbot.events import register


inWait = []
inGrab = False


@register(outgoing=True, pattern="^[.]grabusername (.+)")
async def grabUsername(e):
  global inGrab
  await e.edit("Il processo di grab è stato avviato! Per stopparlo usa .stopgrab")
  inGrab = True
  createdPrivateChannel = await bot(CreateChannelRequest("BlackList", "BlackList", megagroup=False))
  newChannelID = createdPrivateChannel.dict["chats"][0].dict["id"]
  newChannelAccessHash = createdPrivateChannel.dict["chats"][0].dict["access_hash"]
  desiredPublicUsername = e.text.split(" ", 1)[1].replace("@", "")
  while inGrab:
    try:
      checkUsernameResult = await bot(CheckUsernameRequest(InputPeerChannel(channel_id=newChannelID, access_hash=newChannelAccessHash), desiredPublicUsername))
      if checkUsernameResult:
        publicChannel = await bot(UpdateUsernameRequest(InputPeerChannel(channel_id=newChannelID, access_hash=newChannelAccessHash), desiredPublicUsername))
        inGrab = False
        await e.edit("Grab Riuscito!")
      else:
        await asyncio.sleep(1)
    except:
      await asyncio.sleep(1)
    
  

@register(outgoing=True, pattern="^[.]stopgrab$")
async def stopGrab(e):
  global inGrab
  if inGrab:
    inGrab = False
    await e.edit("Grab Stoppato Correttamente")
  else:
    await e.edit("Grab non in corso!")