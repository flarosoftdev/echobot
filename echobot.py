import logging
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

TOKEN = "BOT_TOKEN"

logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO)

MAX_MESSAGES = 10
MIN_DELAY = 0.5
delay = 2

async def send_messages(update: Update, context: CallbackContext) -> None:
    args = context.args
    if len(args) < 3:
        await update.message.reply_text("Использование: /send @группа текст кол-во")
        return
    
    chat_username = args[0]
    text = " ".join(args[1:-1])
    try:
        count = int(args[-1])
    except ValueError:
        await update.message.reply_text("Ошибка: Количество сообщений должно быть числом!")
        return
    
    if count > MAX_MESSAGES:
        await update.message.reply_text(f"Ошибка: Количество сообщений не может превышать {MAX_MESSAGES}.")
        return
    
    for i in range(1, count + 1):
        message_text = text
        await context.bot.send_message(chat_id=chat_username, text=message_text)
        await asyncio.sleep(delay)
    
    await update.message.reply_text(f"Отправлено {count} сообщений в {chat_username}.")

async def set_delay(update: Update, context: CallbackContext) -> None:
    global delay
    if len(context.args) != 1:
        await update.message.reply_text("Использование: /setdelay <время_в_секундах>")
        return
    try:
        new_delay = float(context.args[0])
        if new_delay < MIN_DELAY:
            await update.message.reply_text(f"Ошибка: Задержка не может быть меньше {MIN_DELAY} секунд.")
            return
        delay = new_delay
        await update.message.reply_text(f"Задержка установлена на {delay} секунд.")
    except ValueError:
        await update.message.reply_text("Ошибка: Задержка должна быть числом!")

async def send_sticker(update: Update, context: CallbackContext) -> None:
    args = context.args
    if len(args) < 3:
        await update.message.reply_text("Использование: /sticker @группа <URL_или_стикер_id> <количество>")
        return
    
    chat_username = args[0]
    sticker = args[1]
    try:
        count = int(args[2])
    except ValueError:
        await update.message.reply_text("Ошибка: Количество должно быть числом!")
        return
    
    if count > MAX_MESSAGES:
        await update.message.reply_text(f"Ошибка: Количество стикеров не может превышать {MAX_MESSAGES}.")
        return
    
    for i in range(count):
        await context.bot.send_sticker(chat_id=chat_username, sticker=sticker)
        await asyncio.sleep(delay)
    
    await update.message.reply_text(f"Отправлено {count} стикеров в {chat_username}.")

async def send_image(update: Update, context: CallbackContext) -> None:
    args = context.args
    if len(args) < 3:
        await update.message.reply_text("Использование: /image @группа <URL_или_путь_к_изображению> <количество>")
        return
    
    chat_username = args[0]
    image = args[1]
    try:
        count = int(args[2])
    except ValueError:
        await update.message.reply_text("Ошибка: Количество должно быть числом!")
        return
    
    if count > MAX_MESSAGES:
        await update.message.reply_text(f"Ошибка: Количество изображений не может превышать {MAX_MESSAGES}.")
        return
    
    for i in range(count):
        await context.bot.send_photo(chat_id=chat_username, photo=image)
        await asyncio.sleep(delay)
    
    await update.message.reply_text(f"Отправлено {count} изображений в {chat_username}.")

async def send_gif(update: Update, context: CallbackContext) -> None:
    args = context.args
    if len(args) < 3:
        await update.message.reply_text("Использование: /gif @группа <URL_или_путь_к_GIF> <количество>")
        return
    
    chat_username = args[0]
    gif = args[1]
    try:
        count = int(args[2])
    except ValueError:
        await update.message.reply_text("Ошибка: Количество должно быть числом!")
        return
    
    if count > MAX_MESSAGES:
        await update.message.reply_text(f"Ошибка: Количество GIF не может превышать {MAX_MESSAGES}.")
        return
    
    for i in range(count):
        await context.bot.send_animation(chat_id=chat_username, animation=gif)
        await asyncio.sleep(delay)
    
    await update.message.reply_text(f"Отправлено {count} GIF в {chat_username}.")

async def send_video(update: Update, context: CallbackContext) -> None:
    args = context.args
    if len(args) < 3:
        await update.message.reply_text("Использование: /video @группа <URL_или_путь_к_видео> <количество>")
        return
    
    chat_username = args[0]
    video = args[1]
    try:
        count = int(args[2])
    except ValueError:
        await update.message.reply_text("Ошибка: Количество должно быть числом!")
        return
    
    if count > MAX_MESSAGES:
        await update.message.reply_text(f"Ошибка: Количество видео не может превышать {MAX_MESSAGES}.")
        return
    
    for i in range(count):
        await context.bot.send_video(chat_id=chat_username, video=video)
        await asyncio.sleep(delay)
    
    await update.message.reply_text(f"Отправлено {count} видео в {chat_username}.")

async def send_audio(update: Update, context: CallbackContext) -> None:
    args = context.args
    if len(args) < 3:
        await update.message.reply_text("Использование: /audio @группа <URL_или_путь_к_аудио> <количество>")
        return
    
    chat_username = args[0]
    audio = args[1]
    try:
        count = int(args[2])
    except ValueError:
        await update.message.reply_text("Ошибка: Количество должно быть числом!")
        return
    
    if count > MAX_MESSAGES:
        await update.message.reply_text(f"Ошибка: Количество аудио не может превышать {MAX_MESSAGES}.")
        return
    
    for i in range(count):
        await context.bot.send_audio(chat_id=chat_username, audio=audio)
        await asyncio.sleep(delay)
    
    await update.message.reply_text(f"Отправлено {count} аудио в {chat_username}.")

async def sticker_id(update: Update, context: CallbackContext) -> None:
    """Обработчик получения ID стикера."""
    sticker = update.message.sticker
    if not sticker:
        return

    await update.message.reply_text(f"📌 ID вашего стикера: `{sticker.file_id}`", parse_mode="Markdown")

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("👋🏻 *Приветствую!*\n"
                                    "\n- Отправьте /send (@username группы) (текст) (кол-во)\nИспользуйте /setdelay (время в секундах) для установки задержки.\n"
                                    "- Для отправки стикеров, изображений, GIF, видео и аудио используйте команды:\n"
                                    "- /sticker (@username группы) (URL или ID стикера) (кол-во)\n"
                                    "- /image (@username группы) (URL или путь к изображению) (кол-во)\n"
                                    "- /gif (@username группы) (URL или путь к GIF) (кол-во)\n"
                                    "- /video (@username группы) (URL или путь к видео) (кол-во)\n"
                                    "- /audio (@username группы) (URL или путь к аудио) (кол-во)\n"
                                    "- Для того, чтобы узнать ID стикера, просто отправьте его.\n"
                                    "\n❗ Обратите внимание, *бот должен присутствовать в группе*, в которую Вы хотите отправить сообщения, и *группа должна быть супергруппой*.",
                                    parse_mode="Markdown")

def main():
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("send", send_messages))
    app.add_handler(CommandHandler("setdelay", set_delay))
    app.add_handler(CommandHandler("sticker", send_sticker))
    app.add_handler(CommandHandler("image", send_image))
    app.add_handler(CommandHandler("gif", send_gif))
    app.add_handler(CommandHandler("video", send_video))
    app.add_handler(CommandHandler("audio", send_audio))
    app.add_handler(MessageHandler(filters.Sticker.ALL, sticker_id))
    
    app.run_polling()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        raise RuntimeError(f"An error occured during running this script: {e}.")
else:
    raise RuntimeError("Cannot run \"tg_group_flood\" as module.")
