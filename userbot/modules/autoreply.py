import asyncio
from userbot import bot
from userbot import (AFKREASON, COUNT_MSG, ISAFK, LOGGER, LOGGER_GROUP, USERS)
from userbot import (COUNT_PM, HELPER, LOGGER, LOGGER_GROUP, NOTIF_OFF,
                     PM_AUTO_BAN, BRAIN_CHECKER, LASTMSG, LOGS)
from userbot import (LOGGER)
from userbot.events import register
from telethon.tl.functions.account import UpdateProfileRequest
from telethon import events
from telethon.events import StopPropagation
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from telethon.tl.functions.messages import ReportSpamRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon import functions, types
import requests
from telethon.tl.functions.messages import GetAllChatsRequest
from googletrans import Translator
import os
import json

message = ""
exempt = []
mutedList = []
autoNiceText = False
autoReplyPvt = False



@register(outgoing=True, pattern="^[.]creator$")
async def cre(e):
  await e.edit("Userbot creato da: [Raedpi](https://t.me/Raedpi)") #shh lol



@register(outgoing=True, pattern="^.pula$")
async def CARABINIERIIIIIIIIIII(e):
  for i in range(10):
    await asyncio.wait([e.edit("ð´ð´ð´ð´   ðµðµðµðµ\nð´ð´ð´ð´   ðµðµðµðµ\nð´ð´ð´ð´   ðµðµðµðµ\nð´ð´ð´ð´   ðµðµðµðµ")])
    await asyncio.sleep(0.1)
    await asyncio.wait([e.edit("ðµðµðµðµ   ð´ð´ð´ð´\nðµðµðµðµ   ð´ð´ð´ð´\nðµðµðµðµ   ð´ð´ð´ð´\nðµðµðµðµ   ð´ð´ð´ð´")])
    await asyncio.sleep(0.1)
  await asyncio.wait([e.edit("** ð ARRIVA LA PULA ð **")])

@register(outgoing=True, pattern="^.ficca$")
async def ficca(e):
  for i in range(5):
    await asyncio.wait([e.edit("ðð»ðð» OHH")])
    await asyncio.sleep(0.2)
    await asyncio.wait([e.edit("ðð» ðð»OHH SII ")])
    await asyncio.sleep(0.2)
    await asyncio.wait([e.edit("ðð»  ðð»OOOOOOH ")])
    await asyncio.sleep(0.2)
  await asyncio.wait([e.edit("OHH SIII!")])


@register(outgoing=True, pattern="^[.]cb")
async def cb(e):
  bio = e.text.split(" ", 1)[1]
  await bot(UpdateProfileRequest(about=bio))
  await e.edit("**â Bio Impostata Correttamente â**")

@register(outgoing=True, pattern="^[.]help")
async def comandi(e):
	await asyncio.wait([e.edit("[ðComandi Userbot](https://telegra.ph/SkammatoBene-Ubot-Personalizzato-03-10)")])
#BTC
@register(outgoing=True, pattern="^[.]btc$")
async def bitCoinezzss(e):
  await e.edit("**Prezzo: " + str(requests.get("https://blockchain.info/ticker").json()["USD"]["last"]) + " USD**")

@register(outgoing=True, pattern="^[.]btceur$")
async def bitCoinezzss(e):
  await e.edit("**Prezzo: " + str(requests.get("https://blockchain.info/ticker").json()["EUR"]["last"]) + " EUR**")

#CALC
@register(outgoing=True, pattern="^[.]calc ")
async def Calcolozzs(e):
  st = e.text.split(" ")
  if st.__len__() == 4:
    if st[2] == "+":
      r = float(st[1].replace(",", ".")) + float(st[3].replace(",", "."))
      await e.edit(f"**Operazione eseguita: {st[1]} + {st[3]}\nRisultato: {r}**")
    elif st[2] == "-":
      r = float(st[1].replace(",", ".")) - float(st[3].replace(",", "."))
      await e.edit(f"**Operazione eseguita: {st[1]} - {st[3]}\nRisultato: {r}**")
    elif st[2] == "x" or st[2] == "Ã" or st[2] == "*":
      r = float(st[1].replace(",", ".")) * float(st[3].replace(",", "."))
      await e.edit(f"**Operazione eseguita: {st[1]} Ã {st[3]}\nRisultato: {r}**")
    elif st[2] == ":" or st[2] == "/" or st[2] == "Ã·":
      r = float(st[1].replace(",", ".")) / float(st[3].replace(",", "."))
      await e.edit(f"**Operazione eseguita: {st[1]} : {st[3]}\nRisultato: {r}**")
  else:
    await e.edit("**â Errore Di Sintassi â**")

