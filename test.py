#TelegramBot

import telebot

from  pyowm  import  OWM 
from  pyowm.utils  import  config 
from  pyowm.utils  import  timestamps

bot = telebot.TeleBot("1811369651:AAHxVXrHGoMibnp4SYd8u67Y_OtQhyG_uTQ", parse_mode=None)
owm  =  OWM ( '9c559e199dce315bf9ba812eb6e374f5')
mgr = owm.weather_manager()

@bot.message_handler(content_types=['text'])
def send_echo(message):
	observation = mgr.weather_at_place( message.text )
	w = observation.weather
	temp = w.temperature('celsius')["temp"]

	answer = "In " + message.text + " now it's " + w.detailed_status + "\n"
	answer += "Air temperature now " + str(temp) + " degrees.\n\n"
	
	if temp < 10:
		answer += "It's very cold outside, dress in the warmest clothes!)"
	elif temp <20:
		answer += "It's cold outside, put on your jacket!)"
	else:
		answer += "It's warm outside, dress as you want!)"

	bot.send_message( message.chat.id, answer )

bot.polling( none_stop = True )