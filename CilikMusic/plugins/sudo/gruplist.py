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

from CilikMusic import app
from CilikMusic.misc import OWNER_ID
from CilikMusic.utils.database import (gruplist_db,
                                       add_gruplist,
                                       remove_gruplist)


@app.on_message(filters.command("addgc", [".", "/"]) & filters.user(OWNER_ID)
async def addgruplist(client, message: Message):
    if len(message.command) != 2:
        return await message.reply_text("**Penggunaan:**\n/addgc [CHAT_ID]")
    chat_id = int(message.text.strip().split()[1])
    if chat_id in await add_gruplist():
        return await message.reply_text("Grup ini sudah gabung di **Jamal Project**")
    gruplisted = await add_gruplist(chat_id)
    if gruplisted:
        await message.reply_text("✅ **Succes**\nGrup ini berhasil bergabung di **Jamal Project**")
    else:
        await message.reply_text("Sesuatu yang salah terjadi.")

                
@app.on_message(filters.command("removegc", [".", "/"]) & filters.user(OWNER_ID)
async def removegruplist(client, message: Message):
    if len(message.command) != 2:
        return await message.reply_text("**Penggunaan:**\nremovegc/ [CHAT_ID]")
    chat_id = int(message.text.strip().split()[1])
    if chat_id not in await add_gruplist():
        return await message.reply_text("Grup ini sudah keluar dari **Jamal Project**")
    nogruplisted = await remove_gruplist(chat_id)
    if nogruplisted:
        return await message.reply_text("✅ **Succes**\nGrup ini berhasil dikeluarkan dari **Jamal Project**")
    await message.reply_text("Sesuatu yang salah terjadi.")


@app.on_message(filters.command("gruplist", [".", "/"]) & filters.user(OWNER_ID)
async def allgruplist(client, message: Message):
    text = "**Grup Yang Bergabung di Jamal Project:**\n\n"
    j = 0
    for count, chat_id in enumerate(await gruplist_db(), 1):
        try:
            title = (await app.get_chat(chat_id)).title
        except Exception:
            title = "Private"
        j = 1
        text += f"**{count}. {title}** [`{chat_id}`]\n"
    if j == 0:
        await message.reply_text("**Tidak ada yang bergabung di Jamal project**")
    else:
        await message.reply_text(text)
