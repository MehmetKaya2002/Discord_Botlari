import discord
from discord.ext import commands, tasks
import random
import requests
from bs4 import BeautifulSoup
import time
import ast
import asyncio
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import string
import json

intents = discord.Intents(messages=True, guilds=True, reactions=True, presences=True, members=True)
Bot = commands.Bot(command_prefix="-", intents=intents,description="açıklama")

stringList = string.ascii_uppercase


@Bot.event
async def on_ready():

    print("ben hazırım")
    #osym.start()

@Bot.event
async def on_message(message):
    await Bot.process_commands(message)

    if message.content.find("(:") != -1 or message.content.find(":)") != -1:
        metin = ""
        uzunluk = random.randint(9,35)
        for x in range(uzunluk):
            secim = random.choice(stringList)
            print(secim)
            metin += f"{secim}"
        await message.channel.send(metin)
    if message.content.startswith("Gül") or message.content.startswith("gül") or message.content.startswith("Gül"):
        metin = ""
        uzunluk = random.randint(9, 35)
        for x in range(uzunluk):
            secim = random.choice(stringList)
            print(secim)
            metin += f"{secim}"
        await message.channel.send(metin)
        await message.delete()








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







    if message.content.startswith("düet yap"):
        await asyncio.sleep(2.5)
        await message.channel.send("Dünyanın sonuna doğmuşum")
    if message.content.startswith("Ya da ölmüşüm de haberim yok"):
        await asyncio.sleep(2.5)
        await message.channel.send("İyi bilirdik derler elbet ardımdan")
        await asyncio.sleep(2.5)
    if message.content.startswith("Bundan büyük bi' yalan yok"):
        await asyncio.sleep(2.5)
        await message.channel.send("-2 Dünyanın sonuna doğmuşum")
    if message.content.startswith("-2 Ya da ölmüşüm de haberim yok"):
        await asyncio.sleep(2.5)
        await message.channel.send("-2 İyi bilirdik derler elbet ardımdan")
        await asyncio.sleep(2.5)
    if message.content.startswith("-2 Bundan büyük bi' yalan yok"):
        await asyncio.sleep(2.5)
        await message.channel.send("Tabi baba, kanımızda var.  (MHT-C)")
    if message.content.startswith("Bizden Güzeli Mezarda Baba   (MHT-G)"):
        await asyncio.sleep(1)
        await message.channel.send("")




    if message.content.startswith("🚬"):
        liste = ["😢", "🥲", "😭", "😥", "😓", "😕", "😶", "😐"]

        await message.channel.send(f"{random.choice(liste)} :smoking:")




@Bot.command()
async def kanal(ctx):
    guild = ctx.message.guild
    await guild.create_voice_channel("Chill")




@tasks.loop(seconds=1)
async def osym():
    try:
        target = await Bot.fetch_user(343051107788128256)

        sonuc1 = "2021 Tıpta Uzmanlık Eğitimi Giriş Sınavı (TUS) 2. Dönem Sonuçları"


        zaman = datetime.now()


        channel = Bot.get_channel(890783026680823888)

        r = requests.get("https://sonuc.osym.gov.tr/SonucSec.aspx")
        print(r)
        soup = BeautifulSoup(r.content, 'html.parser')
        liste = soup.find_all("a")



        sonuc_sayi = len(liste)
        print(len(liste))

        for x in liste:
            sonuc_adi = str(x)
            sonuc_adi = sonuc_adi.split(">")

            sonuc_adi2 = sonuc_adi[1].split("<")
            #print(sonuc_adi2[0])



        sonuc_1 = str(liste[0])

        sonuc_1 = sonuc_1.split(">")
        sonuc_2 = sonuc_1[1].split("<")
        print(f"{sonuc_2[0]}         zaman : {zaman}")
        print(f"{sonuc1}         zaman : {zaman}")
        if sonuc1 == sonuc_2[0]:
            print("eşitler")

        if sonuc_sayi != 11:
            print("YENİ SONUÇ AÇIKLANDI")
            await channel.send(f"YENİ SONUÇ AÇIKLANDI \n\n {sonuc_2[0]}      zaman : {zaman}")
            await target.send(f"YENİ SONUÇ AÇIKLANDI  \n\n {sonuc_2[0]}      zaman : {zaman}")


            for x in liste:
                sonuc_adi = str(x)
                sonuc_adi = sonuc_adi.split(">")

                sonuc_adi2 = sonuc_adi[1].split("<")
                #print(sonuc_adi2[0])
                await channel.send(sonuc_adi2[0])
        if sonuc1 != sonuc_2[0] :
            print("YENİ SONUÇ AÇIKLANDI !!!")
            await channel.send(f"YENİ SONUÇ AÇIKLANDI \n\n {sonuc_2[0]}      zaman : {zaman}")
            await target.send(f"YENİ SONUÇ AÇIKLANDI \n\n {sonuc_2[0]}       zaman : {zaman}")
    except:
        print("hata oldu")

