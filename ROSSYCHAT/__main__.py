import asyncio
import importlib

from pyrogram import idle

from ROSSYCHAT import LOGGER, ROSSYCHAT
from ROSSYCHAT.modules import ALL_MODULES


async def anony_boot():
    try:
        await ROSSYCHAT.start()
    except Exception as ex:
        LOGGER.error(ex)
        quit(1)

    for all_module in ALL_MODULES:
        importlib.import_module("ROSSYCHAT.modules." + all_module)

    LOGGER.info(f"@{ROSSYCHAT.username} Started.")
    await idle()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(anony_boot())
    LOGGER.info("Stopping ROSSYCHAT Bot...")
