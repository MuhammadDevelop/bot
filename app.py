import telebot
bot = telebot.TeleBot("8563036644:AAEG4I5mCwIdBOdIJ1q5ebcsmToFLSNO94w",parse_mode=None)
@bot.message_handler(["start"])
def start(xabar):
    bot.reply_to(xabar,"Assalomu alaykum")
bot.infinity_polling()