# api id, hash
API_ID = 123456789
API_HASH = '1a2b3c4d5e6f7g1a2b3c4d5e6f7g'

REF_LINK = 'https://t.me/Agent301Bot/app?startapp=onetime352437152'

DELAYS = {
    "RELOGIN": [5, 7],  # delay after a login attempt
    'ACCOUNT': [5, 15],  # delay between connections to accounts (the more accounts, the longer the delay)
    'PLAY_WHEEL': [10, 20],   # delay between wheel games
    'TASK_COMPLETE': [10, 15],  # delay after completed the task
    'GET_TASKS': [5, 10],  # delay after receiving list of tasks
    'RESTARTING': [21600, 43200]  # delay before restart
}

# blacklist tasks
BLACKLIST_TASK = ['Watch short video', 'Make a transaction', 'Stars purchase', 'Invite 3 friends', 'Boost our channel', 'Earn with JetTon Farming', 'Join TapWarrior']

PROXY = {
    "USE_PROXY_FROM_FILE": False,  # True - if use proxy from file, False - if use proxy from accounts.json
    "PROXY_PATH": "data/proxy.txt",  # path to file proxy
    "TYPE": {
        "TG": "socks5",  # proxy type for tg client. "socks4", "socks5" and "http" are supported
        "REQUESTS": "socks5"  # proxy type for requests. "http" for https and http proxys, "socks5" for socks5 proxy.
        }
}

# session folder (do not change)
WORKDIR = "sessions/"

# timeout in seconds for checking accounts on valid
TIMEOUT = 30
