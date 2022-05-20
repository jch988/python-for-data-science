from telegram.ext import Updater, MessageHandler, Filters
from datetime import datetime
import csv

def get_location(update, context):
	msg = None
	if update.edited_mesaage:
		msg = update.edited_mesaage
	else:
		msg = update.message
	gps = msg.get_location
	sender = msg.from_user.username
	tm = datetime.now().strftime("%H:%M:%S")
	with open(r'/JCH/loc.csv', 'a') as f:
		writer = csv.writer(f)
		writer.writerow([sender, gps.latitude, gps.longitude, tm])
		context.bot.send_message(chat_id=msg.chat_id, text=str(gps))

def main():
	updater = Updater('5318577456:AAEandjiYnXwgDOq5SpBDBB_JB0TnunwVbQ', use_context=True)
	updater.dispatcher.add_handler(MessageHandler(Filters.location, get_location))
	updater.start_polling()
	updater.idle()

if __name__ == '__main__':
	main()


GET THE FOLLOWING ERROR AND IDK WHY
"""
Traceback (most recent call last):
  File "/Users/JCH/Python/Python for Data Science book/ch_9_loc_2.py", line 1, in <module>
    from telegram.ext import Updater, MessageHandler, Filters
ImportError: cannot import name 'Filters' from 'telegram.ext' (/Users/JCH/Python/anaconda3/lib/python3.9/site-packages/telegram/ext/__init__.py)
[Finished in 2.0s with exit code 1]
[cmd: ['python3', '-u', '/Users/JCH/Python/Python for Data Science book/ch_9_loc_2.py']]
[dir: /Users/JCH/Python/Python for Data Science book]
[path: /opt/local/bin:/opt/local/sbin:/Users/JCH/Python/anaconda3/bin:/Users/JCH/Python/anaconda3/condabin:/Library/Frameworks/Python.framework/Versions/3.10/bin:/Library/Frameworks/Python.framework/Versions/3.10/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin]
"""