@Bot.command()
async def onayla(ctx,arg):
    sayi = random.randint(1, 999999)
    sayi = str(sayi)

    if len(sayi) == 1:
        sayi = f"00000{sayi}"
    if len(sayi) == 2:
        sayi = f"0000{sayi}"
    if len(sayi) == 3:
        sayi = f"000{sayi}"
    if len(sayi) == 4:
        sayi = f"00{sayi}"
    if len(sayi) == 5:
        sayi = f"0{sayi}"

    mesaj = MIMEMultipart()
    mesaj['from'] = "GÖNDEREN MAİLİ"
    mesaj['to'] = f"{arg}"
    mesaj['subject'] = sayi

    yazi = "kod : " + sayi

    mesaj_yapisi = MIMEText(yazi, 'plain')
    mesaj.attach(mesaj_yapisi)
    try:
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.ehlo()
        mail.login('GÖNDEREN MAİLİ', 'GÖNDEREN MAİLİN ŞİFRESİ')
        mail.sendmail(mesaj['from'], mesaj['to'], mesaj.as_string())
        print('Mail gönderildi')
        await ctx.send("Mail gönderildi")
        mail.close()
    except:
        print('hata oluştu')

    count = 3
    while count > 0:


        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel

        msg = await Bot.wait_for("message", check=check)

        if msg.content == sayi:
            print("DOĞRULANDI")
            await ctx.send("DOĞRULANDI")
            break
        else:
            count -= 1
            print(f"Yanlış KOD\nKalan Deneme Hakkın : {count}")
            await ctx.send(f"Yanlış KOD\nKalan Deneme Hakkın : {count}")
            continue
    if count == 0:
        print("HAK KALMADI.")
        await ctx.send("HAK KALMADI")




@Bot.command()

async def vki(ctx,boy: int,kilo: float):
    boy2 = boy*boy
    vki = kilo / boy2
    print(vki*1000)


    await ctx.send(vki*10000)


@Bot.command()
async def üs(ctx,sayi1,sayi2):
    sayi1 = int(sayi1)
    sayi2 = int(sayi2)
    sonuc = sayi1**sayi2
    print(sonuc)
    embed = discord.Embed(title=f"{sayi1} ** {sayi2} =",description=sonuc)
    await ctx.send(embed=embed)


@Bot.command(aliases=["ck"])
async def create_key(ctx,uzunluk : int):
    harfler = "abcdefgghijklmnoprstuvyzqwx"
    buyuk_harfler = harfler.upper()
    sayilar = "1234567890"
    liste = [harfler,buyuk_harfler,sayilar]

    key=""
    for x in range(uzunluk):
        pool = random.choice(liste)
        key += random.choice(pool)
    await ctx.send(f"Your KEY : {key}")

use = True

@Bot.command()
async def kutla(ctx):
    target = await Bot.fetch_user(784845899972083743)
    await target.send("https://www.youtube.com/watch?v=kOvLkkJc_l0")

