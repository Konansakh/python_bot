import logging
import settings
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters # импортируем из папки telegram/ext файл Updater.py и обработчик команд

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def start_bot(update: Updater, context:CallbackContext):
    mytext = """Hello {}
    
    I have only /start command!""".format(update.message.chat.first_name)
    logging.info('User {} press /start'.format(update.message.chat.username))
    update.message.reply_text(mytext)

def chat(update: Updater, context:CallbackContext):
    text = update.message.text
    logging.info(text)
    
    update.message.reply_text(text)

def main():
    updtr = Updater(settings.TOKEN_TELEGRAM) # указываем токен
    
    updtr.dispatcher.add_handler(CommandHandler("start", start_bot)) # по команде start будет вызываться функция start_bot
    updtr.dispatcher.add_handler(MessageHandler(Filters.text, chat)) 
    
    
    updtr.start_polling() # подключаемся к платформе
    updtr.idle()

if __name__ == "__main__":
    logging.info('Bot started')
    main()                      # конструкция для запуска функции main из текущего файла, а не main импорта
    