#GROUPLIST & CHANNELLIST
@register(outgoing=True, pattern="^[.]grouplist$")
async def groupList(e):
  chats = await e.client(GetAllChatsRequest([]))
  groups = []
  for i in chats.chats:
    if type(i).__name__ == "Channel":
      if i.megagroup and not i.left:
        groups.append(f"__{i.title}__ - [`{i.id}`]")
    elif type(i).__name__ == "Chat":
      if not i.left and not i.kicked and not i.deactivated:
        groups.append(f"__{i.title}__ - [`{i.id}`]")
  mex = "**LISTA GRUPPI**\n"
  for i in groups:
    mex += f"\n{i}"
  await e.edit(mex)

@register(outgoing=True, pattern="^[.]channelList$")
async def channelList(e):
  chats = await e.client(GetAllChatsRequest([]))
  chann = []
  for i in chats.chats:
    if type(i).__name__ == "Channel":
      if not i.megagroup and not i.left:
        chann.append(f"__{i.title}__ - [`{i.id}`]")
  mex = "**LISTA CANALI**\n"
  for i in chann:
    mex += f"\n{i}"
  await e.edit(mex)

#TRANSLATE
@register(outgoing=True, pattern="^[.]trit")
async def TranslateLOL(e):
  if e.is_reply:
    msg = await e.get_reply_message()
    tr = Translator()
    try:
      await e.edit("**Traduzione:**\n" + (tr.translate(msg.text, dest="it")).text)
    except:
      await e.edit("**â Errore Sconosciuto â**")
  else:
    st = e.text.split(" ", 1)
    if st.__len__() == 2:
      tr = Translator()
      try:
        await e.edit("**Traduzione:**\n" + (tr.translate(st[1], dest="it")).text)
      except:
        await e.edit("**â Errore Sconosciuto â**")
    else:
      await e.edit("**â Specificare il testo da tradurre â**")

@register(outgoing=True, pattern="^[.]tren")
async def TranslateLOL(e):
  if e.is_reply:
    msg = await e.get_reply_message()
    tr = Translator()
    try:
      await e.edit("**Traduzione:**\n" + (tr.translate(msg.text, dest="en")).text)
    except:
      await e.edit("**â Errore Sconosciuto â**")
  else:
    st = e.text.split(" ", 1)
    if st.__len__() == 2:
      tr = Translator()
      try:
        await e.edit("**Traduzione:**\n" + (tr.translate(st[1], dest="en")).text)
      except:
        await e.edit("**â Errore Sconosciuto â**")
    else:
      await e.edit("**â Specificare il testo da tradurre â**")

#PURGE
@register(outgoing=True, pattern="^[.]purge$")
async def Purge(e):
  if e.is_reply:
    chat = await e.get_input_chat()
    msgs = []
    count = 0
    async for msg in e.client.iter_messages(chat, min_id=e.reply_to_msg_id):
      msgs.append(msg)
      count += 1
      msgs.append(e.reply_to_msg_id)
      if len(msgs) == 100:
        await e.client.delete_messages(chat, msgs)
        msgs = []
    if msgs.__len__() > 0:
      await e.client.delete_messages(chat, msgs)
  else:
    await e.edit("**â Rispondere al messaggio dal quale iniziare a eliminare â**")

#Verify
verify = None

@register(outgoing=True, pattern="^[.]verify$")
async def Verify(e):
  global verify
  verify = e
  await e.client.send_message("@SpamBot", "/start")

@register(incoming=True)
async def checkVerify(e):
  global verify
  if verify != None:
    if e.chat_id == 178220800:
      if ":" in e.text:
        st = e.text.split(" ")
        for i in range(st.__len__()):
          if ":" in st[i]:
            fine = st[i - 3] + " " + st[i - 2] + " " + st[i - 1] + " Ore: " +st[i]
            break
        await verify.edit(f"**â Sei limitato fino al {fine} â**")
        verify = None
        await e.client(functions.messages.DeleteHistoryRequest(e.chat_id, 0, False, True))
      else:
        await verify.edit("**â Non sei limitato â**")
        verify = None
        await e.client(functions.messages.DeleteHistoryRequest(e.chat_id, 0, False, True))

#FILTER
if not os.path.exists("storage.json"):
  with open("storage.json", "w+") as f:
    data = {}
    data["filtri"] = []
    data["reply"] = []
    json.dump(data, f)

