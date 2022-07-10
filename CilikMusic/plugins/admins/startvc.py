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
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall
from pyrogram.raw.types import InputPeerChannel
from pyrogram.errors import UserAlreadyParticipant, UserNotParticipant, ChatAdminRequired

from config import BANNED_USERS
from strings import get_command
from CilikMusic import app
from CilikMusic.utils.decorators import AdminRightsCheck
  
# Commands
STARTVC_COMMAND = get_command("STARTVC_COMMAND")
    

@app.on_message(
    filters.command(STARTVC_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminRightsCheck    
async def start_group_call(cli, message: Message,):
    chat_id = message.chat.id
    msg = await cli.send_message(chat_id, "`starting...`")
    try:
        peer = await user.resolve_peer(chat_id)
        await user.send(
            CreateGroupCall(
                peer=InputPeerChannel(
                    channel_id=peer.channel_id,
                    access_hash=peer.access_hash,
                ),
                random_id=user.rnd_id() // 9000000000,
            )
        )
        await msg.edit_text("✅ Group call started !")
    except ChatAdminRequired:
        await msg.edit_text(
            "The userbot is not admin in this chat. To start the Group call you must promote the userbot as admin first with permission:\n\n» ❌ manage_video_chats"
        )    
        
