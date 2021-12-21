import discord
from discord.ext import commands, tasks
import random
import ast
import asyncio
import time
from datetime import datetime

intents = discord.Intents(messages=True, guilds=True, reactions=True, presences=True, members=True)
Bot = commands.Bot(command_prefix="-", intents=intents)


@Bot.event
async def on_ready():
    print("ben hazırım")




@Bot.event
async def on_message(message):
    await Bot.process_commands(message)
    if message.content.find(" mı ") != -1 or message.content.find(" mi ") != -1 or message.content.find(" mu ") != -1 or message.content.find(" mü ") != -1:
        cumle = message.content
        cumle = cumle.replace("mı","mi ")
        cumle = cumle.replace("mu", "mi ")
        cumle = cumle.replace("mü", "mi ")

        print(cumle)

        liste = cumle.split(" mi")
        liste = liste[0:-1]
        print(liste)
        await message.channel.send(random.choice(liste))


    if message.content.startswith("BİR KAR YAĞAR İNCE İNCE"):
        await message.channel.send("**BİR KAR YAĞAR İNCE İNCE !!!**")
    if message.content.startswith("KOMANDONUN HALİ NİCE"):
        await message.channel.send("**KOMANDONUN HALİ NİCE !!!**")
    if message.content.startswith("BİR OPERASYON VAR BU GECE"):
        await message.channel.send("**BİR OPERASYON VAR BU GECE !!!**")
    if message.content.startswith("HEY PARAŞÜTÇÜ KOMANDO"):
        await message.channel.send("**HEY PARAŞÜTÇÜ KOMANDO !!!**")
    if message.content.startswith("VUR VUR DAĞCI KOMANDO"):
        await message.channel.send("**VUR VUR DAĞCI KOMANDO !!!**")
    if message.content.startswith("AFERİN TAKIM"):
        await message.channel.send("**SAĞOL !!!**")
    if message.content.startswith("AFERİN TAKIM !"):
        await message.channel.send("**SAĞOL SAĞOL SAĞOL !!!**")

    if message.content.startswith("🚬"):
        liste = ["😢", "🥲", "😭", "😥", "😓", "😕", "😶", "😐"]

        await message.channel.send(f"{random.choice(liste)} :smoking:")





@Bot.command()
@commands.has_role(848218868480475156)
async def müşteriler(ctx):
    guild = ctx.message.guild
    tk = guild.get_role(856253273233293372)
    tkm = tk.members

    cümle = ""
    # print(type(tkm)) shows it as "list"
    total = len(tkm)
    for row in tkm:
        a = row.name
        # print(type(a)) # shows "<class 'discord.member.Member'>" x amount of times

        cümle += a + "\n"
    cümle += f"\n\n {total}   Adet Müşteri Bulunmaktadır"
    await ctx.send(cümle)


@Bot.command()
@commands.has_role(848664815160787004)
async def müşteri_sayaç(ctx):
    guild = ctx.message.guild
    tk = guild.get_role(856253273233293372)
    tkm = tk.members
    total = len(tkm)

    embed = discord.Embed(title=f"Sunucuda {total} Adet Müşteri Bulunmakta", colour=discord.Colour.from_rgb(0, 0, 0))
    msg = await ctx.send(embed=embed)

    """
    
    while False:
        await asyncio.sleep(delay=1)
        guild = ctx.message.guild
        tk = guild.get_role(856253273233293372)
        tkm = tk.members
        total = len(tkm)
        saat = datetime.now()
        saat = saat.strftime("%H:%M:%S")
        r = random.randint(0,255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        embed = discord.Embed(title=f"Sunucuda {total} Adet Müşteri Bulunmakta",colour=discord.Colour.from_rgb(r,g,b),description=f"\n\n {saat}")
        await msg.edit(embed=embed)
        
        
        """


@tasks.loop(seconds=1)
async def musteri_sayac():
    channel = Bot.get_channel(857368785224204369)
    msg_id = 857449685262270504

    msg = await channel.fetch_message(msg_id)
    guild = msg.guild

    tk = guild.get_role(856253273233293372)
    tkm = tk.members
    total = len(tkm)
    saat = datetime.now()
    saat = saat.strftime("%H:%M:%S")
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    await Bot.change_presence(activity=discord.Game(name=f"Sunucuda {total} Adet Müşteri Bulunmakta"))

    embed = discord.Embed(title=f"Sunucuda {total} Adet Müşteri Bulunmakta", colour=discord.Colour.from_rgb(r, g, b),
                          description=f"\n\n {saat}")

    await msg.edit(embed=embed)




@Bot.command(aliases=["slm", "Sa", "SA", "sA", "Selam", "SELAM", "selam"])
async def sa(ctx):
    await ctx.send(f"Selam  {ctx.author.mention} ")
@Bot.command()
async def kutla(ctx):
    target = await Bot.fetch_user(784845899972083743)
    await target.send("https://www.youtube.com/watch?v=kOvLkkJc_l0")

@Bot.command(aliases=["Dimi", "DİMİ"])
async def dimi(ctx):
    await ctx.send(f"Evet Kesinlikle Doğru {ctx.author.mention}")



Bot.run("BURAYA DİSCORD BOT TOKENİ GELİR")
