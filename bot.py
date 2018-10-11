#!/usr/bin/python
# -*- coding: utf-8 -*-
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters)
from telegram import ParseMode

from pytio import Tio, TioRequest
	
def start(bot, update):
    update.message.reply_text("Hi, Use /j, /mathematica, /julia, /nim, /elixir, /rust or /crystal followed with your code to run it.")
	
def j(bot, update, args):
	
    code = " ".join(args)
    request = TioRequest(lang='j', code="")
    request.set_code('echo ' + str(code))
    tio = Tio()
    data = tio.send(request)
    update.message.reply_text("*[J]*\n*Input*: `{}`".format(str(code)) + "\n\n*Output*: \n`{}`".format(data.result), parse_mode=ParseMode.MARKDOWN)
	
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
    
def elixir(bot, update, args):
	
    code = " ".join(args)
    request = TioRequest(lang='elixir', code="")
    request.set_code(str(code))
    tio = Tio()
    data = tio.send(request)
    update.message.reply_text("*[Elixir]*\n*Input*: `{}`".format(str(code)) + "\n\n*Output*: `{}`".format(data.result), parse_mode=ParseMode.MARKDOWN)

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
    if data.error:
    	update.message.reply_text("*[Crystal]*\n*Input*: `{}`".format(str(code)) + "\n\n*Output*: `{}`".format(data.error), parse_mode=ParseMode.MARKDOWN)
    else:
    	update.message.reply_text("*[Crystal]*\n*Input*: `{}`".format(str(code)) + "\n\n*Output*: `{}`".format(data.result), parse_mode=ParseMode.MARKDOWN)
    	
def main():
    updater = Updater('615050736:AAF2_gmzCle8abVSFSsZwz_C2wJrWnm4Cg4')
    dp = updater.dispatcher
    print ('BOT STARTED!')
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('j', j, pass_args=True))
    dp.add_handler(CommandHandler('mathematica', mathematica, pass_args=True))
    dp.add_handler(CommandHandler('julia', julia, pass_args=True))
    dp.add_handler(CommandHandler('nim', nim, pass_args=True))
    dp.add_handler(CommandHandler('rust', rust, pass_args=True))
    dp.add_handler(CommandHandler('elixir', elixir, pass_args=True))
    dp.add_handler(CommandHandler('crystal', crystal, pass_args=True))
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
