from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters
print('PIZDA')
#import logging
#import urllib3
#logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                     level=logging.INFO)

tg_token = '842308578:AAHu6MUSeIsfFOhOVJ6R9QsYxcN1so7qLM4'


def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Привет, мешок! День сегодня говно и ты тоже, но тут когда-нибудь можно будет взять кофе. Здоровайся со мной епта!")

def hi(update, context):
    current_user = update.effective_user
    if (update.message.text == 'привет'or update.message.text == 'Привет' 
    	or update.message.text =='Здравствуй' or update.message.text =='Здравствуйте'):
        context.bot.send_message(chat_id=current_user.id, 
        	text='Отлично. Наверное, тут стоит ебануть меню или картинку с меню, чтобы типа можно было выбрать')
    else:
        context.bot.send_message(chat_id=current_user.id, 
        	text='Поздоровайся говорю, а не хуйню пиши, здоровайся это привет, здравствуйте')

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


if __name__ == '__main__':
    main()
