# Agent 301
clicker for [https://t.me/Agent301Bot](t.me/Agent301Bot/app?startapp=onetime352437152)

My telegram: [@CatSnowdrop](https://t.me/CatSnowdrop)

## Functionality
| Functional                                                     | Supported |
|----------------------------------------------------------------|:---------:|
| Multithreading                                                 |     ✅     |
| Binding a proxy to a session                                   |     ✅     |
| Auto-reger; wheel game, complete tasks                         |     ✅     |
| Random sleep time between accounts                             |     ✅     |
| Support pyrogram .session                                      |     ✅     |

## Settings data/config.py
| Setting                      | Description                                                                                    |
|------------------------------|------------------------------------------------------------------------------------------------|
| **API_ID / API_HASH**        | Platform data from which to launch a Telegram session _(stock - Android)_                      |
| **REF_LINK**         	       | Your referral link  _(eg 'https://t.me/Agent301Bot/app?startapp=onetime352437152')_             (with a 30% chance my link will be used) |
| **BLACKLIST_TASK**           | Blacklist tasks  _(eg ['Invite 3 friends', 'Watch short video'])_                              |
| DELAYS                       |                                                                                                |
| **RELOGIN**                  | Delay after unsuccessful login _(eg [5, 7])_                                                   |
| **ACCOUNT**                  | Delay between connections to accounts (the more accounts, the longer the delay) _(eg [5, 15])_ |
| **PLAY_WHEEL**               | Delay between Wheel games _(eg [5, 20])_                                                       |
| **TASK_COMPLETE**            | Delay after completed the task _(eg [10, 15])_                                                 |
| **GET_TASKS**                | Delay after receiving list of tasks _(eg [5, 10])_                                             |
| **RESTARTING**               | Delay before restart _(eg [21600, 43200])_                                                     |
| PROXY                        |                                                                                     |
| **PROXY_TYPES-TG**           | Proxy type for telegram session _(eg 'socks5')_                                                |
| **PROXY_TYPES-REQUESTS**     | Proxy type for requests _(eg 'socks5')_                                                        |
| **WORKDIR**                  | directory with session _(eg "sessions/")_                                                      |
| **TIMEOUT**                  | timeout in seconds for checking accounts on valid _(eg 30)_                                    |
## Requirements
- Python 3.9 (you can install it [here](https://www.python.org/downloads/release/python-390/)) 
- Telegram API_ID and API_HASH (you can get them [here](https://my.telegram.org/auth))

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   
## Usage
1. Run the bot:
   ```bash
   python main.py
   ```
