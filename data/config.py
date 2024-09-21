#
#   DO NOT CHANGE ANYTHING IN THIS FILE!!!! ALL SETTINGS ARE STORED IN config.ini AND CHANGED FROM SOFTWARE MENU
#
#   В ЭТОМ ФАЙЛЕ НИЧЕГО НЕ МЕНЯТЬ!!! ВСЕ НАСТРОЙКИ ХРАНЯТСЯ В config.ini И МЕНЯЮТСЯ ЧЕРЕЗ МЕНЮ СОФТА
#
#   У ЦЬОМУ ФАЙЛІ НІЧОГО НЕ ЗМІНЮВАТИ!!! УСІ НАЛАШТУВАННЯ ЗБЕРІГАЮТЬСЯ В config.ini І ЗМІНЮЮТЬСЯ ЧЕРЕЗ МЕНЮ СОФТА

import configparser

config = configparser.ConfigParser()
config.sections()

config.read('data/config.ini')

LANG = config['Config']['LANG']

API_ID = int(config['Config']['API_ID'])
API_HASH = config['Config']['API_HASH']

REF_LINK = config['Config']['REF_LINK']

DELAYS = {
    "RELOGIN": list(map(int, config['Config']['DELAY_RELOGIN'].split("|"))),  # delay after a login attempt
    'ACCOUNT': list(map(int, config['Config']['DELAY_ACCOUNT'].split("|"))),  # delay between connections to accounts (the more accounts, the longer the delay)
    'PLAY_WHEEL': list(map(int, config['Config']['DELAY_PLAY_WHEEL'].split("|"))),   # delay between wheel games
    'TASK_COMPLETE': list(map(int, config['Config']['DELAY_TASK_COMPLETE'].split("|"))),  # delay after completed the task
    'GET_TASKS': list(map(int, config['Config']['DELAY_GET_TASKS'].split("|"))),  # delay after receiving list of tasks
    'RESTARTING': list(map(int, config['Config']['DELAY_RESTARTING'].split("|")))  # delay before restart
}

# blacklist tasks
with open('data/BLACKLIST_TASK.txt', 'r') as f:
    BLACKLIST_TASK = f.read().splitlines()

PROXY = {
    "USE_PROXY_FROM_FILE": config['Config'].getboolean('USE_PROXY_FROM_FILE'),  # True - if use proxy from file, False - if use proxy from accounts.json
    "PROXY_PATH": "data/proxy.txt",  # path to file proxy
    "TYPE": {
        "TG": config['Config']['PROXY_TYPE_TG'],  # proxy type for tg client. "socks4", "socks5" and "http" are supported
        "REQUESTS": config['Config']['PROXY_TYPE_REQUESTS']  # proxy type for requests. "http" for https and http proxys, "socks5" for socks5 proxy.
        }
}

# session folder (do not change)
WORKDIR = "sessions/"

# timeout in seconds for checking accounts on valid
TIMEOUT = 30
