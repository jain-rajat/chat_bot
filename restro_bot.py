from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler)
import time,datetime
import db as db
import email_bot as e
#from flask import Flask

#app=Flask(__name__)

FIRST, TYPING_CHOICE, SECOND,THIRD,DONE,EMAIL = range(6)

No_of_person = [['1', '2','3','4'],
                  ['5','6','7','8'],
                  ['Enter Your own']]
person= ReplyKeyboardMarkup(No_of_person, one_time_keyboard=True)


import bot_message_reply as bt


def start(bot, update,user_data):
	print(bot)
	print(update)
	user_data['id']=update.message.from_user.id
	result=db.insert_user(update.message.from_user.id)
	if result=='Exist':
		bot.sendMessage(update.message.from_user.id,'Hey Welcome back. To see your booking type /details or make a new booking press /book')
	elif result==False:
		bot.sendMessage(update.message.from_user.id,'Something wrong happened! Try again later')
	else:

		bot.sendMessage( update.message.from_user.id,"Welcome to Rajat Waffle's Factory. Press or type '/help' for information")

def helps(bot,update,user_data):
  bot.sendMessage( update.message.from_user.id, "Hi! I am bot Joey. I will help you book a table for you. Type '/book' for Reservation or /details to see your booking")


def get_book(bot,update,user_data):
	result=db.get_entity(update.message.from_user.id)
	if result==False		bot.sendMessage(update.message.from_user.id:
,'Something wrong happened! Try again later')

	
	elif len(result)==0:
		update.message.reply_text('Sorry! No booking found . Please try by pressing /book')
	else:
		for i in range(len(result)):
			date=str(result[i]['date'])
			time=str(result[i]['time'])
			person=str(result[i]['person'])
			update.message.reply_text('Your booking details:  Date:'+date+'  Time:'+time+'   Person:'+person)
		update.message.reply_text('Thats All I have. :)')


def number_choice(bot, update, user_data):
    text = update.message.text
    try:
    	i=int(text)
    	update.message.reply_text('great! Date of your visit?(yyyy-mm-dd)')
    except:
    	update.message.reply_text('invalid number! Try Again')
    	return TYPING_CHOICE


	    

    user_data['person']=i
    return SECOND


def own_choice(bot, update):
	update.message.reply_text('Please enter your input')
	return TYPING_CHOICE



def book(bot, update):
    update.message.reply_text(
        "Hola! Tell me for many people you want to book a table? ",
        reply_markup=person)

    return FIRST

def date_choice(bot,update,user_data):
	date = update.message.text
	current_date=datetime.date.today()

	try:
		valid_date = time.strptime(date, '%Y-%m-%d')
	except:
  		update.message.reply_text('Invalid date! Try Again')
  		return SECOND

	if date<str(current_date):
  		update.message.reply_text('Please Enter future date')
  		return SECOND
	else:
  		update.message.reply_text('Nice! Please enter time in HH:MM format')
  		user_data['date']=date
  		return THIRD

def time_choice(bot,update,user_data):
	time1=update.message.text
	try:
		valid_time=time.strptime(time1,"%H:%M")
	except:
		update.message.reply_text('Invalid Time! Try Again')
		return THIRD
	update.message.reply_text("awesome! type Yes to confirm your booking")                                                                                           
	user_data['time']=time1
	return  DONE
	
def done(bot, update, user_data):
	update.message.reply_text('Great. Please wait while we confirm your order')
	user_data['id']=update.message.from_user.id
	result=db.create_entity(user_data)
	if result:
		update.message.reply_text('Congrats! Booking confirmed press /details to see your booking. Type Email id to recieve email confirmation or \'no\' to end ')
		return EMAIL
		#user_data.clear()
	else:
		update.message.reply_text('Sorry! Some problem while reserving your table. Try again later!')
		user_data.clear()
	return ConversationHandler.END

def end(bot,update,user_data):
	user_data.clear()
	update.message.reply_text('Try Again by pressing /book')
	return CommandHandler.END

def invalid_command(bot,update):
  bot.sendMessage( update.message.from_user.id,'Sorry! I didnt get you. Press /help for more information')

def get_message(bot,update):
	#print('Hi')
	text=update.message.text
	ans=bt.result(text)
	bot.sendMessage(update.message.from_user.id,ans)

def email(bot,update,user_data):
	mail=update.message.text
	reply=e.send_email(mail,user_data)
	bot.sendMessage(update.message.from_user.id,reply)
	return ConversationHandler.END
	
#@app.route('/')
def main():

	TOKEN='479155987:AAFZx-MBYxjRbLlc_dniKdAQjrFACr5Xsuc'
	updater = Updater(TOKEN)
	dispatcher = updater.dispatcher
	print("Bot started")
	start_handler = CommandHandler('start',start,pass_user_data=True)
	help_handler=CommandHandler('help',helps,pass_user_data=True)
	invalid=MessageHandler(Filters.command,invalid_command)
	get_books=CommandHandler('details',get_book,pass_user_data=True)
	message=MessageHandler(Filters.text,get_message)
	conv_handler = ConversationHandler(
	        entry_points=[CommandHandler('book', book)],

	        states={
	            FIRST: [RegexHandler('^(1|2|3|4|5|6|7|8)$',
	                                    number_choice,
	                                    pass_user_data=True),
	                       RegexHandler('^Enter Your own$',
	                                    own_choice),
	                       ],

	            TYPING_CHOICE: [MessageHandler(Filters.text,
	                                           number_choice,
	                                           pass_user_data=True),
	                            ],

	            SECOND: [MessageHandler(Filters.text,
	                                    date_choice,pass_user_data=True),
	                           ],

	            THIRD: [MessageHandler(Filters.text,
	                                    time_choice,pass_user_data=True),
	                           ]
	                      ,
	            DONE: [RegexHandler('^(YES|yes|Yes)$',
	                                    done,
	                                    pass_user_data=True),
	                       RegexHandler('^(No|NO|no)$',
	                                    end,pass_user_data=True),
	                       ],
	            EMAIL: [RegexHandler('^(No|NO|no)$',
	                                    end,pass_user_data=True),

	            		MessageHandler(Filters.text,
	                                    email,
	                                    pass_user_data=True),
	                    
	                       ],
	        },

        fallbacks=[MessageHandler(Filters.text,
	                                    end,pass_user_data=True)]
    )

	dispatcher.add_handler(start_handler)
	dispatcher.add_handler(help_handler)
	dispatcher.add_handler(conv_handler)
	dispatcher.add_handler(get_books)
	dispatcher.add_handler(message)
	dispatcher.add_handler(invalid)
	print(updater)
	print(dispatcher)
	updater.start_polling()

	updater.idle()

if __name__ == '__main__':
  main()