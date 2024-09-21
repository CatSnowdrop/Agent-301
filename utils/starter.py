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
    if config.LANG == 'RU':
        logger.info(f"Thread {thread} | {account} | Бот будет запущен через {sleep_timer} сек.")
    elif config.LANG == 'UA':
        logger.info(f"Thread {thread} | {account} | Бот буде запущений через {sleep_timer} сек.")
    else:
        logger.info(f"Thread {thread} | {account} | Bot will start in {sleep_timer}s")
    await sleep(sleep_timer)

    attempts = 3
    while attempts:
        try:
            balance, tickets = await agent.login()
            if config.LANG == 'RU':
                logger.success(f"Поток {thread} | {account} | Вход выполнен! | Balance: {balance} | Tickets: {tickets}")
            elif config.LANG == 'UA':
                logger.success(f"Поток {thread} | {account} | Вхід виконано! | Balance: {balance} | Tickets: {tickets}")
            else:
                logger.success(f"Thread {thread} | {account} | Login! | Balance: {balance} | Tickets: {tickets}")
            break
        except Exception as e:
            logger.error(f"Thread {thread} | {account} | Left login attempts: {attempts}, error: {e}")
            await asyncio.sleep(uniform(*config.DELAYS['RELOGIN']))
            attempts -= 1
    else:
        if config.LANG == 'RU':
            logger.error(f"Поток {thread} | {account} | Не удалось войти")
        elif config.LANG == 'UA':
            logger.error(f"Поток {thread} | {account} | Не вдалося увійти")
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
            if config.LANG == 'RU':
                logger.success(f"Поток {thread} | {account} | Сон: {sleep_timer} секунд...")
            elif config.LANG == 'UA':
                logger.success(f"Поток {thread} | {account} | Сон: {sleep_timer} секунд...")
            else:
                logger.success(f"Thread {thread} | {account} | Sleep: {sleep_timer} second...")
            await asyncio.sleep(sleep_timer)

        except ContentTypeError as e:
            if config.LANG == 'RU':
                logger.error(f"Поток {thread} | {account} | Ошибка: {e}")
            elif config.LANG == 'UA':
                logger.error(f"Поток {thread} | {account} | Помилка: {e}")
            else:
                logger.error(f"Thread {thread} | {account} | Error: {e}")
            await asyncio.sleep(120)

        except Exception as e:
            if config.LANG == 'RU':
                logger.error(f"Поток {thread} | {account} | Ошибка: {e}")
            elif config.LANG == 'UA':
                logger.error(f"Поток {thread} | {account} | Помилка: {e}")
            else:
                logger.error(f"Thread {thread} | {account} | Error: {e}")


