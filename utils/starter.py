from utils.agent301 import Agent301
from asyncio import sleep
from random import uniform
from data import config
from utils.core import logger
import datetime
from utils.core.telegram import Accounts
import asyncio
from aiohttp.client_exceptions import ContentTypeError


async def start(thread: int, session_name: str, phone_number: str, proxy: [str, None]):
    agent = Agent301(session_name=session_name, phone_number=phone_number, thread=thread, proxy=proxy)
    account = session_name + '.session'

    sleep_timer = round(uniform(*config.DELAYS['ACCOUNT']))
    logger.info(f"Thread {thread} | {account} | Bot will start in {sleep_timer}s")
    await sleep(sleep_timer)

    attempts = 3
    while attempts:
        try:
            balance, tickets = await agent.login() # логин + получение баланса и билетов
            logger.success(f"Thread {thread} | {account} | Login! | Balance: {balance} | Tickets: {tickets}")
            break
        except Exception as e:
            logger.error(f"Thread {thread} | {account} | Left login attempts: {attempts}, error: {e}")
            await asyncio.sleep(uniform(*config.DELAYS['RELOGIN']))
            attempts -= 1
    else:
        logger.error(f"Thread {thread} | {account} | Couldn't login")
        await agent.logout()
        return

    while True:
        try:
            await asyncio.sleep(5)
            if await agent.need_new_login():
                if await agent.login() is None:
                    return

            await agent.game_wheel()
            await sleep(uniform(2, 8))
            
            await agent.tasks()
            await sleep(uniform(2, 8))
            
            sleep_timer = round(uniform(*config.DELAYS['RESTARTING']))
            logger.success(f"Thread {thread} | {account} | Sleep: {sleep_timer} second...")
            await asyncio.sleep(sleep_timer)

        except ContentTypeError as e:
            logger.error(f"Thread {thread} | {account} | Error: {e}")
            await asyncio.sleep(120)

        except Exception as e:
            logger.error(f"Thread {thread} | {account} | Error: {e}")


