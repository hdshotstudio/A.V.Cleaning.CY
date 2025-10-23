# coding: utf-8
import os
import asyncio
import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.constants import ParseMode
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(name)s | %(message)s")
log = logging.getLogger("AVCleaningCY")

WELCOME_TEXT = (
    "👋 Добро пожаловать в <b>AV Cleaning CY</b>!\n"
    "Премиальный клининг на Кипре 🏝\n\n"
    "Выберите действие из меню ниже:"
)

MENU = [
    ["🧽 Записаться"],
    ["📋 Наши услуги", "📞 Связаться"]
]

SERVICES_TEXT = (
    "<b>📋 Наши услуги</b>\n\n"
    "🏠 <b>Генеральная уборка</b> — глубокая очистка всех помещений.\n"
    "🧹 <b>Поддерживающая уборка</b> — регулярная чистота.\n"
    "🏢 <b>Уборка офиса</b> — для бизнеса.\n"
    "🪣 <b>После ремонта</b> — удаление строительной пыли.\n\n"
    "Напишите нам удобные дату/адрес — и менеджер свяжется с вами."
)

CONTACT_TEXT = (
    "📞 Связаться с менеджером:\n"
    "Telegram: @adrian_handsome\n"
    "Instagram: https://instagram.com/av.cleaning.cy"
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    kb = ReplyKeyboardMarkup(MENU, resize_keyboard=True)
    await update.message.reply_text(WELCOME_TEXT, reply_markup=kb, parse_mode=ParseMode.HTML)

async def handle_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (update.message.text or "").strip()
    kb = ReplyKeyboardMarkup(MENU, resize_keyboard=True)
    if text == "📋 Наши услуги":
        await update.message.reply_text(SERVICES_TEXT, parse_mode=ParseMode.HTML, reply_markup=kb)
    elif text == "📞 Связаться":
        await update.message.reply_text(CONTACT_TEXT, parse_mode=ParseMode.HTML, reply_markup=kb)
    elif text == "🧽 Записаться":
        await update.message.reply_text("✍️ Напишите адрес и удобное время — мы ответим в ближайшее время.", reply_markup=kb)
    else:
        await update.message.reply_text("Спасибо! Мы получили ваше сообщение. Напишите /start, чтобы открыть меню.", reply_markup=kb)


async def main():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN не найден. Добавьте переменную окружения BOT_TOKEN в Render или .env")
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_menu))

    log.info("🚀 Бот запущен и готов к работе!")
    # Запускаем бота
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())