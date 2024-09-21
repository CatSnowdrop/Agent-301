# Agent 301

[![Static Badge](https://img.shields.io/badge/Telegram-BOT-Link?style=for-the-badge&logo=Telegram&logoColor=white&logoSize=auto&color=blue)](https://t.me/Agent301Bot/app?startapp=onetime352437152)

[![Static Badge](https://img.shields.io/badge/My_Telegram-@CatSnowdrop-Link?style=for-the-badge&logo=Telegram&logoColor=white&logoSize=auto&color=blue)](https://t.me/CatSnowdrop)

## Рекомендация перед использованием

# 🔥🔥 Используйте PYTHON 3.10 🔥🔥

[![Static Badge](https://img.shields.io/badge/README_in_Ukrainian_available-README_%D0%A3%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D1%81%D1%8C%D0%BA%D0%BE%D1%8E_%D0%BC%D0%BE%D0%B2%D0%BE%D1%8E-blue.svg?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMjAwIiBoZWlnaHQ9IjgwMCI+DQo8cmVjdCB3aWR0aD0iMTIwMCIgaGVpZ2h0PSI4MDAiIGZpbGw9IiMwMDU3QjciLz4NCjxyZWN0IHdpZHRoPSIxMjAwIiBoZWlnaHQ9IjQwMCIgeT0iNDAwIiBmaWxsPSIjRkZENzAwIi8+DQo8L3N2Zz4=)](README-UA.md)
[![Static Badge](https://img.shields.io/badge/README_in_russian_available-README_%D0%BD%D0%B0_%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%BE%D0%BC_%D1%8F%D0%B7%D1%8B%D0%BA%D0%B5-blue?style=for-the-badge)](README-RU.md)


## Функционал
| Функционал                                                     | Поддерживается |
|----------------------------------------------------------------|:---------:|
| Многопоточность                                                |     ✅     |
| Привязка прокси к сессии                                       |     ✅     |
| Авторегер; игра Wheel, выполнение заданий                      |     ✅     |
| Случайное время сна между аккаунтами                           |     ✅     |
| Поддержка pyrogram .session                                    |     ✅     |

## Настройки
- Все настройки, кроме черного списка заданий, производятся из меню программы
- Чтобы добавить задания в черный список внесите строку с его названием в файл data/BLACKLIST_TASK.txt

## Быстрый старт 📚
Для быстрой установки и последующего запуска - запустите файл run.bat на Windows
Для быстрой установки и последующего запуска - запустите файл run.sh на Linux

## Предварительные условия
Прежде чем начать, убедитесь, что у вас установлено следующее:
- [Python](https://www.python.org/downloads/) **версии 3.10**

## Получение API ключей
1. Перейдите на сайт my.telegram.org и войдите в систему, используя свой номер телефона.
2. Выберите "API development tools" и заполните форму для регистрации нового приложения.

## Установка
Вы можете скачать [**Репозиторий**](https://github.com/CatSnowdrop/Agent-301) клонированием на вашу систему и установкой необходимых зависимостей:
```shell
git clone https://github.com/CatSnowdrop/Agent-301.git
cd Agent-301
```

Затем для автоматической установки введите:

Windows:
```shell
run.bat
```

Linux:
```shell
run.sh
```


# Linux ручная установка
```shell
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 main.py
```

Также для быстрого запуска вы можете использовать аргументы, например:
```shell
~/Agent-301 >>> python3 main.py --action (1/2)
# Or
~/Agent-301 >>> python3 main.py -a (1/2)

# 1 - Настроить софт
# 2 - Создать сессию
# 3 - Запустить софт
```

# Windows ручная установка
```shell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

Также для быстрого запуска вы можете использовать аргументы, например:
```shell
~/Agent-301 >>> python main.py --action (1/2)
# Or
~/Agent-301 >>> python main.py -a (1/2)

# 1 - Настроить софт
# 2 - Создать сессию
# 3 - Запустить софт
```
