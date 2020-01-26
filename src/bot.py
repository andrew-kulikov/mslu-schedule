from functools import wraps

from telegram import ChatAction
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters

from scheduleFileUtils import get_weeks
from processor import load_week_schedule


def send_action(action):
    """Sends `action` while processing func command."""

    def decorator(func):
        @wraps(func)
        def command_func(*args, **kwargs):
            bot, update = args
            bot.send_chat_action(
                chat_id=update.effective_message.chat_id, action=action)
            return func(bot, update, **kwargs)

        return command_func

    return decorator


with open('token.txt', 'r') as f:
    token = f.readline()

updater = Updater(token=token)
dispatcher = updater.dispatcher


@send_action(ChatAction.TYPING)
def start_command(bot, update):
    weeks = get_weeks()

    keyboard = [[InlineKeyboardButton(week, callback_data=week)] for week in weeks]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Please choose:', reply_markup=reply_markup)


@send_action(ChatAction.UPLOAD_PHOTO)
def button(bot, update):
    query = update.callback_query
    week = query.data
    query.edit_message_text(text="Загружаю расписание на неделю {} ...".format(week))
    try:
        loaded_image = load_week_schedule(week)
        bot.send_photo(query.message.chat_id, photo=open(loaded_image, 'rb'))
    except Exception as e:
        bot.send_message(chat_id=query.message.chat_id, text='Расписание на данную неделю недоступно :(')


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
