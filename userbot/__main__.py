from importlib import import_module
import os

from telethon.errors.rpcerrorlist import PhoneNumberInvalidError

from userbot import LOGS, bot
from userbot.modules import ALL_MODULES

INVALID_PH = '\nERROR: Numero di cellulare non valido' \
             '\n  Tip: Ricorda di scrivere col formato internazionale' \
             '\n       Oppure controlla di aver scritto correttamente'

try:
    bot.start()
except PhoneNumberInvalidError:
    print(INVALID_PH)
    exit(1)

for module_name in ALL_MODULES:
    imported_module = import_module("userbot.modules." + module_name)

LOGS.info("UserBot Avviato!")

SEM_TEST = os.environ.get("SEMAPHORE", None)
if SEM_TEST:
    bot.disconnect()
else:
    bot.run_until_disconnected()