@Bot.command()
async def çiz(ctx,width : int,height : int):
    global use
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel
    if width >= 13 or height >= 13:
        await ctx.send("12x12 den büyük değer girmeyin")
    else:

        if use :
            use = False
            print(use)
            kare = ":black_square_button:"#Bot.get_emoji(908167350963023874)
            red =":red_square:"
            green =":green_square:"
            blue =":blue_square:"
            yellow =":yellow_square:"
            purple =":purple_square:"
            brown =":brown_square:"
            orange =":orange_square:"
            black =":black_large_square:"
            white =":white_large_square:"


            mht_emoji = Bot.get_emoji(908350210072248330)

            liste01 = []
            liste02 = []



            for x in range(height):
                for y in range(width):
                    liste02.append(kare)
                liste01.append(liste02)
                liste02 = []
            print(liste01)

            board = ""
            for countx in range(-1,width):
                if countx == -1:
                    board +=f"{mht_emoji}"
                if countx == 0:
                    board +=f":zero:"
                if countx == 1:
                    board +=f":one:"
                if countx == 2:
                    board +=f":two:"
                if countx == 3:
                    board +=f":three:"
                if countx == 4:
                    board +=f":four:"
                if countx == 5:
                    board +=f":five:"
                if countx == 6:
                    board +=f":six:"
                if countx == 7:
                    board +=f":seven:"
                if countx == 8:
                    board +=f":eight:"
                if countx == 9:
                    board +=f":nine:"
                if countx == 10:
                    board +=f":a:"
                if countx == 11:
                    board +=f":b:"

            board += f"\n"
            print(len(liste01))
            for y in range(0,len(liste01)):

                if y == 0:
                    board +=f":zero:"
                if y == 1:
                    board +=f":one:"
                if y == 2:
                    board +=f":two:"
                if y == 3:
                    board +=f":three:"
                if y == 4:
                    board +=f":four:"
                if y == 5:
                    board +=f":five:"
                if y == 6:
                    board +=f":six:"
                if y == 7:
                    board +=f":seven:"
                if y == 8:
                    board +=f":eight:"
                if y == 9:
                    board +=f":nine:"
                if y == 10:
                    board +=f":a:"
                if y == 11:
                    board +=f":b:"

                for x in liste01[y]:

                    board += f"{x}"
                board += f"\n"
            print(len(board))
            embedRenkler = discord.Embed(
                title="Renk Kodları\nçizmek için yazmanız gereken mesaj =\n <renk_kodu> <yataydaki sıra no> <dikeydeki sıra no> ",
                description=f"{red} : red\n{green} : green\n{blue} : blue\n{yellow} : yellow\n{purple} : purple\n{orange} : orange\n{brown} : brown\n{black} : black\n{white} : white\n",
                colour=discord.Colour.from_rgb(0, 0, 0))
            await ctx.send(embed=embedRenkler)

            embed = discord.Embed(
                title="PixiM Art\nçizmek için yazmanız gereken mesaj = \n<renk_kodu> <yataydaki sıra no> <dikeydeki sıra no> \n kaydetmek için kaydet, çıkmak için exit yazın",
                description=f"{board}",
                colour=discord.Colour.from_rgb(0,0,0))
            embedBoard =await ctx.send(embed=embed)


            while True:
                try:
                    msg1 = await Bot.wait_for("message", check=check)


                    msg = msg1.content
                    msg = msg.lower()
                    print(msg)
                    if msg == "exit":
                        use = True
                        await ctx.send("çizim tablosu kapandı yeni bir tane oluşturabilirsin")
                        break
                    if msg == "save":
                        await ctx.send("çiziminize bir isim vermelisiniz lütfen mesaj olarak yazın. bu işlem geri alınamaz !")
                        kayit_bilgi = await Bot.wait_for("message",check=check)
                        kayit_bilgi = kayit_bilgi.content
                        dictionary = {
                            "name" : f"{kayit_bilgi}",
                            "art" : f"{liste01}",
                            "width" :f"{width}",
                            "height": f"{height}",
                        }
                        with open(f"art{ctx.author.id}.json","w") as outfile:
                            json.dump(dictionary,outfile)
                        await ctx.send(f"çiziminizin adı {kayit_bilgi} oldu.")
                        continue
                    if msg == "open":
                        with open(f"art{ctx.author.id}.json","r") as openfile:
                            json_object = json.load(openfile)
                            liste01 = ast.literal_eval(json_object["art"])
                            print(liste01)
                            print(type(liste01))

                            width = int(json_object["width"])
                            height = int(json_object["height"])

                            board = ""

                            for countx in range(-1, width):

                                if countx == -1:
                                    board += f"{mht_emoji}"
                                if countx == 0:
                                    board += f":zero:"
                                if countx == 1:
                                    board += f":one:"
                                if countx == 2:
                                    board += f":two:"
                                if countx == 3:
                                    board += f":three:"
                                if countx == 4:
                                    board += f":four:"
                                if countx == 5:
                                    board += f":five:"
                                if countx == 6:
                                    board += f":six:"
                                if countx == 7:
                                    board += f":seven:"
                                if countx == 8:
                                    board += f":eight:"
                                if countx == 9:
                                    board += f":nine:"
                                if countx == 10:
                                    board += f":a:"
                                if countx == 11:
                                    board += f":b:"

                            board += f"\n"
                            for y in range(0, len(liste01)):

                                if y == 0:
                                    board += f":zero:"
                                if y == 1:
                                    board += f":one:"
                                if y == 2:
                                    board += f":two:"
                                if y == 3:
                                    board += f":three:"
                                if y == 4:
                                    board += f":four:"
                                if y == 5:
                                    board += f":five:"
                                if y == 6:
                                    board += f":six:"
                                if y == 7:
                                    board += f":seven:"
                                if y == 8:
                                    board += f":eight:"
                                if y == 9:
                                    board += f":nine:"
                                if y == 10:
                                    board += f":a:"
                                if y == 11:
                                    board += f":b:"

                                for x in liste01[y]:
                                    board += f"{x}"
                                board += f"\n"
                            print(board)
                            embed = discord.Embed(
                                title="PixiM Art\nçizmek için yazmanız gereken mesaj = \n<renk_kodu> <yataydaki sıra no> <dikeydeki sıra no> ",
                                description=f"{board}",
                                colour=discord.Colour.from_rgb(0, 0, 0))
                            await embedBoard.edit(embed=embed)
                            continue





                    msg_koordinat = msg.split(" ")
                    renk_kodu = msg_koordinat[0]

                    if msg_koordinat[1] == "a":
                        msg_koordinat[1] = 10
                    if msg_koordinat[1] == "b":
                        msg_koordinat[1] = 11
                    if msg_koordinat[2] == "a":
                        msg_koordinat[2] = 10
                    if msg_koordinat[2] == "b":
                        msg_koordinat[2] = 11
                    x_koordinat =int(msg_koordinat[1])
                    y_koordinat =int(msg_koordinat[2])

                    if renk_kodu == "red":
                        renk_kodu = red
                    elif renk_kodu == "green":
                        renk_kodu = green
                    elif renk_kodu == "blue":
                        renk_kodu = blue
                    elif renk_kodu == "yellow":
                        renk_kodu = yellow
                    elif renk_kodu == "purple":
                        renk_kodu = purple
                    elif renk_kodu == "orange":
                        renk_kodu = orange
                    elif renk_kodu == "brown":
                        renk_kodu = brown
                    elif renk_kodu == "black":
                        renk_kodu = black
                    elif renk_kodu == "white":
                        renk_kodu = white
                    elif renk_kodu != "red" or renk_kodu != "green" or renk_kodu != "blue" or renk_kodu != "yellow" or renk_kodu != "purple" or renk_kodu != "orange" or renk_kodu != "brown" or renk_kodu != "black" or renk_kodu != "white":
                        renk_kodu = kare

                    liste01[y_koordinat][x_koordinat] = renk_kodu

                    board = ""
                    for countx in range(-1, width):
                        if countx == -1:
                            board += f"{mht_emoji}"
                        if countx == 0:
                            board += f":zero:"
                        if countx == 1:
                            board += f":one:"
                        if countx == 2:
                            board += f":two:"
                        if countx == 3:
                            board += f":three:"
                        if countx == 4:
                            board += f":four:"
                        if countx == 5:
                            board += f":five:"
                        if countx == 6:
                            board += f":six:"
                        if countx == 7:
                            board += f":seven:"
                        if countx == 8:
                            board += f":eight:"
                        if countx == 9:
                            board += f":nine:"
                        if countx == 10:
                            board += f":a:"
                        if countx == 11:
                            board += f":b:"

                    board += f"\n"
                    for y in range(0, len(liste01)):

                        if y == 0:
                            board += f":zero:"
                        if y == 1:
                            board += f":one:"
                        if y == 2:
                            board += f":two:"
                        if y == 3:
                            board += f":three:"
                        if y == 4:
                            board += f":four:"
                        if y == 5:
                            board += f":five:"
                        if y == 6:
                            board += f":six:"
                        if y == 7:
                            board += f":seven:"
                        if y == 8:
                            board += f":eight:"
                        if y == 9:
                            board += f":nine:"
                        if y == 10:
                            board += f":a:"
                        if y == 11:
                            board += f":b:"

                        for x in liste01[y]:
                            board += f"{x}"
                        board += f"\n"

                    embed = discord.Embed(
                        title="PixiM Art\nçizmek için yazmanız gereken mesaj = \n<renk_kodu> <yataydaki sıra no> <dikeydeki sıra no> ",
                        description=f"{board}",
                        colour=discord.Colour.from_rgb(0, 0, 0))
                    await embedBoard.edit(embed=embed)
                    await msg1.delete()



                except:
                    await ctx.send("hatalı bilgi girişi. tekrar deneyin.")





        else:
            await ctx.send("Zaten bir çizim tablosu oluştu")
