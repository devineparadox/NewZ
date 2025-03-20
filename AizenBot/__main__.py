import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from AizenBot import LOGGER, app, userbot
from AizenBot.core.call import Aizen
from AizenBot.misc import sudo
from AizenBot.plugins import ALL_MODULES
from AizenBot.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Fill String session.")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("AizenBot.plugins" + all_module)
    LOGGER("AizenBot.plugins").info("programs installed.")
    await userbot.start()
    await Aizen.start()
    try:
        await Aizen.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("AizenBot").error(
            "Turn On video chat of Log Channel/Gc"
        )
        exit()
    except:
        pass
    await Aizen.decorators()
    LOGGER("AizenBot").info(
        "Powered by @devine_network"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("AizenBot").info("Bot Stopped.")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
