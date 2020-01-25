from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
from telegram import ChatAction
from functools import wraps
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def send_action(action):
    """Sends `action` while processing func command."""

    def decorator(func):
        @wraps(func)
        def command_func(*args, **kwargs):
            bot, update = args
            bot.send_chat_action(chat_id=update.effective_message.chat_id, action=action)
            return func(bot, update, **kwargs)

        return command_func

    return decorator


with open('token.txt', 'r') as f:
    token = f.readline()

updater = Updater(token=token)
dispatcher = updater.dispatcher


@send_action(ChatAction.TYPING)
def start_command(bot, update):
    keyboard = [[InlineKeyboardButton("Option 1", callback_data='1'),
                 InlineKeyboardButton("Option 2", callback_data='2')],
                [InlineKeyboardButton("Option 3", callback_data='3')]]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Please choose:', reply_markup=reply_markup)


def button(bot, update):
    query = update.callback_query
    print(query)
    query.edit_message_text(text="Selected option: {}".format(query.data))


@send_action(ChatAction.TYPING)
def text_message(bot, update):
    response = 'Получил Ваше сообщение: ' + update.message.text
    bot.send_message(chat_id=update.message.chat_id, text=response)


def main():
    start_command_handler = CommandHandler('start', start_command)
    button_handler = CallbackQueryHandler(button)
    text_message_handler = MessageHandler(Filters.text, text_message)

    dispatcher.add_handler(start_command_handler)
    dispatcher.add_handler(button_handler)
    dispatcher.add_handler(text_message_handler)

    updater.start_polling(clean=True)

    updater.idle()


if __name__ == '__main__':
    main()