@Bot.command()
async def c(ctx,sayi):
    sayi = int(sayi)
    yazi = ""
    while sayi > 1:
        if sayi % 2 == 0:
            sayi = sayi//2
            print(sayi)
            yazi += f"{sayi}\n"

        else:
            sayi = 3*sayi+1
            print(sayi)
            yazi += f"{sayi}\n"
    await ctx.send(yazi)

#######                           CLASH OF CLANS                            ######
#________________________________________________________________________________#

headers = {
    'Accept':'application/json',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6Ijg1OTY3M2NjLWJiY2UtNDgxMy04OTVmLTM1ZDZkOGExN2I4MyIsImlhdCI6MTYzNzk0MjAxNSwic3ViIjoiZGV2ZWxvcGVyLzNkODQ3MjFkLWIwZWYtNWI5MS05MzVlLTY3MDY0MTIwOThlZSIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjk0LjEyMi4xNTYuMjEiXSwidHlwZSI6ImNsaWVudCJ9XX0.jtT2ugH_bcY1X51lQjYtODVugXRwDQlqOfE2cQHw6X7kVoCkPAroCmDD5XreQcFLr2SWxrabFnpXf3PP3LIAWQ'
}


#mehmet tag: #U8UYC290


@Bot.command()
async def coc_info(ctx,tag):
    barbar = Bot.get_emoji(888187722441842759)
    okcu = Bot.get_emoji(888187722865471528)
    dev = Bot.get_emoji(888187722626387969)
    goblin = Bot.get_emoji(888187723003854878)
    duvar_yikici = Bot.get_emoji(888187722798362655)
    balon = Bot.get_emoji(888187722710278187)
    buyucu = Bot.get_emoji(888187722441818124)
    sifaci = Bot.get_emoji(888187722374713356)
    ejderha = Bot.get_emoji(888187722718654504)
    pekka = Bot.get_emoji(888187722928373790)
    bebek_ejderha = Bot.get_emoji(888187722441850921)
    madenci = Bot.get_emoji(888187722710257764)
    elektro_ejderha = Bot.get_emoji(888187723050020894)
    yeti = Bot.get_emoji(888187722928382062)
    ejderha_binicisi = Bot.get_emoji(888187722878034000)
    minyon = Bot.get_emoji(888187722764804146)
    binici = Bot.get_emoji(888187722722836520)
    valkyre = Bot.get_emoji(888187722840289310)
    golem = Bot.get_emoji(888187722978713651)
    cadi = Bot.get_emoji(888187722810929193)
    lav_tazisi = Bot.get_emoji(888187721812701255)
    atici = Bot.get_emoji(888187722815135804)
    buz_golemi = Bot.get_emoji(888187722446012427)
    kelle_avcisi = Bot.get_emoji(888187722739634217)






    if tag == "mehmet" or tag == "Mehmet" or tag == "cheif" or tag == "Chief":
        tag = "U8UYC290"
    if tag == "emre" or tag == "Emre" or tag == "Judge2World" or tag == "judge2world":
        tag = "2GR89URJQ"







    response1 = requests.get(f"https://api.clashofclans.com/v1/players/%23{tag}", headers=headers)
    user_json = response1.json()
    print(user_json)








    player_name = user_json["name"]
    tag = user_json["tag"]
    townHall = user_json["townHallLevel"]
    expLevel = user_json["expLevel"]
    trophies = user_json["trophies"]
    bestTrophies = user_json["bestTrophies"]
    warStars = user_json["warStars"]
    attackWins = user_json["attackWins"]
    defensewins = user_json["defenseWins"]


    clanName = user_json["clan"]["name"]
    clanTag = user_json["clan"]["tag"]
    clanLevel = user_json["clan"]["clanLevel"]
    clan_icon = user_json["clan"]["badgeUrls"]["large"]

    lig_name = user_json["league"]["name"]
    lig_icon = user_json["league"]["iconUrls"]["medium"]
    #https: // api - assets.clashofclans.com / leagues / 288 / CorhMY9ZmQvqXTZ4VYVuUgPNGSHsO0cEXEL5WYRmB2Y.png


    ################### TROOPS #######################


    acik_birimler = []

    for x in range(len(user_json["troops"])):
        isim = user_json["troops"][x]["name"]
        if isim == "Barbarian":
            print(f"barbar level : {user_json['troops'][x]['level']}")
            barbar1 = f"{barbar} barbar level : **{user_json['troops'][x]['level']}**"
            acik_birimler.append(barbar1)
        if isim == "Archer":
            print(f"Archer level : {user_json['troops'][x]['level']}")
            okcu1 = f"{okcu} Archer level : **{user_json['troops'][x]['level']}**"
            acik_birimler.append(okcu1)
        if isim == "Giant":
            print(f"Giant level : {user_json['troops'][x]['level']}")
            dev1 = f"{dev} Giant level : **{user_json['troops'][x]['level']}**"
            acik_birimler.append(dev1)
        if isim == "Goblin":
            print(f"Goblin level : {user_json['troops'][x]['level']}")
            goblin1 = f"{goblin} Goblin level : **{user_json['troops'][x]['level']}**"
            acik_birimler.append(goblin1)
        if isim == "Wall Breaker":
            print(f"Wall Breaker level : {user_json['troops'][x]['level']}")
            duvar_yikici1 = f"{duvar_yikici} Wall Breaker level : **{user_json['troops'][x]['level']}**"
            acik_birimler.append(duvar_yikici1)
        if isim == "Balloon":
            print(f"Balloon level : {user_json['troops'][x]['level']}")
            balon1 = f"{balon} Balloon level : **{user_json['troops'][x]['level']}**"
            acik_birimler.append(balon1)
        if isim == "Wizard":
            print(f"Wizard level : {user_json['troops'][x]['level']}")
            buyucu1 = f"{buyucu} Wizard level : **{user_json['troops'][x]['level']}**"
            acik_birimler.append(buyucu1)
        if isim == "Healer":
            print(f"Healer level : {user_json['troops'][x]['level']}")
            sifaci1 = f"{sifaci} Healer level : **{user_json['troops'][x]['level']}**"
            acik_birimler.append(sifaci1)
        if isim == "Dragon":
            print(f"Dragon level : {user_json['troops'][x]['level']}")
            ejderha1 = f"{ejderha} Dragon level : **{user_json['troops'][x]['level']}**"
            acik_birimler.append(ejderha1)
        if isim == "P.E.K.K.A":
            print(f"P.E.K.K.A level : {user_json['troops'][x]['level']}")
            pekka1 = f"{pekka} P.E.K.K.A level : **{user_json['troops'][x]['level']}**"
            acik_birimler.append(pekka1)
        if isim == "Baby Dragon" and user_json['troops'][x]['village'] == "home" :
            print(f"Baby Dragon level : {user_json['troops'][x]['level']}")
            bebek_ejderha1 = f"{bebek_ejderha} Baby Dragon level : **{user_json['troops'][x]['level']}**"
            acik_birimler.append(bebek_ejderha1)
        if isim == "Miner":
            print(f"Miner level : {user_json['troops'][x]['level']}")
            madenci1 = f"{madenci} Miner level : **{user_json['troops'][x]['level']}**"
            acik_birimler.append(madenci1)
        if isim == "Yeti":
            print(f"Yeti level : {user_json['troops'][x]['level']}")
            yeti1 = f"{yeti} Yeti level : **{user_json['troops'][x]['level']}**"
            acik_birimler.append(yeti1)
        if isim == "Dragon Rider":
            print(f"Dragon Rider level : {user_json['troops'][x]['level']}")
            ejderha_binicisi1 = f"{ejderha_binicisi} Dragon Rider level : **{user_json['troops'][x]['level']}**"
            acik_birimler.append(ejderha_binicisi1)
        if isim == "Minion":
            print(f"Minion level : {user_json['troops'][x]['level']}")
            minyon1 = f"{minyon} Minion level : **{user_json['troops'][x]['level']}**"
            acik_birimler.append(minyon1)
        if isim == "Hog Rider":
            print(f"Hog Rider level : {user_json['troops'][x]['level']}")
            binici1 = f"{binici} Hog Rider level : **{user_json['troops'][x]['level']}**"
            acik_birimler.append(binici1)
        if isim == "Valkyrie":
            print(f"Valkyrie level : {user_json['troops'][x]['level']}")
            valkyre1 = f"{valkyre} Valkyrie level : **{user_json['troops'][x]['level']}**"
            acik_birimler.append(valkyre1)
        if isim == "Golem":
            print(f"Golem level : {user_json['troops'][x]['level']}")
            golem1 = f"{golem} Golem level : **{user_json['troops'][x]['level']}**"
            acik_birimler.append(golem1)
        if isim == "Witch":
            print(f"Witch level : {user_json['troops'][x]['level']}")
            cadi1 = f"{cadi} Witch level : **{user_json['troops'][x]['level']}**"
            acik_birimler.append(cadi1)
        if isim == "Lava Hound":
            print(f"Lava Hound level : {user_json['troops'][x]['level']}")
            lav_tazisi1 = f"{lav_tazisi} Lava Hound level : **{user_json['troops'][x]['level']}**"
            acik_birimler.append(lav_tazisi1)
        if isim == "Bowler":
            print(f"Bowler level : {user_json['troops'][x]['level']}")
            atici1 = f"{atici} Bowler level : **{user_json['troops'][x]['level']}**"
            acik_birimler.append(atici1)
        if isim == "Ice Golem":
            print(f"Ice Golem level : {user_json['troops'][x]['level']}")
            buz_golemi1 = f"{buz_golemi} Ice Golem level : **{user_json['troops'][x]['level']}**"
            acik_birimler.append(buz_golemi1)
        if isim == "Headhunter":
            print(f"Headhunter level : {user_json['troops'][x]['level']}")
            kelle_avcisi1 = f"{kelle_avcisi} Headhunter level : **{user_json['troops'][x]['level']}**"
            acik_birimler.append(kelle_avcisi1)


    troops_msg = ""
    for birlik in acik_birimler:
        troops_msg += f"{birlik}\n"

    embedTroops = discord.Embed(title="Birlikler | ANA KÖY", url=lig_icon, description=troops_msg)




    embed1 = discord.Embed(title=player_name, url=lig_icon)
    embed1.set_thumbnail(url=lig_icon)
    embed1.add_field(name="------------\nGenel Bilgiler\n------------", value=f"**İsim** : {player_name}\n**Etiket** : {tag}\n**Seviye** : {expLevel}\n**Belediye Binası** : {townHall}. Seviye",inline=False)
    embed1.add_field(name="------------\nLig\n------------",value=f"**Lig İsim** : {lig_name}\n**Güncel Kupa** : {trophies}\n**En yüksek kupa** : {bestTrophies}",inline=False)
    embed1.add_field(name="------------\nSavaşlar\n------------",value=f"**Kazanılan Saldırılar** : {attackWins}\n**Kazanılan Savunmalar** : {defensewins}\n**Klan Savaşı Yıldızları** : {warStars}",inline=False)
    embed1.set_author(name=f"{ctx.message.author.name} tarafından oluşturuldu",icon_url=ctx.message.author.avatar_url)
    embed2 = discord.Embed(title=clanName, url=clan_icon)
    embed2.set_thumbnail(url=clan_icon)
    embed2.add_field(name=f"Klan Bilgileri",value=f"**Klan İsim** : {clanName}\n**Klan Etiketi** : {clanTag}\n**Klan Level** : {clanLevel}",inline=False)

    await ctx.send(embed=embed1)
    await ctx.send(embed=embed2)
    await ctx.send(embed=embedTroops)

