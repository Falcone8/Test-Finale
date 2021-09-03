import os

from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from userbot.events import register

TMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY", "./")


@register(pattern=".info(?: |$)(.*)", outgoing=True)
async def who(event):
    if event.fwd_from:
        return
    if not os.path.isdir(TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(TMP_DOWNLOAD_DIRECTORY)
    replied_user = await get_user(event)
    photo, caption = await fetch_info(replied_user, event)
    message_id_to_reply = event.message.reply_to_msg_id
    if not message_id_to_reply:
        message_id_to_reply = None
    try:
        await event.client.send_file(event.chat_id, photo, caption=caption, link_preview=False, force_document=False, reply_to=message_id_to_reply, parse_mode="html")
    except:
        await event.edit("**❌ ERRORE SCONOSCIUTO, RIPROVARE! ❌**")
    if not photo.startswith("http"):
        os.remove(photo)
    await event.delete()

async def get_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        replied_user = await event.client(GetFullUserRequest(previous_message.from_id))
    else:
        user = event.pattern_match.group(1)
        if user.isnumeric():
            user = int(user)
        if not user:
            self_user = await event.client.get_me()
            user = self_user.id
        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user
        try:
            user_object = await event.client.get_entity(user)
            replied_user = await event.client(GetFullUserRequest(user_object.id))
        except:
            await event.edit("**❌ Utente Non Trovato ❌**")
            return None
    return replied_user

async def fetch_info(replied_user, event):
    user_id = replied_user.user.id
    first_name = replied_user.user.first_name
    last_name = replied_user.user.last_name
    common_chat = replied_user.common_chats_count
    username = replied_user.user.username
    user_bio = replied_user.about
    if replied_user.user.bot:
        user_is_bot = "✅"
    else:
        user_is_bot = "❌"
    try:
        photo = await event.client.download_profile_photo(user_id, TMP_DOWNLOAD_DIRECTORY + str(user_id) + ".jpg", download_big=True)
    except:
        photo = "https://thumbs.dreamstime.com/b/no-user-profile-picture-24185395.jpg"
    first_name = first_name.replace("\u2060", "") if first_name else (
        "❌")
    last_name = last_name.replace("\u2060", "") if last_name else (
        "❌")
    username = "@{}".format(username) if username else (
        "❌")
    user_bio = "❌" if not user_bio else "\n" + user_bio
    caption = f"<b>⚙ INFO UTENTE ⚙</b>\n\n<b>👨🏻‍🔧Nome:</b> {first_name}\n<b>🤵🏻Cognome:</b> {last_name}\n<b>🌐Username:</b> {username}\n🆔ID:</b> <code>{user_id}</code>\n<b>🤖Bot:</b> {user_is_bot}\n<b>💬Chat In Comune:</b> {common_chat}\n<b>🔗PermaLink:</b> <a href=\"tg://user?id={user_id}\">{first_name}</a>\n<b>📕Bio:</b> <code>{user_bio}</code>"
    return photo, caption
