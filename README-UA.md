# Agent 301

[![Static Badge](https://img.shields.io/badge/Telegram-BOT-Link?style=for-the-badge&logo=Telegram&logoColor=white&logoSize=auto&color=blue)](https://t.me/Agent301Bot/app?startapp=onetime352437152)

[![Static Badge](https://img.shields.io/badge/My_Telegram-@CatSnowdrop-Link?style=for-the-badge&logo=Telegram&logoColor=white&logoSize=auto&color=blue)](https://t.me/CatSnowdrop)

## Рекомендація перед використанням

# 🔥🔥 Використовуйте PYTHON 3.10 🔥🔥

[![Static Badge](https://img.shields.io/badge/README_in_Ukrainian_available-README_%D0%A3%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D1%81%D1%8C%D0%BA%D0%BE%D1%8E_%D0%BC%D0%BE%D0%B2%D0%BE%D1%8E-blue.svg?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMjAwIiBoZWlnaHQ9IjgwMCI+DQo8cmVjdCB3aWR0aD0iMTIwMCIgaGVpZ2h0PSI4MDAiIGZpbGw9IiMwMDU3QjciLz4NCjxyZWN0IHdpZHRoPSIxMjAwIiBoZWlnaHQ9IjQwMCIgeT0iNDAwIiBmaWxsPSIjRkZENzAwIi8+DQo8L3N2Zz4=)](README-UA.md)
[![Static Badge](https://img.shields.io/badge/README_in_russian_available-README_%D0%BD%D0%B0_%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%BE%D0%BC_%D1%8F%D0%B7%D1%8B%D0%BA%D0%B5-blue?style=for-the-badge)](README-RU.md)


## Функціонал
| Функціонал                                                     | Підтримується |
|----------------------------------------------------------------|:---------:|
| Багатопоточність                                               |     ✅     |
| Прив'язка проксі до сесії                                      |     ✅     |
| Авторегер; гра Wheel, виконання завдань                        |     ✅     |
| Випадковий час сну між акаунтами                               |     ✅     |
| Підтримка pyrogram .session                                    |     ✅     |

## Налаштування
- Усі налаштування, крім чорного списку завдань, здійснюються з меню програми
- Щоб додати завдання до чорного списку, внесіть рядок з його назвою у файл data/BLACKLIST_TASK.txt

## Швидкий старт 📚
Для швидкого встановлення і подальшого запуску - запустіть файл run.bat на Windows

Для швидкого встановлення і подальшого запуску - запустіть файл run.sh на Linux

## Попередні умови
Перш ніж почати, переконайтеся, що у вас встановлено наступне:
- [Python](https://www.python.org/downloads/) **версії 3.10**

## Отримання API ключів
1. Перейдіть на сайт my.telegram.org і увійдіть у систему, використовуючи свій номер телефону.
2. Виберіть "API development tools" і заповніть форму для реєстрації нового додатка.

## Установка
Ви можете завантажити [**Репозиторій**](https://github.com/CatSnowdrop/Agent-301) клонуванням на вашу систему і встановленням необхідних залежностей:
```shell
git clone https://github.com/CatSnowdrop/Agent-301.git
cd Agent-301
```

Потім для автоматичного встановлення введіть:

Windows:
```shell
run.bat
```

Linux:
```shell
run.sh
```


# Linux ручне встановлення
```shell
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 main.py
```

Також для швидкого запуску ви можете використовувати аргументи, наприклад:
```shell
~/Agent-301 >>> python3 main.py --action (1/2)
# Or
~/Agent-301 >>> python3 main.py -a (1/2)

# 1 - Налаштувати софт
# 2 - Створити сесію
# 3 - Запустити софт
```

# Windows ручне встановлення
```shell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

Також для швидкого запуску ви можете використовувати аргументи, наприклад:
```shell
~/Agent-301 >>> python main.py --action (1/2)
# Or
~/Agent-301 >>> python main.py -a (1/2)

# 1 - Налаштувати софт
# 2 - Створити сесію
# 3 - Запустити софт
```