@Bot.command()
async def ligler(ctx):
    respons = requests.get("https://api.clashofclans.com/v1/leagues", headers=headers)
    lig_json = respons.json()
    print(lig_json)

    a = lig_json["items"]
    print(len(a))
    for x in range(len(a)):
        print(lig_json["items"][x]["iconUrls"]["small"])
        await ctx.send(lig_json["items"][x]["iconUrls"]["small"])



#response1 = requests.get(f"https://api.clashofclans.com/v1/players/%232GR89URJQ", headers=headers)
#user_json = response1.json()
#print(user_json)


@Bot.command()
async def ipadPro(ctx):
    r = requests.get("https://www.apple.com/de/shop/buy-ipad/ipad-pro/12,9%22-display-2tb-space-grau-wifi-cellular")
    soup = BeautifulSoup(r.content, "html.parser")
    para = soup.findAll("span")
    para = str(para)

    para1 = soup.findAll("span", attrs={"class": "current_price"})
    fiyat = para1[4].text
    print(fiyat)
    await ctx.send(fiyat)



@Bot.command()
async def dede(ctx):
    embed = discord.Embed(
        title="**Dede**",
        description=f"Ben Dede",
        colour=discord.Colour.from_rgb(10, 200, 30))
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/901157476932661308/916791645285023814/pixil-gif-drawing_5.gif")

    embedBoard = await ctx.send(embed=embed)

@Bot.command()
async def logları_al(ctx):
    print("1")
    channel = Bot.get_channel(915347152471990303)
    await ctx.send("işlem başladı bu çok zaman alıcak...")
    messages = await channel.history(limit=250000).flatten()
    for x in messages:
        file = open("dolarGeriKurtarma.txt","a")
        file.writelines(f" {x.content}\n")
        print(x.content)
    await ctx.send("işlem bitti...")
Bot.run("BURAYA DİSCORD BOT TOKENİ GELİR")