#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS, MONGO_DB_URI, OWNER_ID
from strings import get_command
from CilikMusic import app
from CilikMusic.misc import GRUPLIST
from CilikMusic.utils.database import add_gruplist, remove_gruplist



@app.on_message(
    filters.command("addgc", [".", "/"]) & filters.user(OWNER_ID)
)
async def grupadd(client, message: Message):
    if MONGO_DB_URI is None:
        return await message.reply_text(
            "**Karena masalah privasi bot, Anda tidak dapat mengelola pengguna sudo saat menggunakan Database Cilik.\n\n Silakan isi MONGO_DB_URI Anda di vars Anda untuk menggunakan fitur ini**"
        )
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text("**Berikan id Grup Yang ingin ditambahkan di Jamal Project**")
        chat = message.text.split(None, 1)[1]
        if "@" in chat:
            chat = chat.replace("@", "")
        chat = await app.get_chat(chat)
        if chat.id in GRUPLIST:
            return await message.reply_text(
                f"Grup {chat.mention} sudah bergabung di Jamal Project"
            )
        added = await add_gruplist(chat.id)
        if added:
            GRUPLIST.add(chat.id)
            await message.reply_text(f"{chat.mention} Ditambahkan ke Jamal Project.")
        else:
            await message.reply_text("Failed")
        return


@app.on_message(
    filters.command("delgc", [".", "/"]) & filters.user(OWNER_ID)
)
async def grupdel(client, message: Message):
    if MONGO_DB_URI is None:
        return await message.reply_text(
            "**Karena masalah privasi bot, Anda tidak dapat mengelola pengguna sudo saat menggunakan Database Cilik.\n\n Silakan isi MONGO_DB_URI Anda di vars Anda untuk menggunakan fitur ini**"
        )
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text("**Berikan id Grup Yang ingin dihapus di Jamal Project**")
        chat = message.text.split(None, 1)[1]
        if "@" in chat:
            chat = chat.replace("@", "")
        chat = await app.get_chat(chat)
        if chat.id not in GRUPLIST:
            return await message.reply_text("Grup ini Bukan bagian dari Jamal Project")
        removed = await remove_gruplist(chat.id)
        if removed:
            GRUPLIST.remove(chat.id)
            await message.reply_text("Dikeluarkan dari Jamal Project")
            return
        await message.reply_text(f"Sesuatu yang salah terjadi.")
        return


@app.on_message(filters.command("gruplist", [".", "/"]) & filters.user(OWNER_ID)
async def sudoers_list(client, message: Message, _):
    text = _["black_7"]
    j = 0
    for count, chat_id in enumerate(await blacklisted_chats(), 1):
        try:
            title = (await app.get_chat(chat_id)).title
        except Exception:
            title = "Private"
        j = 1
        text += f"**{count}. {title}** [`{chat_id}`]\n"
    if j == 0:
        await message.reply_text(_["black_8"])
    else:
        await message.reply_text(text)