@register(outgoing=True, pattern="^[.]addfiltro ")
async def setFilter(e):
  with open("storage.json", "r") as f:
    data = json.load(f)
  st = e.text.split(" ", 2)
  if st.__len__() == 3:
    if not "filtri" in data or not st[1] in data["filtri"]:
      data["filtri"].append(st[1])
      data["reply"].append(st[2])
      with open("storage.json", "w+") as f:
        json.dump(data, f)
      await e.edit("**â Filtro Aggiunto â**")
    else:
      await e.edit("**â Filtro giÃ  presente â**")
  else:
    await e.edit("**â Errore Di Sintassi â**")

@register(outgoing=True, pattern="^[.]delfiltro ")
async def unFilter(e):
  filtro = e.text.split(" ")[1]
  with open("storage.json", "r") as f:
    data = json.load(f)
  if "filtri" in data and filtro in data["filtri"]:
    for i in range(data["filtri"].__len__()):
      if data["filtri"][i] == filtro:
        data["reply"].remove(data["reply"][i])
        break
    await e.edit("**ð« Filtro Rimosso ð«**")
    data["filtri"].remove(filtro)
    with open("storage.json", "w+") as f:
      json.dump(data, f)
  else:
    await e.edit("**â Filtro Non Esistente â**")

@register(outgoing=True, pattern="^[.]filtri$")
async def filterList(e):
  with open("storage.json", "r") as f:
    data = json.load(f)
  filtri = "**LISTA FILTRI**__\n"
  if "filtri" in data:
    for i in data["filtri"]:
      filtri += "\n- " + i
  await e.edit(filtri + "__")

@register(outgoing=True)
async def Filter(e):
  with open("storage.json", "r") as f:
    data = json.load(f)
  if "filtri" in data:
    for i in range(data["filtri"].__len__()):
      if e.text.lower() == data["filtri"][i].lower():
        await e.edit(data["reply"][i])
        break

@register(outgoing=True, pattern="^[.]type ")
async def niceText(e):
  split = e.text.split(" ", 1)
  if split.__len__() >= 2:
    text = split[1]
    mex = ""
    for i in range(len(text)):
      if text[i] == " ":
        mex = mex + ' '
      else:
        mex = mex + text[i]
      await asyncio.wait([e.edit("`" + mex + " |`")])
      await asyncio.sleep(0.1)
      await asyncio.wait([e.edit("`" + mex + "  âââ `")])
      await asyncio.sleep(0.1)
      if i == len(e.text) - 1:
        await asyncio.wait([e.edit("`" + e.text + "`")])

#BLOCK & UNBLOCK
blockMessage = "**messaggiobloccato**"

@register(outgoing=True, pattern="^[.]block$")
async def blockUser(e):
  if not (await e.get_sender()).bot:
    global blockMessage
    if e.is_reply:
      reply = await e.get_reply_message()
      await e.delete()
      await e.client.send_message(reply.chat_id, blockMessage, reply_to=reply)
      await e.client(BlockRequest(reply.sender.id))
    else:
      if e.is_private:
        await e.edit(blockMessage)
        await e.client(BlockRequest(e.chat_id))

unblockMessage = "**messaggiosbloccato**"

@register(outgoing=True, pattern="^.unblock$")
async def unblockUser(e):
  if not e.text[0].isalpha():
    if not (await e.get_sender()).bot:
      global unblockMessage
      if e.is_reply:
        reply = await e.get_reply_message()
        await e.delete()
        await e.client.send_message(reply.chat_id, unblockMessage, reply_to=reply)
        await e.client(UnblockRequest(reply.sender.id))
      else:
        if e.is_private:
          await e.edit(unblockMessage)
          await e.client(UnblockRequest(e.chat_id))

#ON & OFF
@register(outgoing=True, pattern="^[.]on$")
async def changeNameON(e):
  global ON
  await bot(UpdateProfileRequest(last_name="[Online]"))
  await e.delete()

@register(outgoing=True, pattern="^[.]off$")
async def changeNameOFF(e):
  global OFF
  await bot(UpdateProfileRequest(last_name="[Offline]"))
  await e.delete()
  
  

@register(outgoing=True, pattern="^.niceText$")
async def setNiceText(e):
  if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
    global autoNiceText
    if autoNiceText:
      autoNiceText = False
      await e.edit("`Animazione Testo Disattivata!`")
    else:
      autoNiceText = True
      await e.edit("`Animazione Testo Attivata!`")


