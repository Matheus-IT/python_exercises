from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)


def get_token():
    with open('./bot_token.txt') as f:
        return f.readline()


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text='I\'m a bot, please talk to me!'
    )


def echo(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=update.message.text
    )


def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.it, text=text_caps)


def main():
    token = get_token()

    updater = Updater(token)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    updater.start_polling()

    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    dispatcher.add_handler(echo_handler)

    caps_handler = CommandHandler('caps', caps)
    dispatcher.add_handler(caps_handler)


if __name__ == '__main__':
    main()
