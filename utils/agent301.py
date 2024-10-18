import random
import string
import time
from datetime import datetime

from utils.core import logger
from pyrogram import Client
from pyrogram.raw.functions.messages import RequestAppWebView
from pyrogram.raw.types import InputBotAppShortName
import asyncio
from urllib.parse import unquote, quote
from data import config
import aiohttp
from fake_useragent import UserAgent
from aiohttp_socks import ProxyConnector
from faker import Faker





def retry_async(max_retries=2):
    def decorator(func):
        async def wrapper(*args, **kwargs):
            thread, account = args[0].thread, args[0].account
            retries = 0
            while retries < max_retries:
                try:
                    return await func(*args, **kwargs)
                except Exception as e:
                    retries += 1
                    if config.LANG == 'RU':
                        logger.error(f"Поток {thread} | {account} | Ошибка: {e}. Повторная попытка {retries}/{max_retries}...")
                    elif config.LANG == 'UA':
                        logger.error(f"Поток {thread} | {account} | Помилка: {e}. Повторна спроба {retries}/{max_retries}...")
                    else:
                        logger.error(f"Thread {thread} | {account} | Error: {e}. Retrying {retries}/{max_retries}...")
                    await asyncio.sleep(10)
                    if retries >= max_retries:
                        break
        return wrapper
    return decorator


