import telebot

BOT_TOKEN = "8849699805:AAE8THcTNwvP5W-A5-_fL_SDtQSl_9qhMJk"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "أهلا! أنا بوتك الجديد شغال ✅")

@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.reply_to(message, f"وصلتني رسالتك: {message.text}")

print("البوت شغال...")
bot.infinity_polling()
