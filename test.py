from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove
print('PIZDA')
#import logging
#import urllib3
#logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                     level=logging.INFO)

tg_token = '842308578:AAHu6MUSeIsfFOhOVJ6R9QsYxcN1so7qLM4'


def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Привет! красивый текст всем добра, пиши хочу кофе")

def hi(update, context):
    current_user = update.effective_user
    #user_markup = ReplyKeyboardMarkup([['1'], ['2']])
    if (update.message.text == 'Хочу кофе'or update.message.text == 'хочу кофе'):
        context.bot.send_message(chat_id=current_user.id, 
            text='Менюха списком')
        context.bot.send_message(chat_id=current_user.id, 
            text='Выбирай', reply_markup=ReplyKeyboardMarkup([['1'], ['2'], ['3'], ['Другое']]))
    elif (update.message.text.isdigit()):
        context.bot.send_message(chat_id=current_user.id, 
             text='Понел', reply_markup=ReplyKeyboardRemove(True))
    else:
        context.bot.send_message(chat_id=current_user.id, 
            text='если не хочешь кофе,111ё то иди нахуй')

def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_user.id, text="Sorry, I didn't understand that command.")

def main():
    update = Updater(token=tg_token, use_context=True)
    dp = update.dispatcher

    start_handler = CommandHandler('start', start)
    dp.add_handler(start_handler)

    hi_handler = MessageHandler(Filters.text, hi)
    dp.add_handler(hi_handler)

    unknown_handler = MessageHandler(Filters.command, unknown)
    dp.add_handler(unknown_handler)

    update.start_polling()
    update.idle()
    #update.stop()


if __name__ == '__main__':
    main()