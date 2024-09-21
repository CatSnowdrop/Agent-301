import configparser
import os

import sys
from pprint import pprint
sys.path.append(os.path.realpath("."))
import inquirer


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def input_str_or_int(text, text_error):
    while True:
        try:
            input_str = input(text)
            input_int = int(input_str)
            break
        except ValueError:
            if input_str == '':
                input_int = ''
                break
            print(text_error)
            continue
    return input_str


async def configurator():
    clear()
    questions = [
        inquirer.List(
            "action",
            message="Select languege | Выберите язык | Оберіть мову",
            choices=["English", "Русский", "Українська"]
        ),
    ]
    action_mapping = {
                'English': 'EN',
                'Русский': 'RU',
                'Українська': 'UA'
            }
    answers = inquirer.prompt(questions)
    lang = action_mapping[answers['action']]
    clear()
    if lang == 'RU':
        print('API_ID и API_HASH Telegram можно получить здесь - https://my.telegram.org/auth')
        print('Вы можете указать пустое значение, чтобы использовать API Android (не рекомендуется).')
        text_error = "\nВведённое значение должно быть числом!"
        API_ID = input_str_or_int("Введите свой API_ID: ", text_error)
        API_HASH = str(input("Введите свой API_HASH: "))
        clear()
        REF_LINK = str(input("Введите свою реферальную ссылку (не обязательно): "))
        clear()
        print('Вы можете передать пустое значение, чтобы использовать параметры по умолчанию')
        DELAY_RELOGIN_MIN = input_str_or_int("Введите минимальную задержку после попытки входа в систему (в секундах): ", text_error)
        DELAY_RELOGIN_MAX = input_str_or_int("Введите максимальную задержку после попытки входа в систему (в секундах): ", text_error)
        clear()
        print('Вы можете передать пустое значение, чтобы использовать параметры по умолчанию')
        DELAY_ACCOUNT_MIN = input_str_or_int("Введите минимальную задержку между подключениями к аккаунтам (чем больше аккаунтов, тем больше задержка) (в секундах): ", text_error)
        DELAY_ACCOUNT_MAX = input_str_or_int("Введите максимальную задержку между подключениями к аккаунтам (чем больше аккаунтов, тем больше задержка) (в секундах): ", text_error)
        clear()
        print('Вы можете передать пустое значение, чтобы использовать параметры по умолчанию')
        DELAY_PLAY_WHEEL_MIN = input_str_or_int("Введите минимальную задержку между играми Wheel (в секундах): ", text_error)
        DELAY_PLAY_WHEEL_MAX = input_str_or_int("Введите максимальную задержку между играми Wheel (в секундах): ", text_error)
        clear()
        print('Вы можете передать пустое значение, чтобы использовать параметры по умолчанию')
        DELAY_TASK_COMPLETE_MIN = input_str_or_int("Введите минимальную задержку после выполнения задания (в секундах): ", text_error)
        DELAY_TASK_COMPLETE_MAX = input_str_or_int("Введите максимальную задержку после выполнения задания (в секундах): ", text_error)
        clear()
        print('Вы можете передать пустое значение, чтобы использовать параметры по умолчанию')
        DELAY_GET_TASKS_MIN = input_str_or_int("Введите минимальную задержку после получения списка заданий (в секундах): ", text_error)
        DELAY_GET_TASKS_MAX = input_str_or_int("Введите максимальную задержку после получения списка заданий (в секундах): ", text_error)
        clear()
        print('Вы можете передать пустое значение, чтобы использовать параметры по умолчанию')
        DELAY_RESTARTING_MIN = input_str_or_int("Введите минимальную задержку перед перезапуском (в секундах): ", text_error)
        DELAY_RESTARTING_MAX = input_str_or_int("Введите максимальную задержку перед перезапуском (в секундах): ", text_error)
        clear()
        questions = [
            inquirer.List(
                "action",
                message="Использовать прокси из файла (data/proxi.txt) или прокси, указанный при создании сессии (sessions/accounts.json)?",
                choices=["Прокси из файла", "Прокси, указанный при создании сессии"]
            ),
        ]
        action_mapping = {
                    'Прокси из файла': True,
                    'Прокси, указанный при создании сессии': False,
                }
        answers = inquirer.prompt(questions)
        USE_PROXY_FROM_FILE = action_mapping[answers['action']]
        clear()
        questions = [
            inquirer.List(
                "action",
                message="Выберите тип прокси для сессии telegram:",
                choices=["http", "socks4", "socks5"]
            ),
        ]
        answers = inquirer.prompt(questions)
        PROXY_TYPE_TG = answers['action']
        clear()
        questions = [
            inquirer.List(
                "action",
                message="Выберите тип прокси для запросов:",
                choices=["http", "socks4", "socks5"]
            ),
        ]
        answers = inquirer.prompt(questions)
        PROXY_TYPE_REQUESTS = answers['action']
    elif lang == 'UA':
        print('API_ID та API_HASH Telegram можна отримати тут - https://my.telegram.org/auth')
        print('Ви можете вказати порожнє значення, щоб використовувати API Android (не рекомендується).')
        text_error = "\nВведене значення має бути числом!"
        API_ID = input_str_or_int("Введіть свій API_ID: ", text_error)
        API_HASH = str(input("Введіть свій API_HASH: "))
        clear()
        REF_LINK = str(input("Введіть своє реферальне посилання (не обов'язково): "))
        clear()
        print('Ви можете передати порожнє значення, щоб використовувати параметри за замовчуванням')
        DELAY_RELOGIN_MIN = input_str_or_int("Введіть мінімальну затримку після спроби входу в систему (у секундах): ", text_error)
        DELAY_RELOGIN_MAX = input_str_or_int("Введіть максимальну затримку після спроби входу в систему (у секундах): ", text_error)
        clear()
        print('Ви можете передати порожнє значення, щоб використовувати параметри за замовчуванням')
        DELAY_ACCOUNT_MIN = input_str_or_int("Введіть мінімальну затримку між підключеннями до акаунтів (що більше акаунтів, то більша затримка) (у секундах): ", text_error)
        DELAY_ACCOUNT_MAX = input_str_or_int("Введіть максимальну затримку між підключеннями до акаунтів (що більше акаунтів, то більша затримка) (у секундах): ", text_error)
        clear()
        print('Ви можете передати порожнє значення, щоб використовувати параметри за замовчуванням')
        DELAY_PLAY_WHEEL_MIN = input_str_or_int("Введіть мінімальну затримку між іграми Wheel (у секундах): ", text_error)
        DELAY_PLAY_WHEEL_MAX = input_str_or_int("Введіть максимальну затримку між іграми Wheel (у секундах): ", text_error)
        clear()
        print('Ви можете передати порожнє значення, щоб використовувати параметри за замовчуванням')
        DELAY_TASK_COMPLETE_MIN = input_str_or_int("Введіть мінімальну затримку після виконання завдання (у секундах): ", text_error)
        DELAY_TASK_COMPLETE_MAX = input_str_or_int("Введіть максимальну затримку після виконання завдання (у секундах): ", text_error)
        clear()
        print('Ви можете передати порожнє значення, щоб використовувати параметри за замовчуванням')
        DELAY_GET_TASKS_MIN = input_str_or_int("Введіть мінімальну затримку після отримання списку завдань (у секундах): ", text_error)
        DELAY_GET_TASKS_MAX = input_str_or_int("Введіть максимальну затримку після отримання списку завдань (у секундах): ", text_error)
        clear()
        print('Ви можете передати порожнє значення, щоб використовувати параметри за замовчуванням')
        DELAY_RESTARTING_MIN = input_str_or_int("Введіть мінімальну затримку перед перезапуском (у секундах): ", text_error)
        DELAY_RESTARTING_MAX = input_str_or_int("Введіть максимальну затримку перед перезапуском (у секундах): ", text_error)
        clear()
        questions = [
            inquirer.List(
                "action",
                message="Використовувати проксі з файлу (data/proxi.txt) або проксі, вказаний під час створення сесії (sessions/accounts.json)?",
                choices=["Проксі з файлу", "Проксі, вказаний під час створення сесії"]
            ),
        ]
        action_mapping = {
                    'Проксі з файлу': True,
                    'Проксі, вказаний під час створення сесії': False,
                }
        answers = inquirer.prompt(questions)
        USE_PROXY_FROM_FILE = action_mapping[answers['action']]
        clear()
        questions = [
            inquirer.List(
                "action",
                message="Оберіть тип проксі для сесії telegram:",
                choices=["http", "socks4", "socks5"]
            ),
        ]
        answers = inquirer.prompt(questions)
        PROXY_TYPE_TG = answers['action']
        clear()
        questions = [
            inquirer.List(
                "action",
                message="Оберіть тип проксі для запитів:",
                choices=["http", "socks4", "socks5"]
            ),
        ]
        answers = inquirer.prompt(questions)
        PROXY_TYPE_REQUESTS = answers['action']
    else:
        print('Telegram API_ID and API_HASH can be obtained here - https://my.telegram.org/auth')
        print('You can drop an empty value to use the Android API (not recommended)')
        text_error = "\nThe entered value must be a number!"
        API_ID = input_str_or_int("Enter your API_ID: ", text_error)
        API_HASH = str(input("Enter your API_HASH: "))
        clear()
        REF_LINK = str(input("Enter your referral link (optional): "))
        clear()
        print('You can pass an empty value to use the default parameters')
        DELAY_RELOGIN_MIN = input_str_or_int("Enter the minimum delay after a login attempt (in seconds): ", text_error)
        DELAY_RELOGIN_MAX = input_str_or_int("Enter the maximum delay after a login attempt (in seconds): ", text_error)
        clear()
        print('You can pass an empty value to use the default parameters')
        DELAY_ACCOUNT_MIN = input_str_or_int("Enter the minimum delay between connections to accounts (the more accounts, the longer the delay) (in seconds): ", text_error)
        DELAY_ACCOUNT_MAX = input_str_or_int("Enter the maximum delay between connections to accounts (the more accounts, the longer the delay) (in seconds): ", text_error)
        clear()
        print('You can pass an empty value to use the default parameters')
        DELAY_PLAY_WHEEL_MIN = input_str_or_int("Enter the minimum delay between Wheel games (in seconds): ", text_error)
        DELAY_PLAY_WHEEL_MAX = input_str_or_int("Enter the maximum delay between Wheel games (in seconds): ", text_error)
        clear()
        print('You can pass an empty value to use the default parameters')
        DELAY_TASK_COMPLETE_MIN = input_str_or_int("Enter the minimum delay after the task is completed (in seconds): ", text_error)
        DELAY_TASK_COMPLETE_MAX = input_str_or_int("Enter the maximum delay after the task is completed (in seconds): ", text_error)
        clear()
        print('You can pass an empty value to use the default parameters')
        DELAY_GET_TASKS_MIN = input_str_or_int("Enter the minimum delay after receiving the task list (in seconds): ", text_error)
        DELAY_GET_TASKS_MAX = input_str_or_int("Enter the maximum delay after receiving the task list (in seconds): ", text_error)
        clear()
        print('You can pass an empty value to use the default parameters')
        DELAY_RESTARTING_MIN = input_str_or_int("Enter the minimum delay before restarting (in seconds): ", text_error)
        DELAY_RESTARTING_MAX = input_str_or_int("Enter the maximum delay before restarting (in seconds): ", text_error)


        clear()
        questions = [
            inquirer.List(
                "action",
                message="Use proxy from file (data/proxi.txt) or proxy specified at session creation (sessions/accounts.json)?",
                choices=["Proxy from file", "Proxy specified at session creation"]
            ),
        ]
        action_mapping = {
                    'Proxy from file': True,
                    'Proxy specified at session creation': False,
                }
        answers = inquirer.prompt(questions)
        USE_PROXY_FROM_FILE = action_mapping[answers['action']]
        clear()
        questions = [
            inquirer.List(
                "action",
                message="Select proxy type for telegram session:",
                choices=["http", "socks4", "socks5"]
            ),
        ]
        answers = inquirer.prompt(questions)
        PROXY_TYPE_TG = answers['action']
        clear()
        questions = [
            inquirer.List(
                "action",
                message="Select proxy type for requests:",
                choices=["http", "socks4", "socks5"]
            ),
        ]
        answers = inquirer.prompt(questions)
        PROXY_TYPE_REQUESTS = answers['action']

    config = configparser.ConfigParser()
    config['DEFAULT'] = {
        'LANG': 'EN',
        'API_ID': '6',
        'API_HASH': 'eb06d4abfb49dc3eeb1aeb98ae0f581e',
        'REF_LINK': 'https://t.me/Agent301Bot/app?startapp=onetime352437152',
        'USE_PROXY_FROM_FILE': 'False',
        'PROXY_TYPE_TG': 'socks5',
        'PROXY_TYPE_REQUESTS': 'socks5',
        'DELAY_RELOGIN': '5|7',
        'DELAY_ACCOUNT': '5|15',
        'DELAY_PLAY_WHEEL': '5|20',
        'DELAY_TASK_COMPLETE': '10|15',
        'DELAY_GET_TASKS': '5|10',
        'DELAY_RESTARTING': '21600|43200'
    }
    
    config['Config'] = {
        'LANG': lang,
        'USE_PROXY_FROM_FILE': USE_PROXY_FROM_FILE,
        'PROXY_TYPE_TG': PROXY_TYPE_TG,
        'PROXY_TYPE_REQUESTS': PROXY_TYPE_REQUESTS
    }

    if (API_ID != '' and API_HASH != ''):
        config['Config']['API_ID'] = API_ID
        config['Config']['API_HASH'] = API_HASH
    
    if REF_LINK != '':
        config['Config']['REF_LINK'] = REF_LINK
            
    if DELAY_RELOGIN_MIN != '' and DELAY_RELOGIN_MAX != '' and (int(DELAY_RELOGIN_MIN) <= int(DELAY_RELOGIN_MAX)):
        config['Config']['DELAY_RELOGIN'] = f'{DELAY_RELOGIN_MIN}|{DELAY_RELOGIN_MAX}'

    if DELAY_ACCOUNT_MIN != '' and DELAY_ACCOUNT_MAX != '' and (int(DELAY_ACCOUNT_MIN) < int(DELAY_ACCOUNT_MAX)):
        config['Config']['DELAY_ACCOUNT'] = f'{DELAY_ACCOUNT_MIN}|{DELAY_ACCOUNT_MIN}'

    if DELAY_PLAY_WHEEL_MIN != '' and DELAY_PLAY_WHEEL_MAX != '' and (int(DELAY_PLAY_WHEEL_MIN) < int(DELAY_PLAY_WHEEL_MAX)):
        config['Config']['DELAY_PLAY_WHEEL'] = f'{DELAY_PLAY_WHEEL_MIN}|{DELAY_PLAY_WHEEL_MAX}'

    if DELAY_TASK_COMPLETE_MIN != '' and DELAY_TASK_COMPLETE_MAX != '' and (int(DELAY_TASK_COMPLETE_MIN) < int(DELAY_TASK_COMPLETE_MAX)):
        config['Config']['DELAY_TASK_COMPLETE'] = f'{DELAY_TASK_COMPLETE_MIN}|{DELAY_TASK_COMPLETE_MAX}'

    if DELAY_GET_TASKS_MIN != '' and DELAY_GET_TASKS_MAX != '' and (int(DELAY_GET_TASKS_MIN) < int(DELAY_GET_TASKS_MAX)):
        config['Config']['DELAY_GET_TASKS'] = f'{DELAY_GET_TASKS_MIN}|{DELAY_GET_TASKS_MAX}'

    if DELAY_RESTARTING_MIN != '' and DELAY_RESTARTING_MAX != '' and (int(DELAY_RESTARTING_MIN) < int(DELAY_RESTARTING_MAX)):
        config['Config']['DELAY_RESTARTING'] = f'{DELAY_RESTARTING_MIN}|{DELAY_RESTARTING_MAX}'
    
    

    with open('data/config.ini', 'w') as configfile:
      config.write(configfile)

    clear()

    return True