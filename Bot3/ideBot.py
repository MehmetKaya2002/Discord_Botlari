import asyncio
import discord
from discord.ext import commands, tasks
import random
import time
from environments import *
from ideBotToken import  *
import os
intents = discord.Intents(messages=True, guilds=True, reactions=True, presences=True, members=True)
Bot = commands.Bot(command_prefix="-", intents=intents)
@Bot.event
async def on_ready():
    print("ben hazırım")
@Bot.event
async def on_message(message):
    await Bot.process_commands(message)
@Bot.command()
@commands.has_role(905747509148786698)
async def kod_yaz(ctx,arg):
    kod = arg
    kod = str(kod)
    file = open("ideBot.py", "r")
    bilgi1 = file.read()
    file.close()

    bilgi1 = bilgi1.split(split_str)
    kaynakkod1 = bilgi1[0]
    kaynakkod2 = split_str

    file = open("ideBot.py","w")
    file.write(kaynakkod1 +"\n"+kod+"\n"+kaynakkod2)
    file.close()


    file =open("ideBot.py","r")
    bilgi = file.read()
    await ctx.send(bilgi)
    cmd_to_run = "python ideBot.py"
    os.system(cmd_to_run)

@Bot.command()
async def komut2(ctx):
    await ctx.send(random.randint(1,10))
Bot.run(token)