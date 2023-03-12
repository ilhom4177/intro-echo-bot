from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
import os

TOKEN=os.environ.get('TOKEN')

updater = Updater(TOKEN)
dp = updater.dispatcher

count_like = 0
count_dis = 0

def like_and_dislike(update: Update, context: CallbackContext):
    global count_like
    global count_dis
    text = update.message.text
    bot = context.bot
    chat_id = update.message.chat.id
    if text[0] == "👍":
        count_like += 1
    elif text[0] == "👎":
        count_dis += 1
    btn1 = KeyboardButton(text=f"👍 {count_like}")
    btn2 = KeyboardButton(text=f"👎 {count_dis}")
    keyboard = ReplyKeyboardMarkup([[btn1, btn2]], resize_keyboard=True)
    bot.sendMessage(chat_id, "LIKE and DISLIKE", reply_markup=keyboard)

def start(update: Update, context:CallbackContext):
    bot = context.bot
    chat_id = update.message.chat.id
    btn1 = KeyboardButton(text=f"👍 {count_like}")
    btn2 = KeyboardButton(text=f"👎 {count_dis}")
    keyboard = ReplyKeyboardMarkup([[btn1, btn2]], resize_keyboard=True)
    bot.sendMessage(chat_id, "LIKE and DISLIKE", reply_markup=keyboard)


dp.add_handler(CommandHandler('start', start))
dp.add_handler(MessageHandler(Filters.text, like_and_dislike))

updater.start_polling()
updater.idle()