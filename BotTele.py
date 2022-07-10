import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Status Login
#Set up the logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s -%(message)s',level=logging.INFO)
logging.info('Starting Bot ...')


def start(update, context):
    message = ('''
        All command Support:
        /start :StartBot
        /help :To Help
        ''')
    update.message.reply_text(message)


def help(update, context):
    update.message.reply_text('Waiting For New Update!!!')


def echo(update, context):
    """Reply User Messenger"""
    update.message.reply_text(update.message.text)


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater("YOUR TOKEN", use_context=True)
    dp = updater.dispatcher
    # Set Command
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    # on noncommand i.e message 
    dp.add_handler(MessageHandler(Filters.text, echo))
    # log all errors
    dp.add_error_handler(error)
    # Start the Bot
    updater.start_polling()
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