class Agent301:
    def __init__(self, thread: int, session_name: str, phone_number: str, proxy: [str, None]):
        self.LANG = config.LANG
        self.account = session_name + '.session'
        self.thread = thread
        self.ref_token = '352437152' if random.random() <= 0.3 else config.REF_LINK.split('onetime')[1]
        self.proxy = f"{config.PROXY['TYPE']['REQUESTS']}://{proxy}" if proxy is not None else None
        connector = ProxyConnector.from_url(self.proxy) if proxy else aiohttp.TCPConnector(verify_ssl=False)

        if proxy:
            proxy = {
                "scheme": config.PROXY['TYPE']['TG'],
                "hostname": proxy.split(":")[1].split("@")[1],
                "port": int(proxy.split(":")[2]),
                "username": proxy.split(":")[0],
                "password": proxy.split(":")[1].split("@")[0]
            }
            self.proxy = proxy

        self.client = Client(
            name=session_name,
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            workdir=config.WORKDIR,
            proxy=proxy,
            lang_code='ru'
        )

        headers = {'User-Agent': UserAgent(os='android').random}
        headers["Accept"] = "application/json, text/plain, */*"
        headers["Origin"] = "https://telegram.agent301.org"
        headers["Priority"] = "u=1, i"
        headers["Referer"] = "https://telegram.agent301.org/"
        headers["Sec-Ch-Ua-Mobile"] = "?1"
        headers["Sec-Ch-Ua-Platform"] = "Android"
        headers["Sec-Fetch-Dest"] = "empty"
        headers["Sec-Fetch-Mode"] = "cors"
        headers["Sec-Fetch-Site"] = "same-site"
        self.headers = headers
        
        self.session = aiohttp.ClientSession(headers=headers, trust_env=True, connector=connector,
                                             timeout=aiohttp.ClientTimeout(120))

    async def check_proxy(self, proxy):
        try:
            resp = await self.session.get('https://api.ipify.org?format=json', timeout=aiohttp.ClientTimeout(5))
            ip = (await resp.json()).get('ip')
            logger.info(f"Thread {self.thread} | {self.account} | Proxy IP: {ip}")
        except Exception as error:
            logger.error(f"Thread {self.thread} | Proxy: {proxy} | Error: {error}")

    async def need_new_login(self):
        if (await self.session.post("https://api.agent301.org/getMe")).status == 200:
            return False
        else:
            return True


    async def logout(self):
        await self.session.close()


    async def tasks(self):
        tasks_list = await self.get_tasks()
        await asyncio.sleep(random.uniform(*config.DELAYS['GET_TASKS']))
        
        for task in tasks_list:
            if task['title'] in config.BLACKLIST_TASK: continue
            if task['is_claimed'] == False:
                await self.complete_task(task['type'], task['title'])
                await asyncio.sleep(random.uniform(*config.DELAYS['TASK_COMPLETE']))


    async def complete_task(self, task_type: str, task_name: str):
        json_data = {"type":task_type}
        resp = await self.session.post("https://api.agent301.org/completeTask", json=json_data)
        resp_json = await resp.json()
        
        if resp_json.get('ok') == True and resp_json.get('result').get('is_completed') == True:
            reward = resp_json.get('result').get('reward')
            balance = resp_json.get('result').get('balance')
            if self.LANG == 'RU':
                logger.success(f"Поток {self.thread} | {self.account} | Выполнили задание «{task_name}» и получили {reward} AP | Баланс: {balance} AP")
            elif self.LANG == 'UA':
                logger.success(f"Поток {self.thread} | {self.account} | Виконали завдання «{task_name}» і отримали {reward} AP | Баланс: {balance} AP")
            else:
                logger.success(f"Thread {self.thread} | {self.account} | Completed task «{task_name}» and got {reward} AP | Balance: {balance} AP")
            
            return True
        else:
            if self.LANG == 'RU':
                logger.error(f"Поток {self.thread} | {self.account} | Не удалось выполнить задание «{task_name}»")
            elif self.LANG == 'UA':
                logger.error(f"Поток {self.thread} | {self.account} | Не вдалося виконати завдання «{task_name}»")
            else:
                logger.error(f"Thread {self.thread} | {self.account} | Failed complete task «{task_name}»")
                
            return False

    @retry_async()
    async def get_tasks(self):
        resp = await self.session.post('https://api.agent301.org/getTasks')
        resp_json = await resp.json()
        if resp_json.get('ok') == True:
            if self.LANG == 'RU':
                logger.success(f"Поток {self.thread} | {self.account} | Список полученных заданий")
            elif self.LANG == 'UA':
                logger.success(f"Поток {self.thread} | {self.account} | Список отриманих завдань")
            else:
                logger.success(f"Thread {self.thread} | {self.account} | List of tasks received")
                
            return resp_json.get('result').get('data')
        else:
            if self.LANG == 'RU':
                logger.error(f"Поток {self.thread} | {self.account} | Ошибка при получении списка заданий")
            elif self.LANG == 'UA':
                logger.error(f"Поток {self.thread} | {self.account} | Помилка під час отримання списку завдань")
            else:
                logger.error(f"Thread {self.thread} | {self.account} | Error getting task list")
            return False


    async def game_wheel(self):
        resp = await self.session.post("https://api.agent301.org/getMe")
        resp_json = await resp.json()
        if resp_json.get('ok') == True:
            tickets = resp_json.get('result').get('tickets')
        else:
            if self.LANG == 'RU':
                logger.error(f"Поток {self.thread} | {self.account} | Ошибка при получении информации об учетной записи")
            elif self.LANG == 'UA':
                logger.error(f"Поток {self.thread} | {self.account} | Помилка під час отримання інформації про обліковий запис")
            else:
                logger.error(f"Thread {self.thread} | {self.account} | Error retrieving account information")
            return
        await asyncio.sleep(3)

        resp = await self.session.post("https://api.agent301.org/wheel/load")
        resp_json = await resp.json()
        if resp_json.get('ok') == True:
            resp_json_result = resp_json.get('result')
            timestamp_get_ticket = resp_json_result.get('tasks').get('daily')
            rps = resp_json_result.get('tasks').get('rps')
            await asyncio.sleep(1)

        if datetime.now().timestamp() > timestamp_get_ticket:
            json_data = {"type":"daily"}
            resp = await self.session.post("https://api.agent301.org/wheel/task", json=json_data)
            resp_json = await resp.json()
            if resp_json.get('ok') == True:
                tickets = resp_json.get('result').get('tickets')
                if self.LANG == 'RU':
                    logger.success(f"Поток {self.thread} | {self.account} | Получен ежедневный билет Weel! | Билеты: {tickets}")
                elif self.LANG == 'UA':
                    logger.success(f"Поток {self.thread} | {self.account} | Отримано щоденний квиток Weel! | Квитки: {tickets}")
                else:
                    logger.success(f"Thread {self.thread} | {self.account} | Get Weel daily ticket! | Tickets: {tickets}")
                await asyncio.sleep(5)

        if rps == False:
            json_data = {"type":"rps"}
            resp = await self.session.post("https://api.agent301.org/wheel/task", json=json_data)
            resp_json = await resp.json()
            if resp_json.get('ok') == True:
                tickets = resp_json.get('result').get('tickets')
                if self.LANG == 'RU':
                    logger.success(f"Поток {self.thread} | {self.account} | Задание \"Join Stone Cut\" завершено! | Билеты: {tickets}")
                elif self.LANG == 'UA':
                    logger.success(f"Поток {self.thread} | {self.account} | Завдання \"Join Stone Cut\" завершено! | Квитки: {tickets}")
                else:
                    logger.success(f"Thread {self.thread} | {self.account} | Task \"Join Stone Cut\" completed! | Tickets: {tickets}")
                await asyncio.sleep(5)

        if tickets <= 0:
            return

        while tickets:
            resp = await self.session.post("https://api.agent301.org/wheel/spin")
            resp_json = await resp.json()
            if resp_json.get('ok') == True:
                
                reward_mapping = {
                    'tc4': '4 TON',
                    'c1000': '1000 AP',
                    't1': '1 Ticket',
                    'nt1': '1 NOT',
                    'nt5': '5 NOT',
                    't3': '3 Ticket',
                    'tc1': '0.01 TON',
                    'c10000': '10000 AP'
                }
                reward = resp_json.get('result').get('reward')
                reward = reward_mapping.get(reward)
                
                balance = resp_json.get('result').get('balance')
                toncoin = resp_json.get('result').get('toncoin')/100
                notcoin = resp_json.get('result').get('notcoin')
                tickets = resp_json.get('result').get('tickets')
                if self.LANG == 'RU':
                    logger.success(f"Поток {self.thread} | {self.account} | Игра в Weel! | Вознаграждение: {reward} | Баланс: {balance} AP, {toncoin} TON, {notcoin} NOT | Билеты: {tickets}")
                elif self.LANG == 'UA':
                    logger.success(f"Поток {self.thread} | {self.account} | Гра в Weel! | Винагорода: {reward} | Баланс: {balance} AP, {toncoin} TON, {notcoin} NOT | Квитки: {tickets}")
                else:
                    logger.success(f"Thread {self.thread} | {self.account} | Play Weel game! | Reward: {reward} | Balance: {balance} AP, {toncoin} TON, {notcoin} NOT | Tickets: {tickets}")
            else:
                if self.LANG == 'RU':
                    logger.error(f"Поток {self.thread} | {self.account} | Ошибка игры Weel")
                elif self.LANG == 'UA':
                    logger.error(f"Поток {self.thread} | {self.account} | Помилка гри Weel")
                else:
                    logger.error(f"Thread {self.thread} | {self.account} | Wheel game error")
            await asyncio.sleep(random.uniform(*config.DELAYS['PLAY_WHEEL']))


    async def login(self):
        if self.proxy['hostname']:
            await self.check_proxy(self.proxy)
        self.session.headers.pop('Authorization', None)
        query = await self.get_tg_web_data()

        if query is None:
            if self.LANG == 'RU':
                logger.error(f"Поток {self.thread} | {self.account} | Сессия {self.account} недействительна")
            elif self.LANG == 'UA':
                logger.error(f"Поток {self.thread} | {self.account} | Сесія {self.account} недійсна")
            else:
                logger.error(f"Thread {self.thread} | {self.account} | Session {self.account} invalid")
            await self.logout()
            return None

        while True:
            resp = await self.session.get(f'https://telegram.agent301.org/?tgWebAppStartParam=onetime{self.ref_token}')

            if resp.status == 520:
                if self.LANG == 'RU':
                    logger.warning(f"Поток {self.thread} | {self.account} | Повторная попытка входа...")
                elif self.LANG == 'UA':
                    logger.warning(f"Поток {self.thread} | {self.account} | Повторна спроба входу...")
                else:
                    logger.warning(f"Thread {self.thread} | {self.account} | Relogin...")
                await asyncio.sleep(10)
                continue
            else:
                break
        
        self.session.headers['Authorization'] = query
        json_data = {"referrer_id":int(self.ref_token)}

        while True:
            resp = await self.session.post("https://api.agent301.org/getMe", json=json_data)
            resp_json = await resp.json()
            if resp.status == 520:
                if self.LANG == 'RU':
                    logger.warning(f"Поток {self.thread} | {self.account} | Повторная попытка входа...")
                elif self.LANG == 'UA':
                    logger.warning(f"Поток {self.thread} | {self.account} | Повторна спроба входу...")
                else:
                    logger.warning(f"Thread {self.thread} | {self.account} | Relogin...")
                await asyncio.sleep(10)
                continue
            else:
                break

        if resp_json.get('ok') == True:
            balance = resp_json.get('result').get('balance')
            tickets = resp_json.get('result').get('tickets')
            return balance, tickets
        else:
            if self.LANG == 'RU':
                logger.error(f"Поток {self.thread} | {self.account} | Ошибка при получении информации об учетной записи: {resp_json}")
            elif self.LANG == 'UA':
                logger.error(f"Поток {self.thread} | {self.account} | Помилка при отриманні інформації про обліковий запис: {resp_json}")
            else:
                logger.error(f"Thread {self.thread} | {self.account} | Error retrieving account information: {resp_json}")
            await asyncio.sleep(10)


    async def get_tg_web_data(self):
        try:
            await self.client.connect()
            
            if not (await self.client.get_me()).username:
                while True:
                    username = Faker('en_US').name().replace(" ", "") + '_' + ''.join(random.choices(string.digits, k=random.randint(3, 6)))
                    if await self.client.set_username(username):
                        if self.LANG == 'RU':
                            logger.success(f"Поток {self.thread} | {self.account} | Установка имени пользователя @{username}")
                        elif self.LANG == 'UA':
                            logger.success(f"Поток {self.thread} | {self.account} | Встановлення імені користувача @{username}")
                        else:
                            logger.success(f"Thread {self.thread} | {self.account} | Set username @{username}")
                        break
                await asyncio.sleep(5)

            web_view = await self.client.invoke(RequestAppWebView(
                peer=await self.client.resolve_peer('Agent301Bot'),
                app=InputBotAppShortName(bot_id=await self.client.resolve_peer('Agent301Bot'), short_name="app"),
                platform='android',
                write_allowed=True,
                start_param=f'onetime{self.ref_token}'
            ))
            await self.client.disconnect()
            auth_url = web_view.url

            query = unquote(string=unquote(string=auth_url.split('tgWebAppData=')[1].split('&tgWebAppVersion')[0]))
            return query
        except:
            return None
