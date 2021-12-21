import asyncio
import discord
from discord.ext import commands, tasks
import os
import time
import random
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import os


intents = discord.Intents(messages=True, guilds=True, reactions=True, presences=True, members=True)
Bot = commands.Bot(command_prefix="-", intents=intents)

nehir = "https://i.redd.it/mzrvpt77nmo21.png"

wdAlfabet = ["✌", "👌", "👍", "👎", "☜", "☞", "☝", "☟", "✋", "☺", "😐", "☹", "💣", "☠", "⚐", "🏱", "☼", "💧", "❄", "🕆",
             "✞", "✡", "☪", "✠", "🕈"]


@Bot.event
async def on_ready():
    nehir_adam.start()
    dolar_tl.start()
    # dolar_grafik_canli.start()
    print("ben hazırım3")
    await Bot.change_presence(activity=discord.Game(name="Gıcık Köpekle"))


tarih = datetime.now()
gün = tarih.strftime("%A")

if gün == "Saturday":
    gün = "Cumartesi"
if gün == "Sunday":
    gün = "Pazar"
if gün == "Monday":
    gün = "Pazartesi"
if gün == "Tuesday":
    gün = "Salı"
if gün == "Wednesday":
    gün = "Çarşamba"
if gün == "Thursday":
    gün = "Perşembe"
if gün == "Friday":
    gün = "Cuma"

deneme = ["""mail : meymey010@gmail.com
 password : Iv26kp9yse """]
liste = ["* Tra la la.\n* Adım ne mi?\n* . . . Pek bir önemi yok.",
         "* Tra la la.\n* Teknede dans etmek tehlikeli.\n* Ama iyi bir egzersizdir.",
         "* Tra la la.\n* Tri li li.\n* Tre le le.",
         "* Tra la la.\n* Su bugün epey ıslak.",
         "* Tra la la.\n* Arada bir mola vermeyi\n unutma. . .",
         "* Tra la la.\n* Yaklaşma elleriyle konuşan\n adama. ",
         "* Tra la la.\n* İnsanların evlerinin etrafında\n* sinsi sinsi dolaşma...\n\n* Seni çöp tenekesi\n sanabilirler.",
         "* Tra la la.\n* Sıcak da olsa soğuk da olsa,\n bana güvenebilirsin.",
         "* Tra la la.\n* Hımmm. . .\n\n* Bugün birkaç kat daha\n pantolon giymeliydim.",
         "* Tra la la.\n* Hımmm. . .\n\n* Bugün birkaç milyon kat\n daha pantolon giymeliydim.",
         "* Tra la la.\n* Piyano çın çın şarkısını\n* çalıyor.\n\n* Hımm. . . Çın çın.",
         "* Tra la la.\n* Hum hum hum.  Hum hum hum.\n* Minik bir konser veriyorum.",
         "* Tra la la.\n* Ah,",
         "* Tra la la.\n* ASGORE'un favori bir\n yiyeceği varmış.",
         "* Tra la la.\n* Yaklaşma öbür dünyadan\n gelmiş olana.",
         "* Tra la la.\n* Temmie Köyü. . .\n\n* . . . Karaltılmış fenerli\n yerden hemen önce.",
         "* Tra la la.\n* Palamutların içinde ne var?\n* Bu bir gizem o kadar.",
         "* Tra la la.\n* Asla yeterince\n havuçlu kekin olmaz.\n\n* . . . Ne yazık ki, bu doğru\n değil.",
         "* Tra la la.\n* İnsanlar, canavarlar. . .\n* Çiçekler.",
         "* Tra la la.\n* Bugün sular vahşi.\n* Bu kötü şans demektir. . .",
         "* Tra la la.\n* Bir köpekle ne oyun\n oynanır?\n\n* Bir arkadaşım için soruyorum. . . ",
         "* Tra la la.\n* Neden benimle şarkı\n söylemiyorsun? Tra la la.",
         "* Tra la la.\n* Meleğin gelişi yakın. . .\n* Tra la la",
         "* Tra la la.\n* Uh oh.\n* Birdenbire, tropik hissettim. . . ",
         "* Tra la la.\n* Su bugün epey kuru.",
         f"* Tra la la.\n* Bir yerlerde, {gün}.\n* O yüzden dikkatli ol.",
         "* Tra la la.\n* Örümceklerin favori bir\n  yiyeceği varmış\n\n* Örümcekler.",
         "* Tra la la.\n* Denizden gelen eski\n  şarkıyı duydun mu hiç?.",
         "* Tra la la.\n* Sev sev sev. . .\n* Boyun kozmosun derinliklerine\n  doğru esniyor.\n\n* . . . Sorun etme.",

         ]


