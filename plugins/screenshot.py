import asyncio

from pyrogram import filters
from pyrogram.raw import functions
from pyrogram.types import Message

from userge import userge
from userge.misc.help import add_command_help


@userge.on_message(
    filters.command(["screenshot", "ss"], ".") & filters.private & filters.me
)
async def screenshot(_, message: Message):
    await asyncio.gather(
        message.delete(),
        userge.send(
            functions.messages.SendScreenshotNotification(
                peer=await userge.resolve_peer(message.chat.id),
                reply_to_msg_id=0,
                random_id=userge.rnd_id(),
            )
        ),
    )


# Command help section
add_command_help(
    "screenshot",
    [
        [
            ".screenshot",
            "Send a notification in a private chat (not secret) to annoy or troll your friends.",
        ],
    ],
)
