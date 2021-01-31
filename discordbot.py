#coding:utf-8
from discord.ext import commands
import os
import traceback
import json
lang  = "ja_JP"
json_open_wp = open('./weapon.json','r')
weapons=json.load(json_open_wp)
#weapons['section1']['number']
bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


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
		await ctx.send(weapons[0]["name"][lang])


bot.run(token)
