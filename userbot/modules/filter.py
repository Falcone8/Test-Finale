import os
import json
from userbot.events import register

#FILTER
if not os.path.exists("storage.json"):
  with open("storage.json", "w+") as f:
    data = {}
    data["filtri"] = []
    data["reply"] = []
    json.dump(data, f)
 
@register(outgoing=True, pattern="^[.]filter ")
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
      await e.edit("**✅ Filtro Aggiunto ✅**")
    else:
      await e.edit("**❌ Filtro già presente ❌**")
  else:
    await e.edit("**❌ Errore Di Sintassi ❌**")
 
@register(outgoing=True, pattern="^[.]unfilter ")
async def unFilter(e):
  filtro = e.text.split(" ")[1]
  with open("storage.json", "r") as f:
    data = json.load(f)
  if "filtri" in data and filtro in data["filtri"]:
    for i in range(data["filtri"].__len__()):
      if data["filtri"][i] == filtro:
        data["reply"].remove(data["reply"][i])
        break
    await e.edit("**🚫 Filtro Rimosso 🚫**")
    data["filtri"].remove(filtro)
    with open("storage.json", "w+") as f:
      json.dump(data, f)
  else:
    await e.edit("**❌ Filtro Non Esistente ❌**")
 
@register(outgoing=True, pattern="^[.]filterlist$")
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