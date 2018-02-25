import Algorithmia
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


updater = Updater(token='secret token over here')
dispatcher = updater.dispatcher
logging.basicConfig(
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            level=logging.INFO
)


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text="I'm BaeMaxx from MTTN")


def echo(bot, update):
    text = update.message.text
    client = Algorithmia.client('simnNaW19xsi/TpeEDdNI5s62e71')
    algo = client.algo('nlp/SentimentAnalysis/1.0.4')
    re = algo.pipe(text)
    sentiment_value = re.result
    if(sentiment_value>2):
        reply = "I think you are in a good mood"
    elif(sentiment_value<2):
        reply = "You are in a bad mood"
    else:
        reply = "Meh"
    bot.send_message(chat_id=update.message.chat_id, text=reply)


start_handler = CommandHandler('start', start)
echo_handler = MessageHandler(Filters.text, echo)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(echo_handler)

updater.start_polling()
