#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters)
from telegram import ParseMode
import logging
from pytio import Tio, TioRequest

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def start(update, context):
	update.message.reply_text("Hi, Use /j, /red, /mathematica, /nim or /crystal followed with your code to run it.")

def run(update, context):
	text = update.message.text
	if text.startswith('/'):
		command = text.split(' ')[0]
		lang = command[1:]
		if lang not in ['crystal', 'nim', 'j', 'mathematica', 'red']:
			return
	code = text[len(command):]
	request = TioRequest(lang=lang, code="")
	if lang == 'j':
		set_code = 'echo' + code
	else:
		set_code = code
	request.set_code(set_code)
	tio = Tio()
	data = tio.send(request)
	if data.error:
		output = data.error
	else:
		output = data.result
	update.message.reply_text("*[{}]*\n*Input*: `{}`".format(lang.upper(), str(code)) + "\n\n*Output*: `{}`".format(output), parse_mode=ParseMode.MARKDOWN)
		
def main():
	try:
		TOKEN = sys.argv[1]
	except IndexError:
		TOKEN = os.environ.get("TOKEN")
	updater = Updater(TOKEN, use_context=True)
	dp = updater.dispatcher
	dp = updater.dispatcher
	print("Ready to rock..!")
	dp.add_handler(CommandHandler('start', start))
	dp.add_handler(MessageHandler(Filters.text, run))
	
	updater.start_polling()
	updater.idle()

if __name__ == '__main__':
	main()
