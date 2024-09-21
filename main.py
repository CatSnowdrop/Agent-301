from utils.core.telegram import Accounts
from utils.starter import start
from utils.configurator import configurator
import asyncio
from data import config
from itertools import zip_longest
from utils.core import get_all_lines
import os
import argparse

import sys
from pprint import pprint
sys.path.append(os.path.realpath("."))
import inquirer

start_text = """
    _                    _     _____  ___  _ 
   / \   __ _  ___ _ __ | |_  |___ / / _ \/ |
  / _ \ / _` |/ _ \ '_ \| __|   |_ \| | | | |
 / ___ \ (_| |  __/ | | | |_   ___) | |_| | |
/_/   \_\__, |\___|_| |_|\__| |____/ \___/|_|
        |___/                                

Soft's author: https://t.me/CatSnowdrop
"""

async def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        parser = argparse.ArgumentParser()
        parser.add_argument('-a', '--action', type=int, help='Action to perform')
        action = parser.parse_args().action

        print(start_text)
        
        if not action:
            if config.LANG == 'RU':
                questions = [
                    inquirer.List(
                        "action",
                        message="Какое действие вы хотите выполнить?",
                        choices=["Настроить софт", "Создать сессию", "Запустить софт"],
                    ),
                ]
                action_mapping = {
                    'Настроить софт': 1,
                    'Создать сессию': 2,
                    'Запустить софт': 3
                }
            elif config.LANG == 'UA':
                questions = [
                    inquirer.List(
                        "action",
                        message="Яку дію ви хочете виконати?",
                        choices=["Налаштувати софт", "Створити сесію", "Запустити софт"],
                    ),
                ]
                action_mapping = {
                    'Налаштувати софт': 1,
                    'Створити сесію': 2,
                    'Запустити софт': 3
                }
            else:
                questions = [
                    inquirer.List(
                        "action",
                        message="What do you want to do?",
                        choices=["Config soft", "Create sessions", "Start soft"],
                    ),
                ]
                action_mapping = {
                    'Config soft': 1,
                    'Create sessions': 2,
                    'Start soft': 3
                }
            answers = inquirer.prompt(questions)

            action = action_mapping[answers['action']]

        if not os.path.exists('sessions'): os.mkdir('sessions')

        if config.PROXY['USE_PROXY_FROM_FILE']:
            if not os.path.exists(config.PROXY['PROXY_PATH']):
                with open(config.PROXY['PROXY_PATH'], 'w') as f:
                    f.write("")
        else:
            if not os.path.exists('sessions/accounts.json'):
                with open("sessions/accounts.json", 'w') as f:
                    f.write("[]")

        if action == 1:
            await configurator()

        if action == 2:
            await Accounts().create_sessions()

        if action == 3:
            accounts = await Accounts().get_accounts()

            tasks = []

            for thread, account in enumerate(accounts):
                session_name, phone_number, proxy = account.values()
                tasks.append(asyncio.create_task(start(session_name=session_name, phone_number=phone_number, thread=thread, proxy=proxy)))

            await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())