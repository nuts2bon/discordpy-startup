#coding:utf-8
from discord.ext import commands
import os
import traceback
#import sys,codecs
import json
import random
#import it
import ikaTools

#sys.stdout = codecs.getwriter("utf-8")(sys.stdout)
bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
ikaT = ikaTools.ikaTools.ikaTools()

#json_open_wp = open('./weapon.json','r')
#weapons=json.load(json_open_wp)
#weapons['section1']['number']

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def ika(ctx):
    await ctx.send('gawashii')
    
@bot.command()
async def rand_buki(ctx):
		await ctx.send(ikaT.getBukiData)


bot.run(token)
