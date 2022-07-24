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
async def add_gruplist(client, message: Message):
    if len(message.command) != 2:
        return await message.reply_text(_["black_1"])
    chat_id = int(message.text.strip().split()[1])
    if chat_id in await add_gruplist():
        return await message.reply_text(_["black_2"])
    gruplisted = await add_gruplist(chat_id)
    if gruplisted:
        await message.reply_text(_["black_3"])
    else:
        await message.reply_text("Sesuatu yang salah terjadi.")

                
@app.on_message(filters.command("delgc", [".", "/"]) & filters.user(OWNER_ID)
async def remove_gruplist(client, message: Message):
    if len(message.command) != 2:
        return await message.reply_text(_["black_4"])
    chat_id = int(message.text.strip().split()[1])
    if chat_id not in await add_gruplist():
        return await message.reply_text(_["black_5"])
    nogruplisted = await remove_gruplist(chat_id)
    if nogruplisted:
        return await message.reply_text(_["black_6"])
    await message.reply_text("Sesuatu yang salah terjadi.")


@app.on_message(filters.command("gruplist", [".", "/"]) & filters.user(OWNER_ID)
async def all_gruplist(client, message: Message):
    text = _["black_7"]
    j = 0
    for count, chat_id in enumerate(await gruplist_db(), 1):
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