@Bot.event
async def on_message(message):
    await Bot.process_commands(message)
    if message.content.startswith("🚬"):
        liste = ["😢", "🥲", "😭", "😥", "😓", "😕", "😶", "😐"]

        await message.channel.send(f"{random.choice(liste)} :smoking:")


@tasks.loop(hours=2)
async def nehir_adam():
    for c in Bot.get_all_channels():
        if c.id == 901157476932661308:
            choosed = random.choice(liste)
            embed = discord.Embed(title=choosed, colour=discord.Colour.from_rgb(0, 0, 55))
            embed.set_thumbnail(url=nehir)
            await c.send(embed=embed)


@Bot.command()
async def dolar_basla1(ctx):
    channel = Bot.get_channel(917421180980428840)
    await channel.send("https://cdn.discordapp.com/attachments/917506386181636186/917508733641293854/2dolar.png")


@tasks.loop(seconds=2)
async def dolar_grafik_canli():
    file = open("dolar_logs.txt", "r")
    print(1)
    veri = file.readlines()

    uzunluk = len(veri)
    print(uzunluk)
    file.close()
    x = []
    y = []
    yeni_veri = veri[-500:]
    for i in yeni_veri:
        veri1 = i[1:8].replace(",", ".")
        print(veri1)
        y.append(float(veri1))
    y = set(y)
    y = list(y)
    for i2 in range(0, len(y)):
        x.append(i2)

    print(x)
    print(y)

    minFiyat = min(y)
    maksFiyat = max(y)
    print(minFiyat)
    print(maksFiyat)
    plt.plot(x, y, linestyle="solid", marker="o", markersize=2, markerfacecolor="red", markeredgecolor="red")
    plt.title("grafik")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.xlim(0, len(x))
    plt.ylim(minFiyat - 0.13, maksFiyat + 0.13)
    plt.legend()
    plt.savefig('2dolar.png')
    plt.close()
    channel = Bot.get_channel(917506386181636186)
    msg = await channel.send(file=discord.File("2dolar.png"))
    url_dolar = msg.attachments[0].url
    print(url_dolar)

    message_id = 917509061723979846
    channel_esas = Bot.get_channel(917421180980428840)
    msg_esas = channel_esas.fetch_message(message_id)
    await msg_esas.edit(url_dolar)


esasVeri = ""


@tasks.loop(seconds=2)
async def dolar_tl():
    channel = Bot.get_channel(910573909903036446)
    channel_log = Bot.get_channel(915347152471990303)
    message_id = 910580028033601566

    r = requests.get("https://www.bloomberght.com/doviz/dolar")
    soup = BeautifulSoup(r.content, "html.parser")
    veri = soup.find("span", attrs={"data-secid": "USDTRY Curncy"}).text

    print(veri)
    veri = str(veri)
    tarih = datetime.now()
    tarih_log = datetime.now()
    tarih_log = tarih_log.strftime("saat - %H (+3): %M : %S  |  tarih -  %d / %m / %y")
    tarih = tarih.strftime("%H (+3): %M : %S")

    global esasVeri
    if veri == esasVeri:
        pass
    else:
        esasVeri = veri
        await channel_log.send(f" {veri}          : {tarih_log}")
        file = open("dolar_logs.txt", "a")
        file.writelines(f" {veri}          : {tarih_log}\n")
        file.close()
        # dLog = f" {veri}          : {tarih_log}\n"

        # value = db["dolar"].value
        # print(f"ilk dolar_tl {value}")
        # value.append(dLog)
        # print(f"2. dolar_tl {value}")
        # db["dolar"] = value

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    embed = discord.Embed(title="Dolar / Türk Lirası", description=f"**{veri}**\n\n{tarih}",
                          colour=discord.Colour.from_rgb(r, g, b))

    msg = await channel.fetch_message(message_id)
    await msg.edit(embed=embed, content="")


