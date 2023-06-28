import telebot, time, re

token = []
bot = telebot.TeleBot(token)

## START COMMAND ##

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Halo! Bot ini menggunakan hosting Pythonanywhere dan dikelola oleh @[]. Jika kamu butuh bantuan segera hubungi pemilik!")

bot.infinity_polling()
