import telebot


API_key = ""

bot = telebot.Telebot(API_key)


@bot.message_handler(commands=["start"])
def start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup()
    red_button = telebot.types.KeyboardButton("")
    black_button = telebot.types.KeyboardButton("")
    keyboard.row(red_button)
    keyboard.row(black_button)
    bot.send_message(message.chat.id,
    "")