kitap1 = "https://lh3.googleusercontent.com/pw/AM-JKLV0oeORKxEWDO8u_R8lMjfxKMm1zoYjUb6xfvexIvj0ue89sFwS8n-Jf7KHRk0Th4NZmDLzWR8A5rK6k_-aZnE36i5Mb__N7aIjC23MZDvEO-5SliIpWwPRoEdrQTt1pp77kQP5UFl3bHQ5B3iDfUcDWg=s512-no?authuser=0"
kitap2 = "https://lh3.googleusercontent.com/pw/AM-JKLVtGQpXJYnaDoGDkUc1SF3JdYNthD3EsDIV5Z7ilY50hqTBFYY1x1HPRJYq753W-Jrq6sczkJqsxtyMhc4hEibgyNlBdsnONRHYLg6lwP29aoDEFb0CSBh1fzIP5wkoFiMuF0qimDV5jRWSDApSznc5-Q=s512-no?authuser=0"


@Bot.command()
async def kitap(ctx):
    embed = discord.Embed(title="**(Bir şaka kitabı)**", colour=discord.Colour.from_rgb(22, 22, 120))
    embed.set_image(url=kitap1)
    await ctx.send(embed=embed)

    await asyncio.sleep(delay=1)

    embed = discord.Embed(title="** İçine bakacak mısın ?\n\n [ Y ]\t\t\t\t\t[ N ]**",
                          colour=discord.Colour.from_rgb(22, 22, 120))
    embed.set_image(url=kitap1)
    await ctx.send(embed=embed)
    msg = await Bot.wait_for("message")
    if msg.content == "y" or msg.content == "Y":

        embed = discord.Embed(title="**( Şaka kitabının içinde kuantum fiziği kitabı var. )**",
                              colour=discord.Colour.from_rgb(22, 22, 120))
        embed.set_image(url=kitap1)
        await ctx.send(embed=embed)

        await asyncio.sleep(delay=2)

        embed = discord.Embed(title="**( İçine bakıyorsun. . . )**", colour=discord.Colour.from_rgb(22, 22, 120))
        embed.set_image(url=kitap1)
        await ctx.send(embed=embed)

        await asyncio.sleep(delay=2)

        embed = discord.Embed(title="**( Kuantum fiziği kitabının içinde başka bir şaka kitabı var. )**",
                              colour=discord.Colour.from_rgb(22, 22, 120))
        embed.set_image(url=kitap1)
        await ctx.send(embed=embed)

        await asyncio.sleep(delay=2)

        embed = discord.Embed(title="**( İçine bakıyorsun. . . )**", colour=discord.Colour.from_rgb(22, 22, 120))
        embed.set_image(url=kitap1)
        await ctx.send(embed=embed)

        await asyncio.sleep(delay=2)

        embed = discord.Embed(title="**( Başka bir kuantum fiziği kitabı var. . . )**",
                              colour=discord.Colour.from_rgb(22, 22, 120))
        embed.set_image(url=kitap1)
        await ctx.send(embed=embed)

        await asyncio.sleep(delay=2)

        embed = discord.Embed(title="**( Durmaya karar verdin. )**", colour=discord.Colour.from_rgb(22, 22, 120))
        embed.set_image(url=kitap1)
        await ctx.send(embed=embed)
    else:

        embed = discord.Embed(title="**( Kitabı fırlatıp attın. )**", colour=discord.Colour.from_rgb(22, 22, 120))
        embed.set_image(url=kitap2)
        await ctx.send(embed=embed)


