# A.V Cleaning CY — Telegram Bot (FINAL)
Готовый к деплою на Render.

## Запуск локально
1) Python 3.10+
2) `pip install -r requirements.txt`
3) Создайте файл `.env` с содержимым:
```
BOT_TOKEN=ваш_токен_из_BotFather
# Необязательно, адрес сервиса для keep-alive
RENDER_PING_URL=https://av-cleaning-bot.onrender.com
```
4) `python bot.py`

## Деплой на Render
- Build Command: `pip install -r requirements.txt`
- Start Command: `python bot.py`
- Env Vars:
  - `BOT_TOKEN` = ваш токен
  - (опц.) `RENDER_PING_URL` = URL сервиса