#mute
@register(outgoing=True, pattern="^[.]mute$")
async def setMute(e):
	global SAVES
	if e.is_private and not (await e.get_sender()).bot:
		if e.chat_id in SAVES["mutedList"]:
			SAVES["mutedList"].remove(e.chat_id)
			'(save)'
			await e.edit("**ð Utente Smutato ð**")
		else:
			SAVES["mutedList"].append(e.chat_id)
			'(save)'
			await e.edit("**ð Utente Mutato ð**")
		
@register(incoming=True)
async def muteManager(e):
	global SAVES
	if e.is_private and not (await e.get_sender()).bot and e.chat_id in SAVES["mutedList"]:
		await e.delete()
		
		
if os.path.exists("saves.json"):
	with open("saves.json", "r+") as f:
		SAVES = json.load(f)
else:
	SAVES = {"AFKMode": False, "Approved": [], "mutedList": [], "AFK-Mex": "Puoi customizzare il seguente messaggio con .msgafk", "Block-Mex": "Puoi customizzare il seguente messaggio con .msgblock"}
	with open("saves.json", "w+") as f:
		json.dump(SAVES, f)
	

async def save():
	global SAVES
	with open("saves.json", "w+") as f:
		json.dump(SAVES, f)



inWait = []
	
@register(outgoing=True, pattern="^[.]msgafk")
async def setAFKMex(e):
	global SAVES
	st = e.text.split(" ", 1)
	if st.__len__() == 2:
		SAVES["AFK-Mex"] = st[1]
		'(save)'
		await e.edit("**â Messaggio Impostato Correttamente â**")
	else:
		await e.edit("**â Specificare il messaggio â**")
	

@register(outgoing=True, pattern="^[.]msgblock")
async def setBlockMex(e):
  global SAVES
  st = e.text.split(" ", 1)
  if st.__len__() == 2:
    SAVES["Block-Mex"] = st[1]
    '(save)'
    await e.edit("â Messaggio Impostato Correttamente â")
  else:
    await e.edit("â Specificare il messaggio â")
  



@register(outgoing=True, pattern="^[.]block$")
async def BlockUser(e):
  global SAVES
  if e.is_reply:
    try:
      await e.client(functions.contacts.BlockRequest((await (await e.get_reply_message()).get_sender()).id))
      await e.edit(SAVES["Block-Mex"])
    except:
      await e.edit("â Impossibile bloccare questo utente â")
  elif e.is_private:
    try:
      await e.client(functions.contacts.BlockRequest(e.chat_id))
      await e.edit(SAVES["Block-Mex"])
    except:
      await e.edit("â Impossibile bloccare questo utente â")
  else:
    await e.edit("â Puoi usare questo comando solo rispondendo al messaggio di un utente o scrivendolo in privato ad un utente â")
	

@register(outgoing=True, pattern="^[.]afk$")
async def setAFK(e):
	global SAVES
	if SAVES["AFKMode"]:
		SAVES["AFKMode"] = False
		'(save)'
		await e.edit("**â AFK Mode Disattivata â**")
	else:
		SAVES["AFKMode"] = True
		'(save)'
		await e.edit("**â AFK Mode Attivata â**")
	
@register(outgoing=True, pattern="^[.]approve$")
async def approveUser(e):
	global SAVES
	if e.chat_id in SAVES["Approved"]:
		await e.edit("**â Quest utente Ã¨ giÃ  approvato â**")
	else:
		SAVES["Approved"].append(e.chat_id)
		'(save)'
		await e.edit("**â Utente Approvato â**")
	
@register(outgoing=True, pattern="^[.]disapprove$")
async def disapproveUser(e):
	global SAVES
	if e.chat_id in SAVES["Approved"]:
		SAVES["Approved"].remove(e.chat_id)
		'(save)'
		await e.edit("**â Utente Disapprovato â**")
	else:
		await e.edit("**â Quest utente non Ã¨ approvato â**")
	

@register(incoming=True)
async def doAFK(e): 
	global SAVES, inWait
	if SAVES["AFKMode"] and e.is_private and not (await e.get_sender()).bot and not e.chat_id in SAVES["Approved"]:
		await e.delete()
		if not e.chat_id in inWait: 
			inWait.append(e.chat_id)
			if e.text == None or e.text == "":
				mex = "__MEDIA__"
			else:
				mex = e.text
			await e.respond(SAVES["AFK-Mex"].replace("{msg}", mex))
			await asyncio.sleep(30)
			inWait.remove(e.chat_id)		
		