@Bot.command(aliases=["dolar_min"])
async def dolar_maks(ctx):
    file = open("dolar_logs.txt", "r")
    print(1)
    # value = db["dolar"].value

    veri = file.readlines()
    # veri = value

    uzunluk = len(veri)
    print(uzunluk)
    file.close()
    x = []
    y = []
    for i in range(0, uzunluk):
        veri1 = veri[i][1:8].replace(",", ".")
        # print(veri1)
        y.append(float(veri1))
    maks = max(y)
    min1 = min(y)
    tarih = veri[1][-13:-1]
    await ctx.send(
        f"Görülen En Yüksek Değer : {maks}\nGörülen En Düşük Değer {min1}\n\n {tarih} Tarihinden itibaren ölçülmüştür.")


@Bot.command(aliases=["dolarg", "dg", "dolargrafik", "dolar_grafik", "Dolar_Grafik", "Dolar_grafik"])
async def DolarGrafik(ctx):
    file = open("dolar_logs.txt", "r")
    print(1)
    veri = file.readlines()
    # value = db["dolar"].value
    # veri = value

    uzunluk = len(veri)
    print(uzunluk)
    file.close()
    x = []
    y = []
    for i in range(0, uzunluk, (uzunluk // 500)):
        veri1 = veri[i][1:8].replace(",", ".")
        print(veri1)
        y.append(float(veri1))
    for i2 in range(0, len(y)):
        x.append(i2)
    tarih = veri[1][-13:-1]
    tarihSon = veri[-1][-13:-1]
    print(x)
    print(y)

    minFiyat = min(y)
    maksFiyat = max(y)
    print(minFiyat)
    print(maksFiyat)
    plt.plot(x, y, linestyle="solid", linewidth=1.9)  # ,marker = "o", markerfacecolor="red",markeredgecolor="red")
    plt.title("Dolar/Türk Lirası")
    plt.xlabel(f"{tarih}              -->              {tarihSon}")
    plt.ylabel("USD/TL")
    plt.xlim(0, len(x))
    plt.ylim(minFiyat - 0.08, maksFiyat + 0.08)
    plt.legend()
    plt.savefig('1dolar.png')
    plt.savefig('1dolar.pdf')

    await ctx.send(file=discord.File('1dolar.png'))
    await ctx.send(file=discord.File('1dolar.pdf'))
    plt.close()


@Bot.command(aliases=["dolardetay"])
async def DolarGrafikDetay(ctx, arg: int = 1):
    if arg == 1:
        await ctx.send("Bu İşlem Çok Zaman Alabilir...\nLütfen Sabırla Bekleyiniz.")
    elif arg < 10:
        await ctx.send("Bu İşlem Biraz Zaman Alabilir...")
    file = open("dolar_logs.txt", "r")
    print(1)
    veri = file.readlines()
    # value = db["dolar"].value
    # veri = value

    uzunluk = len(veri)
    print(uzunluk)
    file.close()
    x = []
    y = []
    for i in range(0, uzunluk, (uzunluk // (uzunluk // arg))):
        veri1 = veri[i][1:8].replace(",", ".")
        print(veri1)
        y.append(float(veri1))
    for i2 in range(0, len(y)):
        x.append(i2)
    tarih = veri[1][-13:-1]
    tarihSon = veri[-1][-13:-1]
    print(x)
    print(y)

    minFiyat = min(y)
    maksFiyat = max(y)
    print(minFiyat)
    print(maksFiyat)
    plt.plot(x, y, linestyle="solid", linewidth=0.9)  # ,marker = "o", markerfacecolor="red",markeredgecolor="red")
    plt.title("Dolar/Türk Lirası")
    plt.xlabel(f"{tarih}              -->              {tarihSon}")
    plt.ylabel("USD/TL")
    plt.xlim(0, len(x))
    plt.ylim(minFiyat - 0.08, maksFiyat + 0.08)
    plt.legend()
    plt.savefig('1dolar.png')
    plt.savefig('1dolar.pdf')

    await ctx.send(file=discord.File('1dolar.png'))
    await ctx.send(file=discord.File('1dolar.pdf'))
    plt.close()






Bot.run("BURAYA DİSCORD BOT TOKENİ GELİR")