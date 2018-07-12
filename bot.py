#!/usr/bin/python
# -*- coding: utf-8 -*-
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters)
from telegram import ParseMode

from pytio import Tio, TioRequest
	
def start(bot, update):
    update.message.reply_text("Hi, By default this bot is for J, use /j, /mathematica, /julia, /nim, /rust or /crystal followed with your code to run it.")

def run(bot, update):
	request = TioRequest(lang='j', code="")
	request.set_code('echo ' + str(update.message.text))
	tio = Tio()
	data = tio.send(request)
	update.message.reply_text("*Input*: `{}`".format(str(update.message.text)) + "\n*Output*: `{}`".format(data.result))
	
def j(bot, update, args):
	
    code = " ".join(args)
    request = TioRequest(lang='j', code="")
    request.set_code('echo ' + str(code))
    tio = Tio()
    data = tio.send(request)
    update.message.reply_text("*Input*: `{}`".format(str(code)) + "\n\n*Output*: `{}`".format(data.result), parse_mode=ParseMode.MARKDOWN)
	
def mathematica(bot, update, args):
	
    code = " ".join(args)
    request = TioRequest(lang='mathematica', code="")
    request.set_code(str(code))
    tio = Tio()
    data = tio.send(request)
    update.message.reply_text("*[Mathematica]*\n*Input*: `{}`".format(str(code)) + "\n\n*Output*: `{}`".format(data.result), parse_mode=ParseMode.MARKDOWN)
    
def julia(bot, update, args):
	
    code = " ".join(args)
    request = TioRequest(lang='julia6', code="")
    request.set_code(str(code))
    tio = Tio()
    data = tio.send(request)
    update.message.reply_text("*[Julia]*\n*Input*: `{}`".format(str(code)) + "\n\n*Output*: `{}`".format(data.result), parse_mode=ParseMode.MARKDOWN)
    
def nim(bot, update, args):
	
    code = " ".join(args)
    request = TioRequest(lang='nim', code="")
    request.set_code(str(code))
    tio = Tio()
    data = tio.send(request)
    update.message.reply_text("*[Nim]*\n*Input*: `{}`".format(str(code)) + "\n\n*Output*: `{}`".format(data.result), parse_mode=ParseMode.MARKDOWN)
    
def rust(bot, update, args):
	
    code = " ".join(args)
    request = TioRequest(lang='rust', code="")
    request.set_code(str(code))
    tio = Tio()
    data = tio.send(request)
    update.message.reply_text("*[Rust]*\n*Input*: `{}`".format(str(code)) + "\n\n*Output*: `{}`".format(data.result), parse_mode=ParseMode.MARKDOWN)
    
def crystal(bot, update, args):
	
    code = " ".join(args)
    request = TioRequest(lang='crystal', code="")
    request.set_code(str(code))
    tio = Tio()
    data = tio.send(request)
    update.message.reply_text("*[Crystal]*\n*Input*: `{}`".format(str(code)) + "\n\n*Output*: `{}`".format(data.result), parse_mode=ParseMode.MARKDOWN)

def main():
    updater = Updater('TOKEN')
    dp = updater.dispatcher
    print ('BOT STARTED!')
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text, run))
    dp.add_handler(CommandHandler('j', j, pass_args=True))
    dp.add_handler(CommandHandler('mathematica', mathematica, pass_args=True))
    dp.add_handler(CommandHandler('julia', julia, pass_args=True))
    dp.add_handler(CommandHandler('nim', nim, pass_args=True))
    dp.add_handler(CommandHandler('rust', rust, pass_args=True))
    dp.add_handler(CommandHandler('crystal', crystal, pass_args=True))
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
