import random
from telebot import TeleBot, types
import config

bot = TeleBot(config.BOT_TOKEN)

help_message = """Hello! Available commands:
- /start - start to work with bot
- /help - write this message to have a look at all available commands for this bot. The bot will send you the same message you see now
- /joke - get random joke
"""

KNOWN_JOKES = [
    "What does a storm cloud wear under his raincoat? Thunderwear.",
    "Name the kind of tree you can hold in your hand? A palm tree!",
    " What is a room with no walls? A mushroom."
]

@bot.message_handler(commands=["joke"])
def send_random_joke(message: types.Message):
    bot.send_message(
        message.chat.id,
        random.choice(KNOWN_JOKES)
    )
@bot.message_handler(commands=["start"])
def handle_command_start(message: types.Message):
    bot.send_message(
        message.chat.id,
        "Welcome! Let's get acquainted",
    )

@bot.message_handler(commands=["help"])
def send_help_message(message: types.Message):
        bot.send_message(
            message.chat.id,
            help_message,
        )


@bot.message_handler()
def echo_message(message: types.Message):
    text = message.text
    if 'hi' in text.lower():
        text = 'Hi, how is life?'
    if 'how are you?' in text.lower():
        text = 'Good actually'
    bot.send_message(
        message.chat.id,
        text,
    )


bot.infinity_polling(skip_pending=True)
