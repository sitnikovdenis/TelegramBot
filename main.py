import random
from telebot import TeleBot, types

import config
import messages
import jokes

bot = TeleBot(config.BOT_TOKEN)


@bot.message_handler(commands=["joke"])
def send_random_joke(message: types.Message):
    bot.send_message(
        message.chat.id,
        random.choice(jokes.KNOWN_JOKES)
    )
@bot.message_handler(commands=["start"])
def handle_command_start(message: types.Message):
    bot.send_message(
        message.chat.id,
        messages.start_text,
    )

@bot.message_handler(commands=["help"])
def send_help_message(message: types.Message):
        bot.send_message(
            message.chat.id,
            messages.help_text,
        )


@bot.message_handler()
def echo_message(message: types.Message):
    text = message.text
    text_lower = text.lower()
    if 'hi' in text_lower:
        text = 'Hi, how is life?'
    elif 'how are you' in text_lower:
        text = 'Good actually and you?'
    elif "what's up" in text_lower:
        text = "Amazing! Thank, you?"
    elif "bye" in text_lower or "see you" in text_lower:
        text = "See you soon!"
    elif "hello" in text_lower:
        text = "Hello dear"
    bot.send_message(
        message.chat.id,
        text,
    )

if __name__ == "__main__":
    bot.infinity_polling(skip_pending=True)
