import asyncio
import discord
from discord.ext import commands, tasks
import random
import time
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from environments import *


intents = discord.Intents(messages=True, guilds=True, reactions=True, presences=True, members=True)
Bot = commands.Bot(command_prefix="-", intents=intents)

MHT = "https://cdn.discordapp.com/avatars/860251705395380244/bbdb4d2bffb9359e645d827c1cfe4a9a.webp?size=1024"
coin = "https://cdn.discordapp.com/attachments/796394515572981782/861664491024810004/pixil-frame-0_9.png"
yolla_coin = "https://cdn.discordapp.com/attachments/796394515572981782/861375306388078592/pixil-frame-0_8.png"

gold = Bot.get_emoji(862765253431132160)


@Bot.event
async def on_ready():
    print("ben hazırım")

    await Bot.change_presence(activity=discord.Game(name="-kayıt, -bilgi, -work, -sayı, -help ..."))

@Bot.event
async def on_message(message):
    await Bot.process_commands(message)
    if message.content.startswith("Dünyanın sonuna doğmuşum"):
        await asyncio.sleep(2.5)
        await message.channel.send("Ya da ölmüşüm de haberim yok")
        await asyncio.sleep(2.5)
    if message.content.startswith("İyi bilirdik derler elbet ardımdan"):
        await asyncio.sleep(2.5)
        await message.channel.send("Bundan büyük bi' yalan yok")
    if message.content.startswith("-2 Dünyanın sonuna doğmuşum"):
        await asyncio.sleep(2.5)
        await message.channel.send("-2 Ya da ölmüşüm de haberim yok")
        await asyncio.sleep(2.5)
    if message.content.startswith("-2 İyi bilirdik derler elbet ardımdan"):
        await asyncio.sleep(2.5)
        await message.channel.send("-2 Bundan büyük bi' yalan yok")
    if message.content.startswith("Tabi baba, kanımızda var.  (MHT-C)"):
        await asyncio.sleep(1)
        await message.channel.send("Bizden Güzeli Mezarda Babba   (MHT-G)")


    if message.content.startswith("🚬"):
        liste = ["😢", "🥲", "😭", "😥", "😓", "😕", "😶", "😐"]

        await message.channel.send(f"{random.choice(liste)} :smoking:")
    print(message.content)


    if message.content.startswith("BİR KAR YAĞAR İNCE İNCE"):
        await asyncio.sleep(1)
        await message.channel.send("**BİR KAR YAĞAR İNCE İNCE**")
    if message.content.startswith("KOMANDONUN HALİ NİCE"):
        await asyncio.sleep(1)
        await message.channel.send("**KOMANDONUN HALİ NİCE**")
    if message.content.startswith("BİR OPERASYON VAR BU GECE"):
        await asyncio.sleep(1)
        await message.channel.send("**BİR OPERASYON VAR BU GECE**")
    if message.content.startswith("HEY PARAŞÜTÇÜ KOMANDO"):
        await asyncio.sleep(1)
        await message.channel.send("**HEY PARAŞÜTÇÜ KOMANDO**")
    if message.content.startswith("VUR VUR DAĞCI KOMANDO"):
        await asyncio.sleep(1)
        await message.channel.send("**VUR VUR DAĞCI KOMANDO**")
    if message.content.startswith("AFERİN TAKIM"):
        await asyncio.sleep(1)
        await message.channel.send("**SAĞOL**")
    if message.content.startswith("! AFERİN TAKIM"):
        await asyncio.sleep(1)
        await message.channel.send("**SAĞOL SAĞOL SAĞOL**")








@Bot.command(brief="-help kayıt",description="Oyunları oynayabilmek için -kayıt yazıp kaydını oluşturman gerekiyor.")
async def kayıt(ctx):

    try:
        open(f"{ctx.message.author.id}.txt")
        embed1 = discord.Embed(title=f"Zaten Kayıtlısın.", url="https://www.com",
                               description=f"{ctx.message.author.mention} ```-help diyerek kullanabileceğin komutları görebilirsin```")
        embed1.set_thumbnail(url=MHT)
        await ctx.send(embed=embed1)
    except(FileNotFoundError):
        file = open(f"{ctx.message.author.id}.txt", "a")
        time = datetime.now()
        time = time.strftime(TIME_STAMP_PATTERN)
        print(time)
        file.writelines([f"{ctx.message.author.mention}//1000//{time}//0"])

        file.close()
        embed2 = discord.Embed(title=f"Kayıt Başarılı.",
                               description=f"Hoşgeldin {ctx.message.author.mention}. ```Kaydın yapıldı -help diyerek kullanabileceğin komutları görebilirsin```",
                               url="https://www.com")
        embed2.set_thumbnail(url=MHT)
        await ctx.send(embed=embed2)


@Bot.command(brief="-help bilgi",description="Oyundaki hesap bilgilerini (Hesabındaki Coin Miktarını, Mesleğini, vb.) görebilmeni sağlar")
async def bilgi(ctx):
    try:
        file = open(f"{ctx.message.author.id}.txt", "r")
        bilgi = file.read()
        bilgi = bilgi.split("//")
        print(bilgi)
        gold = Bot.get_emoji(862765253431132160)
        para = bilgi[1]
        katılmaTarihi = ctx.message.author.created_at
        katılmaTarihi = str(katılmaTarihi)
        katılmaTarihi = katılmaTarihi.split(".")
        katılmaTarihi = katılmaTarihi[0]
        job = bilgi[3]
        job = meslek_adi(job)
        embed = discord.Embed(
            title="**Hesabım**", url="https://akjsdhgahdgasdad.com",
            # description=f" **__Kişisel Bilgiler__**\n```İsim: {ctx.message.author.name}\n\nID: {ctx.message.author.id}```\n\n **__Hesap Bakiyesi__** {gold}\n```Para: {para}  ```",
            timestamp=datetime.utcnow(),
        )
        embed.set_thumbnail(url=ctx.message.author.avatar_url)
        embed.add_field(name=f"**__Kişisel Bilgiler__**",
                        value=f"```İsim: {ctx.message.author.name}\n\nID: {ctx.message.author.id}```", inline=False)
        embed.add_field(name=f"**__Hesap Bakiyesi__** {gold}", value=f"```{para} ```")
        embed.add_field(name=f"**__Çalışma Durumu__**",value=f"```Meslek : {job}```")
        embed.set_author(name=f"{ctx.message.author.name} tarafından oluşturuldu",
                         icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)

    except(FileNotFoundError):
        embed2 = discord.Embed(title=f"Kullanıcı bulunamadı.",
                               description=f"Henüz bir hesabın yok {ctx.message.author.mention}. Lütfen   ' -kayıt  ' komutu ile hesap oluştur.",
                               url="https://www.com")
        embed2.set_thumbnail(url=MHT)
        await ctx.send(embed=embed2)
        await ctx.send(f"{ctx.message.author.mention}")


@Bot.command(brief="-help work",description="10 Dakikada bir belli miktarda Coin Kazanmanı sağlar.\nİlk kayıttan sonra 10 dakika beklemelisin.")
async def work(ctx):
    try:
        file = open(f"{ctx.message.author.id}.txt", "r")
        bilgi = file.read()
        bilgi = bilgi.split("//")
        para = int(bilgi[1])
        kaydedilmis_zaman = bilgi[2]
        print(para)
        job =bilgi[3]
        kazanilan_para = 0
        if job == "0":
            kazanilan_para = 1000
        if job == "1":
            kazanilan_para = 230000
        if job == "2":
            kazanilan_para = 41000
        if job == "3":
            kazanilan_para = 37000
        if job == "4":
            kazanilan_para = 24000
        if job == "5":
            kazanilan_para = 12000
        if job == "6" or job == "7":
            kazanilan_para = 5000
        if job == "8":
            kazanilan_para = 2500
        if job == "9":
            kazanilan_para = 121000000

        para += kazanilan_para



        if is_more_than_ten_minute(kaydedilmis_zaman):
            time = datetime.now()
            time = time.strftime(TIME_STAMP_PATTERN)

            gold = Bot.get_emoji(862765253431132160)

            file = open(f"{ctx.message.author.id}.txt", "w")
            file.write(f"{ctx.message.author.mention}//{para}//{time}//{job}")
            embed1 = discord.Embed(title=f"Güzel iş +{kazanilan_para} {gold}. Güncel Paran : {para} {gold}")
            embed1.set_thumbnail(url=coin)
            await ctx.send(embed=embed1)
            await ctx.send(f"{ctx.message.author.mention}")
        else:
            suanki_zaman = datetime.now()
            datetime_obj1 = datetime.strptime(kaydedilmis_zaman,TIME_STAMP_PATTERN)
            kalan_sure = suanki_zaman - datetime_obj1
            kalan_sure = kalan_sure.seconds
            embed2 = discord.Embed(
                title=f"Henüz 10 dakika dolmamış. son para kazanmanın ardından 10 dakika geçmesi gerekmektedir.\n Son iş yapılan zaman :{kaydedilmis_zaman}\n\n kalan süre : {600 - kalan_sure} saniye ")
            embed2.set_thumbnail(url=MHT)
            await ctx.send(embed=embed2)
            await ctx.send(f"{ctx.message.author.mention}")


    except(FileNotFoundError):
        embed2 = discord.Embed(
            title=f"Kullanıcı bulunamadı.",
            description=f"Henüz bir hesabın yok {ctx.message.author.mention}. Lütfen   ' -kayıt  ' komutu ile hesap oluştur.",
            url="https://www.com")
        embed2.set_thumbnail(url=MHT)
        await ctx.send(embed=embed2)
        await ctx.send(f"{ctx.message.author.mention}")


@Bot.command(brief="-help yolla",description="kullanıcılar arası Coin yollamayı sağlar. kullanım şekli:\n\n-yolla <yollanıcak kullanıcıyı etiketleyin> <yollanıcak miktarı yazın>\n\nörnek kullanım:\n-yolla @user1 1500")
async def yolla(ctx, arg1: discord.Member, arg2: int):
    try:
        file = open(f"{ctx.message.author.id}.txt", "r")
        file.close()
        if arg1.id == ctx.message.author.id:

            embed4 = discord.Embed(title="Kendine Para Gönderemessin :smile:")
            embed4.set_thumbnail(url=MHT)
            await ctx.send(embed=embed4)
        else:
            if arg2 % 5 == 0:
                try:
                    file = open(f"{arg1.id}.txt", "r")
                    bilgi1 = file.read()
                    bilgi1 = bilgi1.split("//")
                    job2 = bilgi1[3]
                    file.close()
                    file = open(f"{ctx.message.author.id}.txt", "r")
                    bilgi2 = file.read()
                    bilgi2 = bilgi2.split("//")
                    para2 = int(bilgi2[1])
                    job = bilgi2[3]
                    print(para2)
                    paraKontrol = para2 - arg2
                    print(paraKontrol)
                    if para2 >= 0 and paraKontrol >= 0:
                        para2 = para2 - arg2

                        file.close()

                        file = open(f"{ctx.message.author.id}.txt", "w")
                        file.write(f"{ctx.message.author.mention}//{para2}//{bilgi2[2]}//{job}")
                        file.close()

                        file = open(f"{arg1.id}.txt", "r")
                        bilgi = file.read()
                        bilgi = bilgi.split("//")

                        para = int(bilgi[1])
                        para = para + arg2
                        file.close()
                        file = open(f"{arg1.id}.txt", "w")
                        file.write(f"{arg1.mention}//{para}//{bilgi[2]}//{job2}")
                        file.close()
                        gold = Bot.get_emoji(862765253431132160)
                        embed1 = discord.Embed(
                            title="PARA TRANSFERİ",
                            url="https://www.ajsdgdsghdjaksadafa.com",
                            # description=f"**__Gönderen__**```\n{ctx.message.author.name}```\n**__Alıcı__**\n```{arg1.name}```\n**__Miktar__** {gold}\n```{arg2}```\n**__Açıklama__**\n\n{arg1.mention} adlı kullanıcıya {arg2} {gold} gönderilmiştir\n\n**__Güncel Bakiyen__** {gold}\n```{para2}```",
                            timestamp=datetime.utcnow(),
                        )
                        embed1.set_thumbnail(url=yolla_coin)
                        embed1.add_field(name=f"**__Gönderen__**", value=f"```{ctx.message.author.display_name}```",
                                         inline=True)
                        embed1.add_field(name=f"**__Alıcı__**", value=f"```{arg1.display_name}```", inline=True)
                        embed1.add_field(name=f"**__Miktar__** {gold}", value=f"```{arg2}```", inline=True)
                        embed1.add_field(name=f"**__Açıklama__**",
                                         value=f"{arg1.mention} adlı kullanıcıya {arg2} {gold} gönderilmiştir",
                                         inline=False)
                        embed1.add_field(name=f"**__Güncel Bakiyen__** {gold}", value=f"```{para2}```", inline=False)

                        embed1.set_author(name=f"{ctx.message.author.name} tarafından oluşturuldu",
                                          icon_url=ctx.message.author.avatar_url)
                        await ctx.send(embed=embed1)
                    else:
                        embed3 = discord.Embed(title="Yeterli bakiyeniz bulunmamakta.")
                        embed3.set_thumbnail(url=MHT)
                        await ctx.send(embed=embed3)

                except(FileNotFoundError):
                    await ctx.send("böyle bir kullanıcı yok")

            else:
                embed = discord.Embed(title="Lütfen 5 in katı bir sayı yazın")
                embed.set_thumbnail(url=MHT)
                await ctx.send(embed=embed)
    except:
        embed2 = discord.Embed(
            title=f"Kullanıcı bulunamadı.",
            description=f"Henüz bir hesabın yok {ctx.message.author.mention}. Lütfen   ' -kayıt  ' komutu ile hesap oluştur.",
            url="https://www.com")
        embed2.set_thumbnail(url=MHT)
        await ctx.send(embed=embed2)
        await ctx.send(f"{ctx.message.author.mention}")



@Bot.command(brief="Bu bir test komutudur.Kullanılmaz.",description="Bu bir test komutudur.Kullanılmaz.")
@commands.has_role(905747509148786698)
async def d(ctx, arg1: discord.Member):
    des = "a"
    embed = discord.Embed(
        title="**Hesabım**", url="https://ıasukjdasfjahdsjda.com",
        description=f" **__Kişisel Bilgiler__**\n```Discord İsim:  {arg1.name}\n\nDiscord ID:  {arg1.id}```\n\n **__Hesap Bakiyesi__**\n\n ```Para: ```",
        timestamp=datetime.utcnow(),
    )
    embed.set_thumbnail(url=yolla_coin)
    embed.add_field(name="isim", value="değer", inline=True)
    embed.add_field(name="isim2", value="değer2", inline=True)
    embed.add_field(name="isim3", value="```değer3```", inline=False)
    embed.set_author(name=f"{arg1.name} tarafından oluşturuldu\n {arg1.created_at}", icon_url=arg1.avatar_url)
    await ctx.send(embed=embed)


@Bot.command(brief="Bu bir test komutudur.Kullanılmaz.",description="Bu bir test komutudur.Kullanılmaz.")
@commands.has_role(905747509148786698)
async def test(ctx):
    embed = discord.Embed(title="title", timestamp=datetime.now(), description="description", url="https://www.com")

    await ctx.send(embed=embed)


@Bot.command(brief="-help sayı",description="Sayı Oyununu nasıl oynacağınız hakkında tüm bilgileri içerir")
async def sayı(ctx):
    one = ":one:"
    two = ":two:"
    three = ":three:"
    four = ":four:"
    five = ":five:"
    six = ":six:"
    seven = ":seven:"
    eight = ":eight:"
    nine = ":nine:"

    embed = discord.Embed(title="SAYI OYUNU", url="https://www.fdskjhfısfdsfs.com",
                          description=f"```Oynamak için bir sayı seçin ve aşağıdaki komutu uygulayın.\n\n-sayıseç <seçtiğiniz sayı> <yatırmak istediğiniz coin miktarı>\n\nşeklinde komut girerek oyunu oynayabilirsiniz. ```")
    embed.add_field(name="**ÖDÜLLER**",
                    value="```+ x1\n+ x2\n+ x3\n+ x4\n+ x5\n+ x6\n+ x7\n+ x8\n+ x9\n+ x10\n+ x25\n+ x50\n+ x75\n+ x100```")
    embed.add_field(name="**ANTİ ÖDÜLLER**",
                    value="```- x1\n- x2\n- x3\n- x4\n- x5\n- x6\n- x7\n- x8\n- x9\n- x10\n- x25```")
    embed.add_field(name="**BİR SAYI SEÇ**", value=f"{one} {two} {three}\n{four} {five} {six}\n{seven} {eight} {nine}",
                    inline=False)
    embed.set_author(name=f"{ctx.message.author.name} tarafından oluşturuldu",
                     icon_url=ctx.message.author.avatar_url)
    embed.set_thumbnail(url=MHT)
    await ctx.send(embed=embed)


@Bot.command(brief="-help sayıseç",description="Bir şans oyunudur. seçtiğiniz sayının arkasından gelicek değere bağlı olarak yatırdığınız Coini 100 katına kadar katlama şansınız var\n\nÖrnek Kullanım:\n\n-sayıseç <1-9 arası bir sayı> <yatırılacak Coin miktarı>")
async def sayıseç(ctx, secilen_sayi: int, coin: int):
    one = ":one:"
    two = ":two:"
    three = ":three:"
    four = ":four:"
    five = ":five:"
    six = ":six:"
    seven = ":seven:"
    eight = ":eight:"
    nine = ":nine:"

    listeSayi = ["sıfır", one, two, three, four, five, six, seven, eight, nine]

    try:
        file = open(f"{ctx.message.author.id}.txt", "r")
        bilgi2 = file.read()
        bilgi2 = bilgi2.split("//")
        para2 = int(bilgi2[1])
        para2 -= coin
        tarih = bilgi2[2]
        job = bilgi2[3]
        print(para2)
        file.close()

        if para2 >= 0 and 1 <= secilen_sayi <= 9:

            gold = Bot.get_emoji(862765253431132160)
            embed = discord.Embed(title="SAYI OYUNU", url="https://www.fdskjhfısfdsfs.com",
                                  description=f"```SAYI AÇILIYOR.```")
            embed.add_field(name="**Harcanan Miktar**", value=f"-{coin} {gold}", inline=False)
            embed.add_field(name=f"**SEÇİLEN SAYI {secilen_sayi} **",
                            value=f"{listeSayi[1]} {listeSayi[2]} {listeSayi[3]}\n{listeSayi[4]} {listeSayi[5]} {listeSayi[6]}\n{listeSayi[7]} {listeSayi[8]} {listeSayi[9]}")
            embed.set_thumbnail(url=MHT)
            embed.set_author(name=f"{ctx.message.author.name} tarafından oluşturuldu",
                             icon_url=ctx.message.author.avatar_url)
            msg = await ctx.send(embed=embed)
            await asyncio.sleep(1)
            embed = discord.Embed(title="SAYI OYUNU", url="https://www.fdskjhfısfdsfs.com",
                                  description=f"```SAYI AÇILIYOR. .```")
            embed.add_field(name="**Harcanan Miktar**", value=f"-{coin} {gold}", inline=False)
            embed.add_field(name=f"**SEÇİLEN SAYI {secilen_sayi} **",
                            value=f"{listeSayi[1]} {listeSayi[2]} {listeSayi[3]}\n{listeSayi[4]} {listeSayi[5]} {listeSayi[6]}\n{listeSayi[7]} {listeSayi[8]} {listeSayi[9]}")
            embed.set_thumbnail(url=MHT)
            embed.set_author(name=f"{ctx.message.author.name} tarafından oluşturuldu",
                             icon_url=ctx.message.author.avatar_url)
            await msg.edit(embed=embed)

            listeSayi.remove(listeSayi[secilen_sayi])

            listeMiktararti = ["+ x1", "+ x2", "+ x3", "+ x4", "+ x5", "+ x6", "+ x7", "+ x8", "+ x9", "+ x10", "+ x25",
                               "+ x50",
                               "+ x75", "+ x100"]
            listeMiktareksi = ["- x1", "- x2", "- x3", "- x4", "- x5", "- x6", "- x7", "- x8", "- x9", "- x10", "- x25",
                               "- x50",
                               "- x75", "- x100"]

            listeMiktar50 = ["+ x1.5", "+ x2", "+ x1.5", "- x1.5", "- x2", ]
            listeMiktar30 = ["+ x3", "+ x4", "+ x5", "- x3", "- x4", "- x5", ]
            listeMiktar15 = ["+ x6", "+ x7", "+ x8", "- x6", "- x7", "- x8", ]
            listeMiktar5 = ["+ x9", "+ x10", "+ x25", "- x9", "- x10", "- x25", ]
            listeMiktar1 = ["+ x50", "+ x75", "+ x100", ]

            lucky = random.randint(1, 101)
            if 0 < lucky <= 50:
                print(listeMiktar50)
                luckySecilen = random.choice(listeMiktar50)
                luckySecilen = f"**{luckySecilen}**"
                listeSayi.insert(secilen_sayi, luckySecilen)

            elif 50 < lucky <= 80:
                print(listeMiktar30)
                luckySecilen = random.choice(listeMiktar30)
                luckySecilen = f"**{luckySecilen}**"
                listeSayi.insert(secilen_sayi, luckySecilen)

            elif 80 < lucky <= 95:
                print(listeMiktar15)
                luckySecilen = random.choice(listeMiktar15)
                luckySecilen = f"**{luckySecilen}**"
                listeSayi.insert(secilen_sayi, luckySecilen)

            elif 95 < lucky <= 100:
                print(listeMiktar5)
                luckySecilen = random.choice(listeMiktar5)
                luckySecilen = f"**{luckySecilen}**"
                listeSayi.insert(secilen_sayi, luckySecilen)

            elif lucky == 101:
                print(listeMiktar1)
                luckySecilen = random.choice(listeMiktar1)
                luckySecilen = f"**{luckySecilen}**"
                listeSayi.insert(secilen_sayi, luckySecilen)
            await asyncio.sleep(1)
            gold = Bot.get_emoji(862765253431132160)
            embed = discord.Embed(title="SAYI OYUNU", url="https://www.fdskjhfısfdsfs.com",
                                  description=f"```SAYI AÇILDI```")
            embed.add_field(name="**Harcanan Miktar**", value=f"-{coin} {gold}", inline=False)
            embed.add_field(name=f"**SEÇİLEN SAYI {secilen_sayi} **",
                            value=f"{listeSayi[1]} {listeSayi[2]} {listeSayi[3]}\n{listeSayi[4]} {listeSayi[5]} {listeSayi[6]}\n{listeSayi[7]} {listeSayi[8]} {listeSayi[9]}")
            embed.set_thumbnail(url=MHT)
            embed.set_author(name=f"{ctx.message.author.name} tarafından oluşturuldu",
                             icon_url=ctx.message.author.avatar_url)
            await msg.edit(embed=embed)
            print(luckySecilen)
            if luckySecilen.startswith("**+"):
                luckyListe = luckySecilen.split("x")
                print(luckyListe)
                carpan = luckyListe[-1]

                carpan = float(carpan[:-2])
                coin2 = coin * carpan
                coin2 = int(coin2)
                para2 += coin2

                file = open(f"{ctx.message.author.id}.txt", "w")
                file.write(f"{ctx.message.author.mention}//{para2}//{bilgi2[2]}//{job}")
                file.close()

                gold = Bot.get_emoji(862765253431132160)
                embed = discord.Embed(title="SAYI OYUNU", url="https://www.fdskjhfısfdsfs.com",
                                      description=f"```SAYI AÇILDI```")
                embed.add_field(name="**Harcanan Miktar**", value=f"-{coin} {gold}", inline=False)
                embed.add_field(name=f"**SEÇİLEN SAYI {secilen_sayi} **",
                                value=f"{listeSayi[1]} {listeSayi[2]} {listeSayi[3]}\n{listeSayi[4]} {listeSayi[5]} {listeSayi[6]}\n{listeSayi[7]} {listeSayi[8]} {listeSayi[9]}")
                embed.add_field(name=f"**Tebrikler KAZANDIN!**", value=f"+{coin2} {gold}", inline=False)

                file = open(f"{ctx.message.author.id}.txt", "r")
                bilgi2 = file.read()
                bilgi2 = bilgi2.split("//")
                para2 = int(bilgi2[1])


                embed.add_field(name=f"**Güncel Bakiyen**", value=f"{para2} {gold}", inline=False)
                file.close()
                embed.set_thumbnail(url=MHT)
                embed.set_author(name=f"{ctx.message.author.name} tarafından oluşturuldu",
                                 icon_url=ctx.message.author.avatar_url)
                await msg.edit(embed=embed)

            elif luckySecilen.startswith("**-"):
                luckyListe = luckySecilen.split("x")
                carpan = luckyListe[-1]
                carpan = float(carpan[:-2])
                coin2 = coin * carpan
                coin2 = int(coin2)
                para2 -= coin2
                print(para2)
                print(f"-{coin2}")
                if para2 <= 0:
                    para2 = 0
                print(para2)
                print(f"+{coin2}")

                file = open(f"{ctx.message.author.id}.txt", "w")
                file.write(f"{ctx.message.author.mention}//{para2}//{bilgi2[2]}//{job}")
                file.close()

                gold = Bot.get_emoji(862765253431132160)
                embed = discord.Embed(title="SAYI OYUNU", url="https://www.fdskjhfısfdsfs.com",
                                      description=f"```SAYI AÇILDI```")
                embed.add_field(name="**Harcanan Miktar**", value=f"-{coin} {gold}", inline=False)
                embed.add_field(name=f"**SEÇİLEN SAYI {secilen_sayi} **",
                                value=f"{listeSayi[1]} {listeSayi[2]} {listeSayi[3]}\n{listeSayi[4]} {listeSayi[5]} {listeSayi[6]}\n{listeSayi[7]} {listeSayi[8]} {listeSayi[9]}")
                embed.add_field(name=f"**Üzgünüm KAYBETTİN!**", value=f"-{coin2} {gold}", inline=False)

                file = open(f"{ctx.message.author.id}.txt", "r")
                bilgi2 = file.read()
                bilgi2 = bilgi2.split("//")
                para2 = int(bilgi2[1])

                embed.add_field(name=f"**Güncel Bakiyen**", value=f"{para2} {gold}", inline=False)
                file.close()

                embed.set_thumbnail(url=MHT)
                embed.set_author(name=f"{ctx.message.author.name} tarafından oluşturuldu",
                                 icon_url=ctx.message.author.avatar_url)
                await msg.edit(embed=embed)
        else:
            embed3 = discord.Embed(title="Yeterli bakiyeniz bulunmamakta\nya da\nseçtiğiniz sayı 0-10 arasında değil.")
            embed3.set_thumbnail(url=MHT)
            await ctx.send(embed=embed3)


    except(FileNotFoundError):
        embed2 = discord.Embed(
            title=f"Kullanıcı bulunamadı.",
            description=f"Henüz bir hesabın yok {ctx.message.author.mention}. Lütfen   ' -kayıt  ' komutu ile hesap oluştur.",
            url="https://www.com")
        embed2.set_thumbnail(url=MHT)
        embed2.set_author(name=f"{ctx.message.author.name} tarafından oluşturuldu",
                          icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed2)
        await ctx.send(f"{ctx.message.author.mention}")


bayraklar = [
    'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Flag_of_the_Republic_of_Abkhazia.svg/160px-Flag_of_the_Republic_of_Abkhazia.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Afghanistan.svg/120px-Flag_of_Afghanistan.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/134px-Flag_of_Germany.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Flag_of_the_United_States.svg/152px-Flag_of_the_United_States.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Flag_of_Andorra.svg/114px-Flag_of_Andorra.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/Flag_of_Angola.svg/120px-Flag_of_Angola.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Flag_of_Albania.svg/112px-Flag_of_Albania.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Flag_of_Antigua_and_Barbuda.svg/120px-Flag_of_Antigua_and_Barbuda.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Flag_of_Argentina.svg/128px-Flag_of_Argentina.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Flag_of_Australia.svg/160px-Flag_of_Australia.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Flag_of_Austria.svg/120px-Flag_of_Austria.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Flag_of_Azerbaijan.svg/160px-Flag_of_Azerbaijan.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flag_of_the_Bahamas.svg/160px-Flag_of_the_Bahamas.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/Flag_of_Bahrain.svg/134px-Flag_of_Bahrain.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Flag_of_Bangladesh.svg/134px-Flag_of_Bangladesh.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Flag_of_Barbados.svg/120px-Flag_of_Barbados.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/Flag_of_Belgium.svg/92px-Flag_of_Belgium.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Flag_of_Belize.svg/134px-Flag_of_Belize.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Flag_of_Benin.svg/120px-Flag_of_Benin.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Flag_of_Belarus.svg/160px-Flag_of_Belarus.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Flag_of_Bhutan.svg/120px-Flag_of_Bhutan.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Flag_of_the_United_Arab_Emirates.svg/160px-Flag_of_the_United_Arab_Emirates.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Flag_of_Bolivia.svg/118px-Flag_of_Bolivia.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Flag_of_the_United_Kingdom.svg/160px-Flag_of_the_United_Kingdom.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Flag_of_Bosnia_and_Herzegovina.svg/160px-Flag_of_Bosnia_and_Herzegovina.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_Botswana.svg/120px-Flag_of_Botswana.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Flag_of_Brazil.svg/114px-Flag_of_Brazil.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/Flag_of_Brunei.svg/160px-Flag_of_Brunei.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Bulgaria.svg/134px-Flag_of_Bulgaria.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Flag_of_Burkina_Faso.svg/120px-Flag_of_Burkina_Faso.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Flag_of_Burundi.svg/134px-Flag_of_Burundi.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Flag_of_Algeria.svg/120px-Flag_of_Algeria.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Flag_of_Djibouti.svg/120px-Flag_of_Djibouti.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Flag_of_the_Cook_Islands.svg/160px-Flag_of_the_Cook_Islands.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Flag_of_Chad.svg/120px-Flag_of_Chad.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Flag_of_the_Czech_Republic.svg/120px-Flag_of_the_Czech_Republic.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/120px-Flag_of_the_People%27s_Republic_of_China.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/Flag_of_Denmark.svg/106px-Flag_of_Denmark.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Flag_of_East_Timor.svg/160px-Flag_of_East_Timor.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Flag_of_Dominica.svg/160px-Flag_of_Dominica.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Flag_of_the_Dominican_Republic.svg/120px-Flag_of_the_Dominican_Republic.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Flag_of_Ecuador.svg/120px-Flag_of_Ecuador.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Flag_of_Equatorial_Guinea.svg/120px-Flag_of_Equatorial_Guinea.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Flag_of_El_Salvador.svg/142px-Flag_of_El_Salvador.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Flag_of_Indonesia.svg/120px-Flag_of_Indonesia.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Flag_of_Eritrea.svg/160px-Flag_of_Eritrea.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Flag_of_Armenia.svg/160px-Flag_of_Armenia.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Flag_of_Estonia.svg/126px-Flag_of_Estonia.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/7/71/Flag_of_Ethiopia.svg/160px-Flag_of_Ethiopia.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/Flag_of_Morocco.svg/120px-Flag_of_Morocco.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Fiji.svg/160px-Flag_of_Fiji.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Flag_of_C%C3%B4te_d%27Ivoire.svg/120px-Flag_of_C%C3%B4te_d%27Ivoire.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Flag_of_the_Philippines.svg/160px-Flag_of_the_Philippines.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/Flag_of_Palestine.svg/160px-Flag_of_Palestine.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Flag_of_Finland.svg/131px-Flag_of_Finland.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Flag_of_France.svg/120px-Flag_of_France.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Flag_of_Gabon.svg/107px-Flag_of_Gabon.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Flag_of_The_Gambia.svg/120px-Flag_of_The_Gambia.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Flag_of_Ghana.svg/120px-Flag_of_Ghana.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Flag_of_Guinea.svg/120px-Flag_of_Guinea.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Flag_of_Guinea-Bissau.svg/160px-Flag_of_Guinea-Bissau.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Flag_of_Grenada.svg/134px-Flag_of_Grenada.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Flag_of_Guatemala.svg/128px-Flag_of_Guatemala.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Flag_of_Guyana.svg/134px-Flag_of_Guyana.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Flag_of_South_Africa.svg/120px-Flag_of_South_Africa.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Flag_of_South_Korea.svg/120px-Flag_of_South_Korea.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Flag_of_South_Ossetia.svg/160px-Flag_of_South_Ossetia.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Flag_of_South_Sudan.svg/160px-Flag_of_South_Sudan.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Flag_of_Georgia.svg/120px-Flag_of_Georgia.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Flag_of_Haiti.svg/134px-Flag_of_Haiti.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Flag_of_Croatia.svg/160px-Flag_of_Croatia.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Flag_of_India.svg/120px-Flag_of_India.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/120px-Flag_of_the_Netherlands.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Flag_of_Honduras.svg/160px-Flag_of_Honduras.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Flag_of_Iraq.svg/120px-Flag_of_Iraq.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Flag_of_Iran.svg/140px-Flag_of_Iran.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Flag_of_Ireland.svg/160px-Flag_of_Ireland.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/120px-Flag_of_Spain.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Flag_of_Israel.svg/110px-Flag_of_Israel.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Flag_of_Sweden.svg/128px-Flag_of_Sweden.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Flag_of_Switzerland.svg/80px-Flag_of_Switzerland.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/120px-Flag_of_Italy.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/Flag_of_Iceland.svg/111px-Flag_of_Iceland.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Flag_of_Jamaica.svg/160px-Flag_of_Jamaica.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Flag_of_Japan.svg/120px-Flag_of_Japan.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Flag_of_Cambodia.svg/125px-Flag_of_Cambodia.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Flag_of_Cameroon.svg/120px-Flag_of_Cameroon.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Flag_of_Canada.svg/160px-Flag_of_Canada.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/Flag_of_Montenegro.svg/160px-Flag_of_Montenegro.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/Flag_of_Qatar.svg/204px-Flag_of_Qatar.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Flag_of_Kazakhstan.svg/160px-Flag_of_Kazakhstan.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Flag_of_Kenya.svg/120px-Flag_of_Kenya.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Flag_of_Cyprus.svg/120px-Flag_of_Cyprus.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Flag_of_Kyrgyzstan.svg/134px-Flag_of_Kyrgyzstan.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Flag_of_Kiribati.svg/160px-Flag_of_Kiribati.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Flag_of_Colombia.svg/120px-Flag_of_Colombia.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Flag_of_the_Comoros.svg/134px-Flag_of_the_Comoros.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_the_Republic_of_the_Congo.svg/120px-Flag_of_the_Republic_of_the_Congo.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Flag_of_the_Democratic_Republic_of_the_Congo.svg/107px-Flag_of_the_Democratic_Republic_of_the_Congo.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/Flag_of_Costa_Rica.svg/134px-Flag_of_Costa_Rica.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Flag_of_Kosovo.svg/112px-Flag_of_Kosovo.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Flag_of_Kuwait.svg/160px-Flag_of_Kuwait.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Flag_of_the_Turkish_Republic_of_Northern_Cyprus.svg/120px-Flag_of_the_Turkish_Republic_of_Northern_Cyprus.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Flag_of_North_Korea.svg/160px-Flag_of_North_Korea.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Flag_of_North_Macedonia.svg/160px-Flag_of_North_Macedonia.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Flag_of_Cuba.svg/160px-Flag_of_Cuba.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Flag_of_Laos.svg/120px-Flag_of_Laos.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Flag_of_Lesotho.svg/120px-Flag_of_Lesotho.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Flag_of_Latvia.svg/160px-Flag_of_Latvia.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Flag_of_Liberia.svg/152px-Flag_of_Liberia.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Flag_of_Libya.svg/160px-Flag_of_Libya.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Flag_of_Liechtenstein.svg/134px-Flag_of_Liechtenstein.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/Flag_of_Lithuania.svg/134px-Flag_of_Lithuania.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/Flag_of_Lebanon.svg/120px-Flag_of_Lebanon.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Flag_of_Luxembourg.svg/134px-Flag_of_Luxembourg.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Flag_of_Hungary.svg/160px-Flag_of_Hungary.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Flag_of_Madagascar.svg/120px-Flag_of_Madagascar.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Flag_of_Malawi.svg/120px-Flag_of_Malawi.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Flag_of_Maldives.svg/120px-Flag_of_Maldives.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Flag_of_Malaysia.svg/160px-Flag_of_Malaysia.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_Mali.svg/120px-Flag_of_Mali.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Flag_of_Malta.svg/120px-Flag_of_Malta.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Flag_of_the_Marshall_Islands.svg/152px-Flag_of_the_Marshall_Islands.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Flag_of_Mauritius.svg/120px-Flag_of_Mauritius.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/f/fc/Flag_of_Mexico.svg/140px-Flag_of_Mexico.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Flag_of_the_Federated_States_of_Micronesia.svg/152px-Flag_of_the_Federated_States_of_Micronesia.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Flag_of_Egypt.svg/120px-Flag_of_Egypt.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Flag_of_Mongolia.svg/160px-Flag_of_Mongolia.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Flag_of_Moldova.svg/160px-Flag_of_Moldova.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Flag_of_Monaco.svg/100px-Flag_of_Monaco.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Flag_of_Mauritania.svg/120px-Flag_of_Mauritania.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Flag_of_Mozambique.svg/120px-Flag_of_Mozambique.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Flag_of_Myanmar.svg/120px-Flag_of_Myanmar.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/Flag_of_Namibia.svg/120px-Flag_of_Namibia.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Flag_of_Nauru.svg/160px-Flag_of_Nauru.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Flag_of_Nepal.svg/66px-Flag_of_Nepal.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/Flag_of_Niger.svg/93px-Flag_of_Niger.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Flag_of_Nigeria.svg/160px-Flag_of_Nigeria.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Flag_of_Nicaragua.svg/134px-Flag_of_Nicaragua.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Flag_of_Niue.svg/160px-Flag_of_Niue.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Flag_of_Norway.svg/110px-Flag_of_Norway.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Flag_of_the_Central_African_Republic.svg/120px-Flag_of_the_Central_African_Republic.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Flag_of_Uzbekistan.svg/160px-Flag_of_Uzbekistan.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Flag_of_Pakistan.svg/120px-Flag_of_Pakistan.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Flag_of_Palau.svg/128px-Flag_of_Palau.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Flag_of_Panama.svg/120px-Flag_of_Panama.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Flag_of_Papua_New_Guinea.svg/107px-Flag_of_Papua_New_Guinea.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Flag_of_Paraguay.svg/146px-Flag_of_Paraguay.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Flag_of_Peru.svg/120px-Flag_of_Peru.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Flag_of_Poland.svg/128px-Flag_of_Poland.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/120px-Flag_of_Portugal.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Flag_of_Romania.svg/120px-Flag_of_Romania.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/Flag_of_Rwanda.svg/120px-Flag_of_Rwanda.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Flag_of_Russia.svg/120px-Flag_of_Russia.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Flag_of_Saint_Kitts_and_Nevis.svg/120px-Flag_of_Saint_Kitts_and_Nevis.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Flag_of_Saint_Lucia.svg/160px-Flag_of_Saint_Lucia.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Flag_of_Saint_Vincent_and_the_Grenadines.svg/120px-Flag_of_Saint_Vincent_and_the_Grenadines.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Flag_of_the_Sahrawi_Arab_Democratic_Republic.svg/160px-Flag_of_the_Sahrawi_Arab_Democratic_Republic.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Flag_of_Samoa.svg/160px-Flag_of_Samoa.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Flag_of_San_Marino.svg/107px-Flag_of_San_Marino.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Flag_of_Sao_Tome_and_Principe.svg/160px-Flag_of_Sao_Tome_and_Principe.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Flag_of_Senegal.svg/120px-Flag_of_Senegal.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/f/fc/Flag_of_Seychelles.svg/160px-Flag_of_Seychelles.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Flag_of_Serbia.svg/120px-Flag_of_Serbia.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/Flag_of_Sierra_Leone.svg/120px-Flag_of_Sierra_Leone.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Flag_of_Singapore.svg/120px-Flag_of_Singapore.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Flag_of_Slovakia.svg/120px-Flag_of_Slovakia.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Flag_of_Slovenia.svg/160px-Flag_of_Slovenia.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/Flag_of_the_Solomon_Islands.svg/160px-Flag_of_the_Solomon_Islands.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Flag_of_Somalia.svg/120px-Flag_of_Somalia.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/Flag_of_Sri_Lanka.svg/160px-Flag_of_Sri_Lanka.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Flag_of_Sudan.svg/160px-Flag_of_Sudan.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Flag_of_Suriname.svg/120px-Flag_of_Suriname.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Flag_of_Syria.svg/120px-Flag_of_Syria.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Flag_of_Saudi_Arabia.svg/120px-Flag_of_Saudi_Arabia.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Flag_of_Eswatini.svg/120px-Flag_of_Eswatini.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Flag_of_Chile.svg/120px-Flag_of_Chile.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Flag_of_Tajikistan.svg/160px-Flag_of_Tajikistan.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Flag_of_Tanzania.svg/120px-Flag_of_Tanzania.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Flag_of_Thailand.svg/120px-Flag_of_Thailand.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/Flag_of_the_Republic_of_China.svg/120px-Flag_of_the_Republic_of_China.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/6/68/Flag_of_Togo.svg/130px-Flag_of_Togo.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Tonga.svg/160px-Flag_of_Tonga.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/Flag_of_Trinidad_and_Tobago.svg/134px-Flag_of_Trinidad_and_Tobago.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/Flag_of_Tunisia.svg/120px-Flag_of_Tunisia.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Flag_of_Tuvalu.svg/160px-Flag_of_Tuvalu.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Flag_of_Turkey.svg/120px-Flag_of_Turkey.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Flag_of_Turkmenistan.svg/120px-Flag_of_Turkmenistan.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Flag_of_Uganda.svg/120px-Flag_of_Uganda.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Flag_of_Ukraine.svg/120px-Flag_of_Ukraine.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Flag_of_Oman.svg/160px-Flag_of_Oman.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Flag_of_Uruguay.svg/120px-Flag_of_Uruguay.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/Flag_of_Jordan.svg/160px-Flag_of_Jordan.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Flag_of_Vanuatu.svg/134px-Flag_of_Vanuatu.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/Flag_of_the_Vatican_City.svg/80px-Flag_of_the_Vatican_City.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Flag_of_Venezuela.svg/120px-Flag_of_Venezuela.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Flag_of_Vietnam.svg/120px-Flag_of_Vietnam.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Flag_of_Cape_Verde.svg/136px-Flag_of_Cape_Verde.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Flag_of_Yemen.svg/120px-Flag_of_Yemen.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Flag_of_New_Zealand.svg/160px-Flag_of_New_Zealand.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Greece.svg/120px-Flag_of_Greece.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Flag_of_Zambia.svg/120px-Flag_of_Zambia.svg.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Flag_of_Zimbabwe.svg/160px-Flag_of_Zimbabwe.svg.png']
bayrakIsimleri = ['Abhazya ', 'Afganistan', 'Almanya', 'Amerika Birleşik Devletleri', 'Andorra', 'Angola',
                  'Arnavutluk ', 'Antigua ve Barbuda', 'Arjantin', 'Avustralya', 'Avusturya', 'Azerbaycan', 'Bahamalar',
                  'Bahreyn', 'Bangladeş', 'Barbados', 'Belçika', 'Belize', 'Benin', 'Belarus', 'Bhutan',
                  'Birleşik Arap Emirlikleri', 'Bolivya', 'Birleşik Krallık', 'Bosna-Hersek', 'Botsvana', 'Brezilya',
                  'Brunei', 'Bulgaristan', 'Burkina Faso', 'Burundi', 'Cezayir', 'Cibuti', 'Cook Adaları', 'Çad',
                  'Çek Cumhuriyeti', 'Çin', 'Danimarka', 'Doğu Timor', 'Dominika', 'Dominik Cumhuriyeti', 'Ekvador',
                  'Ekvator Ginesi', 'El Salvador', 'Endonezya', 'Eritre', 'Ermenistan', 'Estonya', 'Etiyopya', 'Fas',
                  'Fiji', 'Fildişi Sahili', 'Filipinler', 'Filistin', 'Finlandiya', 'Fransa', 'Gabon', 'Gambiya',
                  'Gana', 'Gine', 'Gine-Bissau', 'Grenada', 'Guatemala', 'Guyana', 'Güney Afrika Cumhuriyeti',
                  'Güney Kore', 'Güney Osetya', 'Güney Sudan', 'Gürcistan', 'Haiti', 'Hırvatistan', 'Hindistan',
                  'Hollanda', 'Honduras', 'Irak', 'iran', 'irlanda', 'ispanya', 'israil', 'isveç', 'isviçre', 'italya',
                  'izlanda', 'Jamaika', 'Japonya', 'Kamboçya', 'Kamerun', 'Kanada', 'Karadağ', 'Katar', 'Kazakistan',
                  'Kenya', 'Kıbrıs Cumhuriyeti', 'Kırgızistan', 'Kiribati', 'Kolombiya', 'Komorlar',
                  'Kongo Cumhuriyeti', 'Kongo Demokratik Cumhuriyeti', 'Kosta Rika', 'Kosova', 'Kuveyt',
                  'Kuzey Kıbrıs Türk Cumhuriyeti', 'Kuzey Kore', 'Kuzey Makedonya', 'Küba', 'Laos', 'Lesotho',
                  'Letonya', 'Liberya', 'Libya', 'Lihtenştayn', 'Litvanya', 'Lübnan', 'Lüksemburg', 'Macaristan',
                  'Madagaskar', 'Malavi', 'Maldivler', 'Malezya', 'Mali', 'Malta', 'Marshall Adaları', 'Mauritius',
                  'Meksika', 'Mikronezya Federal Devletleri', 'Mısır', 'Moğolistan', 'Moldova', 'Monako', 'Moritanya',
                  'Mozambik', 'Myanmar', 'Namibya', 'Nauru', 'Nepal', 'Nijer', 'Nijerya', 'Nikaragua', 'Niue', 'Norveç',
                  'Orta Afrika Cumhuriyeti', 'Özbekistan', 'Pakistan', 'Palau', 'Panama', 'Papua Yeni Gine', 'Paraguay',
                  'Peru', 'Polonya', 'Portekiz', 'Romanya', 'Ruanda', 'Rusya', 'Saint Kitts ve Nevis', 'Saint Lucia',
                  'Saint Vincent ve Grenadinler', 'Sahra Demokratik Arap Cumhuriyeti', 'Samoa', 'San Marino',
                  'São Tomé ve Príncipe', 'Senegal', 'Seyşeller', 'Sırbistan', 'Sierra Leone', 'Singapur', 'Slovakya',
                  'Slovenya', 'Solomon Adaları', 'Somali', 'Sri Lanka', 'Sudan', 'Surinam', 'Suriye', 'Suudi Arabistan',
                  'Esvatini', 'Şili', 'Tacikistan', 'Tanzanya', 'Tayland', 'Tayvan', 'Togo', 'Tonga',
                  'Trinidad ve Tobago', 'Tunus', 'Tuvalu', 'Türkiye', 'Türkmenistan', 'Uganda', 'Ukrayna', 'Umman',
                  'Uruguay', 'Ürdün', 'Vanuatu', 'Vatikan', 'Venezuela', 'Vietnam', 'Yeşil Burun Adaları', 'Yemen',
                  'Yeni Zelanda', 'Yunanistan', 'Zambiya', 'Zimbabve']


@Bot.command(aliases=["bb"],brief="-help bb",description="Bayrak Bulma oyunu hakkındaki tüm bilgileri içerir.")
async def bayrakbulma(ctx):


    embed = discord.Embed(title="Ülke İsmini Bulun",url="https://www.com",colour=discord.Colour.from_rgb(255,23,45))
    embed.add_field(name="**Nasıl Oynanır ?**",value="-bboyna / -bbplay komutu ile oyuna başlayın ve Resimdeki Bayrağın adını mesaj olarak yazın.\n",inline=True)
    embed.add_field(name="**Nasıl çıkılır ?**",value="Bilemediğiniz takdirde çıkmak için başında - işareti __olmadan__ bb.bitir / bb.end yazarak oyunu sonlandırabilirsiniz.\n",inline=True)
    embed.add_field(name="**Yardım**",value="Bilemediğiniz bir bayrağın ismini öğrenmek isterseniz başında - işareti __olmadan__ bb.yardım/bb.help yazabilirsniz.",inline=True)
    embed.set_thumbnail(url = MHT)
    await ctx.send(embed=embed)

@Bot.command(aliases=["bboyna","bbplay"],brief="-help bboyna",description="Bayrak Bulma oyununu başlatır. oyun hakkında bilgi almak için -bayrakbulma komutunu yazınız.")
async def bayrakbulmaoyna(ctx):
    index = random.randint(0, 202)
    bayrak = bayraklar[index]
    bayrakisim = bayrakIsimleri[index]

    embed = discord.Embed(title="Ülke İsmini Bulun",
                          url="https://www.com",
                          colour=discord.Colour.from_rgb(255,23,45),
                          timestamp=datetime.utcnow(),
                          )
    embed.set_author(name=f"{ctx.message.author.name} tarafından oluşturuldu",
                     icon_url=ctx.message.author.avatar_url)
    embed.set_thumbnail(url=bayrak)
    await ctx.send(embed=embed)

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    msg = await Bot.wait_for("message", check=check)

    while True:
        print(msg.content)
        print(msg.content.lower().replace(" ", ""))
        print(bayrakisim.lower().replace(" ",""))
        if msg.content.lower().replace(" ","") == bayrakisim.lower().replace(" ",""):
            embed1 = discord.Embed(title="TEBRİKLER DOĞRU BİLDİN",
                                   description=f"**{bayrakisim}**",
                                   url="https://www.com",
                                   colour=discord.Colour.from_rgb(255,23,45),
                                   timestamp=datetime.utcnow())
            embed1.set_author(name=f"{ctx.message.author.name} tarafından oluşturuldu",
                             icon_url=ctx.message.author.avatar_url)
            embed1.set_thumbnail(url = bayrak)
            await ctx.send(embed=embed1)
            break
        elif msg.content == "bb.yardım" or msg.content == "bb.help":
            embed2 = discord.Embed(title=f"**{bayrakisim}**",
                                   description=f"Tekrar oynamak için -bboyna",
                                   colour=discord.Colour.from_rgb(255, 23, 45),
                                   timestamp=datetime.utcnow())
            embed2.set_author(name=f"{ctx.message.author.name} tarafından oluşturuldu",
                             icon_url=ctx.message.author.avatar_url)
            embed2.set_thumbnail(url=bayrak)
            await ctx.send(embed=embed2)
            break

        elif msg.content == "bb.bitir" or msg.content == "bb.end":
            embed3 = discord.Embed(title="OYUN BİTTİ",description="Tekrar oynamak için -bboyna",colour=discord.Colour.from_rgb(255, 23, 45),
                                   timestamp=datetime.now())
            embed3.set_thumbnail(url=MHT)
            embed3.set_author(name=f"{ctx.message.author.name} tarafından oluşturuldu",
                             icon_url=ctx.message.author.avatar_url)
            await ctx.send(embed=embed3)
            break
        else:
            await ctx.send("**YANLIŞ**  (bb.bitir veya bb.end yazarak oyunu sonlandırabilirsiniz.)")
            msg = await Bot.wait_for("message", check=check)
            continue


@Bot.command(aliases = ["üb"],brief="Bakımda...",description="Bakımda...")
@commands.has_role(905747509148786698)
async def ülkebilgi(ctx,ülke_isim):
    bayrak_resmi = ülke_isim.lower().split(" ")
    bayrak_resmi_2 = ""
    for x in bayrak_resmi:
        if x.startswith("i"):
            bayrak_resmi_2 += f"{x} "
        else:
            x = x.capitalize()
            bayrak_resmi_2 += f"{x} "

    print(bayrak_resmi)
    print(bayrak_resmi_2)

    index = bayrakIsimleri.index(bayrak_resmi_2[0:-1])
    print(index)
    bayrak = bayraklar[index]

    ülke_isim = ülke_isim.lower().replace(" ","_")
    print(ülke_isim)
    link = f"https://tr.wikipedia.org/wiki/{ülke_isim}"
    r = requests.get(f"https://tr.wikipedia.org/wiki/{ülke_isim}")
    soup = BeautifulSoup(r.content, "html.parser")

    a1 = soup.find("p").text
    embed = discord.Embed(title=f"{ülke_isim.upper().replace('_',' ')}",description=f"```{a1}```",url=f"{link}")
    embed.set_thumbnail(url = bayrak)
    await ctx.send(embed=embed)

@Bot.command(aliases=["sb"],brief="-help sayıbulma",description="1-100 arası sayı tutar. sayı girerek bulmaya çalışın.")
async def sayıbulma(ctx):
    sayi1 = 1
    sayi2 = 100
    sayi = random.randint(sayi1,sayi2)
    sayaç = 0

    await ctx.send(f"{sayi1} - {sayi2} arasında birsayı tuttu.")
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    msg = await Bot.wait_for("message", check=check, timeout=90)
    while True:

        try:
            msg.content = int(msg.content)
            if msg.content == 0:
                await ctx.send("tur bitti")
                break
            if msg.content == sayi:
                sayaç += 1

                file = open("sayıbulma_lidertablosu.txt","a")
                name = ctx.author.name
                file.writelines(f"\nISIM :  {name}  |   REKOR : {sayaç}")



                await ctx.send(f"BULDUN {sayi}     {sayaç} kere")
                break
            elif msg.content < sayi:
                await ctx.send("daha yukarı")
                sayaç += 1
                msg = await Bot.wait_for("message", check=check)
            elif msg.content > sayi:
                await ctx.send("daha aşağı")
                sayaç += 1
                msg = await Bot.wait_for("message", check=check)

        except:
            msg = await Bot.wait_for("message", check=check)
            continue



@Bot.command(brief="Bu bir test komutudur.Kullanılmaz.",description="Bu bir test komutudur.Kullanılmaz.")
@commands.has_role(905747509148786698)
async def test1(ctx):
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    msg = await Bot.wait_for("message", check=check)
    await msg.delete()
    message = await ctx.channel.send(f"{msg.content}")
    while True:
        msg = await Bot.wait_for("message", check=check)

        if msg.content == "bitir":
            break
        else:
            await msg.delete()
            await message.edit(content=f"{msg.content}")
@Bot.command(brief="-help meslekler",description="Seçebilceğiniz Meslekleri ve Mesleğe sahip olmak için ne kadar Coin'e ihtiyacınız olduğunu gösterir.")
async def meslekler(ctx):

    meslek_listesi = ["CEO Ozan Korfalı","Cerrah 250.000","Diş Hekimi 190.000","Bilgisayar Mühendisi 150.000","Avukat 60.000","Polis 25.000","İtfaye Eri 25.000","Memur 10.000","Astronot Jeff Bezos 200.000.000.000",]
    msg = ""
    count = 0
    gold = Bot.get_emoji(862765253431132160)
    for x in meslek_listesi:
        count += 1

        msg +=f"{count}- {x}   {gold}\n"
    embed = discord.Embed(title="Meslekler",url="https://www091jeımd1.com",description=f"{msg}\n\n**Meslek seçimi için -meslek_seç (meslek numarası)**")
    embed.set_author(name=f"{ctx.message.author.name} tarafından oluşturuldu")
    embed.set_thumbnail(url=MHT)
    await ctx.send(embed=embed)
@Bot.command(aliases=["meslek_seç"],brief="-help meslek_seç",description="-meslekler komutunda gösterilen meslekleri başlarındaki numaralar ile seçmenize yarar.\n\nÖrnek kullanım:\n\n-meslek_seç <seçilen meslek numarası>")
async def meslek_sec(ctx,arg1):
    try:
        file = open(f"{ctx.message.author.id}.txt", "r")
        bilgi2 = file.read()
        bilgi2 = bilgi2.split("//")
        para2 = int(bilgi2[1])
        tarih = bilgi2[2]
        print(para2)
        job = bilgi2[3]
        file.close()
        id = ctx.message.author.id
        mention = ctx.message.author.mention
        arg1 = int(arg1)
        if job == str(arg1):
            embed = discord.Embed(title=f"Kendi Mesleğinizi Tekrardan Seçemezsiniz\n\nGüncel Meslek : {meslek_adi(job)}")
            embed.set_thumbnail(url=MHT)
            await ctx.send(embed=embed)
        else:
            sonuc = meslek_secim_fonksiyonu(arg1,id,mention,para2,tarih)
            print(sonuc)

            embed = discord.Embed(title=sonuc)
            embed.set_thumbnail(url=MHT)
            await ctx.send(embed=embed)


    except(FileNotFoundError):
        embed2 = discord.Embed(
            title=f"Kullanıcı bulunamadı.",
            description=f"Henüz bir hesabın yok {ctx.message.author.mention}. Lütfen   ' -kayıt  ' komutu ile hesap oluştur.",
            url="https://www.com")
        embed2.set_thumbnail(url=MHT)
        embed2.set_author(name=f"{ctx.message.author.name} tarafından oluşturuldu",
                          icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed2)
        await ctx.send(f"{ctx.message.author.mention}")



@Bot.command(brief="-help meslek_yap",description="Mesleğiniz ile ilgili bir iş yapmanızı sağlar.")
async def meslek_yap(ctx):

    embed = discord.Embed(title="şu anda bu işlemi yapamıyoruz dışardayız...",colour=discord.Colour.from_rgb(0, 0, 0))
    msg = await ctx.send(embed=embed)

    count = 0
    while True:
        count += 1
        if count > 5:
            break
        else:
            await asyncio.sleep(delay=1)

            saat = datetime.now()
            saat = saat.strftime("%H:%M:%S")
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)

            embed = discord.Embed(title="şu anda bu işlemi yapamıyoruz dışardayız...",colour=discord.Colour.from_rgb(r, g, b),description=f"\n\n {saat}")
            await msg.edit(embed=embed)

@Bot.command(brief="-help merak",description="discord ücerindeki herhangi birinin profil fotoğrafını, adını, id'sini, discord hesabının oluşturulma tarihini size gösterir.\n\n Örnek Kullanım:\n-merak 343051107788128256\n")
async def merak(ctx,id):
    user = await Bot.fetch_user(id)

    isim = user.name
    id = user.id
    hesap_tarihi = user.created_at
    avatar = user.avatar_url

    embed = discord.Embed(title="**Bilgiler**",description=f"```isim :  {isim} ```\n```id : {id}```\n``` hesap oluşturulma tarihi : {hesap_tarihi}```",colour=discord.Colour.from_rgb(0, 0, 0))
    embed.set_author(name=isim,icon_url=avatar)
    embed.set_image(url=avatar)
    embed.set_thumbnail(url=MHT)

    await ctx.send(embed=embed)



@Bot.command(brief="-help hayvan",description="Hayvan Yarış oyununun nasıl oynanıcağı hakkında bilgi verir ve oyun içeriğinden bahseder.")
async def hayvan(ctx):
    kermit = Bot.get_emoji(906295701636513883)
    hayvan_listesi = [":tiger2:", ":leopard:", ":elephant:", ":mammoth:", ":bison:", ":hippopotamus:",
                      ":dromedary_camel:", ":camel:", ":giraffe:", ":kangaroo:", ":ox:", ":cow2:", ":racehorse:",
                      ":pig2:", ":ram:", ":sheep:", ":llama:", ":goat:", ":dog2:", ":poodle:", ":cat2:", ":black_cat:",
                      ":rooster:", ":rabbit2:", ":chipmunk:", ":rat:", ":mouse2:", ":beaver:",kermit]
    cumle=""
    for x in hayvan_listesi:
        cumle+=f"{x} "

    embed = discord.Embed(title="**Hayvan Yarışı Oyunu**",description="Hayvan yarışı oynamak için : \n**-hayvango** <**seçiceğiniz hayvanın numarası (1-4)**> <**hayvan'a yatırılacak coin**>",url="https://www.com",colour=discord.Colour.from_rgb(175,30,175))
    embed.add_field(name="**__Hayvanlar__**",value="```1- Hayvan (türü rastgele seçilir)\n2- Hayvan (türü rastgele seçilir)\n3- Hayvan (türü rastgele seçilir)\n4- Hayvan (türü rastgele seçilir)```",inline=True)
    embed.add_field(name="**__Hayvan Havuzu__**",value=f"{cumle}",inline=True)
    embed.set_thumbnail(url=MHT)
    await ctx.send(embed=embed)


@Bot.command(aliases = ["hg"],brief="-help hayvango",description="Bir şans oyunudur.Hayvan Yarış oyununu başlatır.Kazanırsanız yatırdığınız miktarın 4 katını kazanırsınız (Net Kazanç 3 Kat). Oyunun aynı kanal üzerinde aynı anda 1 kez oynanması daha uygundur. Oyun hakkındaki bilgileri öğrenmek için -hayvan komutunu giriniz.\n\nÖrnek Kullanım:\n-hayvango <secilen hayvan sıra numarası (1-4)> <yatırılacak Coin miktarı>\n")
async def hayvango(ctx,arg1,arg2):
    kazanma_durumu = ""
    serit = Bot.get_emoji(906247801489473558)
    gold = Bot.get_emoji(862765253431132160)
    kermit = Bot.get_emoji(906295701636513883)

    try:
        file = open(f"{ctx.message.author.id}.txt", "r")
        bilgi2 = file.read()
        bilgi2 = bilgi2.split("//")
        para2 = int(bilgi2[1])
        tarih = bilgi2[2]
        job = bilgi2[3]
        file.close()

        at_secimi = int(arg1)
        coin_secimi = int(arg2)
        if at_secimi > 4 or at_secimi < 1 or para2 - coin_secimi < 0:
            embedHata=discord.Embed(title="**HATA**",description="**__Hatalı Hayvan Seçimi veya Yetersiz Coin !__**\n nasıl oynayacağınızı öğrenmek için lütfen\n **-hayvan** komutunu yazın.",colour=discord.Colour.from_rgb(255,5,5),url="https://www.com")
            embedHata.set_thumbnail(url=MHT)
            await ctx.send(embed=embedHata)




        else:

            para2 -= coin_secimi

            pist_karesi = ":red_square:"
            pist_karesi_mavi = ":blue_square:"
            pist_karesi_sari = ":yellow_square:"
            pist_karesi_yesil = ":green_square:"
            at = ":horse_racing:"
            hayvan_listesi=[kermit,":tiger2:",":leopard:",":elephant:",":mammoth:",":bison:",":hippopotamus:",":dromedary_camel:",":camel:",":giraffe:",":kangaroo:",":ox:",":cow2:",":racehorse:",":pig2:",":ram:",":sheep:",":llama:",":goat:",":dog2:",":poodle:",":cat2:",":black_cat:",":rooster:",":rabbit2:",":chipmunk:",":rat:",":mouse2:",":beaver:"]

            hayvan_secimi1 = random.choice(hayvan_listesi)
            hayvan_listesi.remove(hayvan_secimi1)

            hayvan_secimi2 = random.choice(hayvan_listesi)
            hayvan_listesi.remove(hayvan_secimi2)

            hayvan_secimi3 = random.choice(hayvan_listesi)
            hayvan_listesi.remove(hayvan_secimi3)

            hayvan_secimi4 = random.choice(hayvan_listesi)
            hayvan_listesi.remove(hayvan_secimi4)






            pist =  [pist_karesi, pist_karesi, pist_karesi, pist_karesi, pist_karesi, pist_karesi, pist_karesi, pist_karesi, pist_karesi, pist_karesi, pist_karesi, pist_karesi, pist_karesi, pist_karesi,pist_karesi,pist_karesi,pist_karesi,pist_karesi,pist_karesi,pist_karesi,pist_karesi,pist_karesi,pist_karesi, hayvan_secimi1]
            pist2 = [pist_karesi_mavi, pist_karesi_mavi, pist_karesi_mavi, pist_karesi_mavi, pist_karesi_mavi, pist_karesi_mavi, pist_karesi_mavi, pist_karesi_mavi, pist_karesi_mavi, pist_karesi_mavi, pist_karesi_mavi, pist_karesi_mavi, pist_karesi_mavi, pist_karesi_mavi, pist_karesi_mavi,pist_karesi_mavi,pist_karesi_mavi,pist_karesi_mavi,pist_karesi_mavi,pist_karesi_mavi,pist_karesi_mavi,pist_karesi_mavi,pist_karesi_mavi,hayvan_secimi2]
            pist3 = [pist_karesi_sari, pist_karesi_sari, pist_karesi_sari, pist_karesi_sari, pist_karesi_sari, pist_karesi_sari, pist_karesi_sari, pist_karesi_sari, pist_karesi_sari, pist_karesi_sari, pist_karesi_sari, pist_karesi_sari, pist_karesi_sari, pist_karesi_sari,pist_karesi_sari,pist_karesi_sari,pist_karesi_sari,pist_karesi_sari,pist_karesi_sari,pist_karesi_sari,pist_karesi_sari,pist_karesi_sari,pist_karesi_sari, hayvan_secimi3]
            pist4 = [pist_karesi_yesil, pist_karesi_yesil, pist_karesi_yesil, pist_karesi_yesil, pist_karesi_yesil, pist_karesi_yesil, pist_karesi_yesil, pist_karesi_yesil, pist_karesi_yesil, pist_karesi_yesil, pist_karesi_yesil, pist_karesi_yesil, pist_karesi_yesil, pist_karesi_yesil,pist_karesi_yesil,pist_karesi_yesil,pist_karesi_yesil,pist_karesi_yesil,pist_karesi_yesil,pist_karesi_yesil,pist_karesi_yesil,pist_karesi_yesil,pist_karesi_yesil, hayvan_secimi4]

            cumle = ""
            for x in pist:
                cumle += f"{x}"
            cumle += f"\n"

            for x in pist2:
                cumle += f"{x}"
            cumle += f"\n"

            for x in pist3:
                cumle += f"{x}"
            cumle += f"\n"                                                           #---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   \n

            for x in pist4:
                cumle += f"{x}"
            cumle += "\n"

            if int(arg1) == 1:
                secimin = f"Seçimin -> {hayvan_secimi1}"
            if int(arg1) == 2:
                secimin = f"Seçimin -> {hayvan_secimi2}"
            if int(arg1) == 3:
                secimin = f"Seçimin -> {hayvan_secimi3}"
            if int(arg1) == 4:
                secimin = f"Seçimin -> {hayvan_secimi4}"
            msg = await ctx.send(f"{secimin}\n\n{cumle}")
            pist_index_len = len(pist)
            pist_index_len2 = len(pist2)
            pist_index_len3 = len(pist2)
            pist_index_len4 = len(pist2)

            sonuc = ""

            while True:


                await asyncio.sleep(delay=0.8)
                if pist_index_len <= 1:
                    sonuc += f"{hayvan_secimi1} "
                    if at_secimi == 1:
                        para2 += coin_secimi*4
                        kazanma_durumu = "kazandı"


                if pist_index_len2 <= 1:
                    sonuc += f"{hayvan_secimi2} "
                    if at_secimi == 2:
                        para2 += coin_secimi*4
                        kazanma_durumu = "kazandı"


                if pist_index_len3 <= 1:
                    sonuc += f"{hayvan_secimi3} "
                    if at_secimi == 3:
                        para2 += coin_secimi*4
                        kazanma_durumu = "kazandı"


                if pist_index_len4 <= 1:
                    sonuc += f"{hayvan_secimi4} "
                    if at_secimi == 4:
                        para2 += coin_secimi*4
                        kazanma_durumu = "kazandı"

                if pist_index_len <= 1 or pist_index_len2 <= 1 or pist_index_len3 <= 1 or pist_index_len4 <= 1:
                    break
                else:
                    pist_index_len -= 1
                    pist_index_len2 -= 1
                    pist_index_len3 -= 1
                    pist_index_len4 -= 1
                    hiz1 = random.randint(1, 3)
                    hiz2 = random.randint(1, 3)
                    hiz3 = random.randint(1, 3)
                    hiz4 = random.randint(1, 3)

                    if hiz1 == 1:

                        pist[pist_index_len] = pist_karesi
                        pist[pist_index_len - 1] = hayvan_secimi1
                    if hiz1 == 2:
                        if pist_index_len - 2 <=0:
                            pist[pist_index_len] = pist_karesi
                            pist[pist_index_len - 1] = pist_karesi
                            pist[0] = hayvan_secimi1
                            pist_index_len -= 1
                        else:

                            pist[pist_index_len] = pist_karesi
                            pist[pist_index_len -1] = pist_karesi
                            pist[pist_index_len - 2] = hayvan_secimi1

                            pist_index_len -= 1
                    if hiz1 == 3:
                        if pist_index_len - 3 <= 0:
                            pist[pist_index_len] = pist_karesi
                            pist[pist_index_len - 1] = pist_karesi
                            pist[pist_index_len - 2] = pist_karesi
                            pist[0] = hayvan_secimi1
                            pist_index_len -= 2
                        else:
                            pist[pist_index_len] = pist_karesi
                            pist[pist_index_len - 1] = pist_karesi
                            pist[pist_index_len - 2] = pist_karesi
                            pist[pist_index_len - 3] = hayvan_secimi1

                            pist_index_len -= 2


                    if hiz2 == 1:

                        pist2[pist_index_len2] = pist_karesi_mavi
                        pist2[pist_index_len2 - 1] = hayvan_secimi2

                    if hiz2 == 2:
                        if pist_index_len2 - 2 <= 0:
                            pist2[pist_index_len2] = pist_karesi_mavi
                            pist2[pist_index_len2 -1] = pist_karesi_mavi
                            pist2[0] = hayvan_secimi2

                            pist_index_len2 -= 1
                        else:
                            pist2[pist_index_len2] = pist_karesi_mavi
                            pist2[pist_index_len2 - 1] = pist_karesi_mavi
                            pist2[pist_index_len2 - 2] = hayvan_secimi2

                            pist_index_len2 -= 1
                    if hiz2 == 3:
                        if pist_index_len2 - 3 <= 0:
                            pist2[pist_index_len2] = pist_karesi_mavi
                            pist2[pist_index_len2 - 1] = pist_karesi_mavi
                            pist2[pist_index_len2 - 2] = pist_karesi_mavi
                            pist2[0] = hayvan_secimi2

                            pist_index_len2 -= 2
                        else:
                            pist2[pist_index_len2] = pist_karesi_mavi
                            pist2[pist_index_len2 - 1] = pist_karesi_mavi
                            pist2[pist_index_len2 - 2] = pist_karesi_mavi
                            pist2[pist_index_len2 - 3] = hayvan_secimi2

                            pist_index_len2 -= 2


                    if hiz3 == 1:
                        pist3[pist_index_len3] = pist_karesi_sari
                        pist3[pist_index_len3 - 1] = hayvan_secimi3

                    if hiz3 == 2:
                        if pist_index_len3 - 2 <= 0:
                            pist3[pist_index_len3] = pist_karesi_sari
                            pist3[pist_index_len3 -1] = pist_karesi_sari
                            pist3[0] = hayvan_secimi3

                            pist_index_len3 -= 1
                        else:
                            pist3[pist_index_len3] = pist_karesi_sari
                            pist3[pist_index_len3 - 1] = pist_karesi_sari
                            pist3[pist_index_len3 - 2] = hayvan_secimi3

                            pist_index_len3 -= 1
                    if hiz3 == 3:
                        if pist_index_len3 - 3 <= 0:
                            pist3[pist_index_len3] = pist_karesi_sari
                            pist3[pist_index_len3 - 1] = pist_karesi_sari
                            pist3[pist_index_len3 - 2] = pist_karesi_sari
                            pist3[0] = hayvan_secimi3

                            pist_index_len3 -= 2
                        else:
                            pist3[pist_index_len3] = pist_karesi_sari
                            pist3[pist_index_len3 - 1] = pist_karesi_sari
                            pist3[pist_index_len3 - 2] = pist_karesi_sari
                            pist3[pist_index_len3 - 3] = hayvan_secimi3

                            pist_index_len3 -= 2


                    if hiz4 == 1:


                        pist4[pist_index_len4] = pist_karesi_yesil
                        pist4[pist_index_len4 - 1] = hayvan_secimi4

                    if hiz4 == 2:
                        if pist_index_len4 - 2 <= 0:

                            pist4[pist_index_len4] = pist_karesi_yesil
                            pist4[pist_index_len4 -1] = pist_karesi_yesil
                            pist4[0] = hayvan_secimi4

                            pist_index_len4 -= 1
                        else:
                            pist4[pist_index_len4] = pist_karesi_yesil
                            pist4[pist_index_len4 - 1] = pist_karesi_yesil
                            pist4[pist_index_len4 - 2] = hayvan_secimi4

                            pist_index_len4 -= 1
                    if hiz4 == 3:
                        if pist_index_len4 - 3 <= 0:
                            pist4[pist_index_len4] = pist_karesi_yesil
                            pist4[pist_index_len4 - 1] = pist_karesi_yesil
                            pist4[pist_index_len4 - 2] = pist_karesi_yesil
                            pist4[0] = hayvan_secimi4

                            pist_index_len4 -= 2
                        else:
                            pist4[pist_index_len4] = pist_karesi_yesil
                            pist4[pist_index_len4 - 1] = pist_karesi_yesil
                            pist4[pist_index_len4 - 2] = pist_karesi_yesil
                            pist4[pist_index_len4 - 3] = hayvan_secimi4

                            pist_index_len4 -= 2



                    cumle = ""
                    for x in pist:
                        cumle += f"{x}"
                    cumle += "\n"

                    for x in pist2:
                        cumle += f"{x}"
                    cumle += "\n"

                    for x in pist3:
                        cumle += f"{x}"
                    cumle += "\n"

                    for x in pist4:
                        cumle += f"{x}"
                    cumle += "\n"

                    await msg.edit(content=f"{secimin}\n\n{cumle}")
            file = open(f"{ctx.message.author.id}.txt", "w")
            file.write(f"{ctx.message.author.mention}//{para2}//{bilgi2[2]}//{job}")
            file.close()

            if kazanma_durumu != "kazandı":

                embedSonuc = discord.Embed(title="**Kaybettin**",url="https://www.com",colour=discord.Colour.from_rgb(175,30,175))
                embedSonuc.set_thumbnail(url =ctx.message.author.avatar_url)
                embedSonuc.add_field(name=f"**__Kazanan Hayvanlar__**", value=f"{sonuc}",inline=True)
                embedSonuc.add_field(name=f"**__Yatırılan Coin__**{gold}",value=f"```{coin_secimi}```")
                embedSonuc.add_field(name=f"**__Kaybettin__**{gold}", value=f"```-{coin_secimi}```")
                embedSonuc.add_field(name=f"**__Güncel Hesap Bakiyesi__**{gold}{gold}{gold}", value=f"```{para2}```",inline=True)


                #sonuc_ciktisi =f"Kaybettin -{coin_secimi} {gold}\nGüncel Hesap Bakiyesi : {para2} {gold}{gold}{gold}"
            else:
                embedSonuc = discord.Embed(title="**Kazandın**", url="https://www.com",colour=discord.Colour.from_rgb(175,30,175))
                embedSonuc.set_thumbnail(url =ctx.message.author.avatar_url)
                embedSonuc.add_field(name=f"**__Kazanan Hayvanlar__**", value=f"{sonuc}",inline=True)
                embedSonuc.add_field(name=f"**__Yatırılan Coin__**{gold}", value=f"```{coin_secimi}```")
                embedSonuc.add_field(name=f"**__Kazandın__**{gold}", value=f"```+{coin_secimi*4}```")
                embedSonuc.add_field(name=f"**__Net Kazanç__**{gold}{gold}", value=f"```+{coin_secimi*4 - coin_secimi}```",inline=True)
                embedSonuc.add_field(name=f"**__Güncel Hesap Bakiyesi__**{gold}{gold}{gold}", value=f"```{para2}```",inline=True)




                #sonuc_ciktisi = f"KAZANDIN +{coin_secimi*4} {gold}\nNet Kazanç: {coin_secimi*4 - coin_secimi} {gold}{gold}\nGüncel Hesap Bakiyesi : {para2} {gold}{gold}{gold}"
            await msg.edit(content=f"{secimin}\n\n{cumle}")
            await ctx.send(embed=embedSonuc)




    except(FileNotFoundError):
        embed2 = discord.Embed(
            title=f"Kullanıcı bulunamadı.",
            description=f"Henüz bir hesabın yok {ctx.message.author.mention}. Lütfen   ' -kayıt  ' komutu ile hesap oluştur.",
            url="https://www.com")
        embed2.set_thumbnail(url=MHT)
        await ctx.send(embed=embed2)
        await ctx.send(f"{ctx.message.author.mention}")



@Bot.command(aliases=["asbilgi"],brief="-help asbilgi",description="Adam Asmaca oyununun nasıl oynanacağı hakkında bilgiler ve kuralları içerir.")
async def adam_asmaca_bilgi(ctx):
    embed= discord.Embed(title="Adam Asmaca Oyunu Hakkında",description="Oyun başladığında gireceğiniz her harf ve kelime tahmin sayılır\n\n***** Harf girerek kelime içindeki harfleri tahmin edebilirsiniz\n\n***** Kelime yazarak direkt olarak bulmanız gereken kelimeyi tahmin edebilirsiniz\n\n***** Her yanlış tahmin 1 hak götürür ve Adam Asılmaya başlar.Adam tamamen asıldığında oyunu kaybedersiniz.\n\n***** Tahminde bulunmadan bir mesaj yazmak isterseniz mesajınıza **.(nokta)** ile başlamanız gerekir.\n\n***** Oyundan, oyun bitmeden çıkmak isterseniz **exit** yazmanız yeterlidir gizli kelimenin ne olduğu gözükür ve oyun biter.\n\n\n\n**Oynamak için -as komutunu kullanın**",colour=discord.Colour.from_rgb(130,50,50))
    embed.set_thumbnail(url=MHT)
    await ctx.send(embed=embed)

@Bot.command(aliases=["as"],brief="-help as",description="Adam Asmaca oyununu başlatır. Oyunun nasıl oynanılacağı hakkında bilgi almak için -asbilgi komutunu kullanabilirsiniz.")
async def adam_asmaca(ctx):

    def check(msg):
        return msg.channel == ctx.channel and msg.author.id != 860251705395380244


    won = "https://cdn.discordapp.com/attachments/901157476932661308/906931149199249480/IMG_0061.jpg"
    lost ="https://cdn.discordapp.com/attachments/901157476932661308/906931149677428757/IMG_0062.jpg"
    terminated ="https://cdn.discordapp.com/attachments/901157476932661308/906931150918942790/IMG_0066.jpg"
    kazandin="https://cdn.discordapp.com/attachments/901157476932661308/906931150285582376/IMG_0064.jpg"
    kaybettin ="https://cdn.discordapp.com/attachments/901157476932661308/906931149975207976/IMG_0063.jpg"
    sonlandi="https://cdn.discordapp.com/attachments/901157476932661308/906931150562422814/IMG_0065.jpg"

    direk = "https://cdn.discordapp.com/attachments/901157476932661308/906682973003321354/unknown.png"
    kafa = "https://cdn.discordapp.com/attachments/901157476932661308/906693778935541770/unknown.png"
    govde = "https://cdn.discordapp.com/attachments/901157476932661308/906694199150276668/unknown.png"
    bacak1 ="https://cdn.discordapp.com/attachments/901157476932661308/906694613249712208/unknown.png"
    bacak2 ="https://cdn.discordapp.com/attachments/901157476932661308/906695710425116713/unknown.png"
    kol1 = "https://cdn.discordapp.com/attachments/901157476932661308/906696560652451890/unknown.png"
    son = "https://cdn.discordapp.com/attachments/901157476932661308/906697192717316106/unknown.png"
    control = 1
    kalan_hak = 6

    guncel_resim =direk

    liste_kategori =["doğa","uzay","okyanus","doğa","uzay","okyanus","doğa","uzay","okyanus","doğa","uzay","okyanus","developer"]
    kategori_secimi = random.choice(liste_kategori)
    if kategori_secimi == "doğa":
        kategori_ismi = "Kategori : __Doğa__"
        liste = ['armut', 'ağaç', 'böcek', 'elma', 'mantar', 'meyve', 'muz', 'orman', 'ot', 'palmiye', 'sebze', 'yaprak', 'çimen', 'çiçek']
    elif kategori_secimi == "uzay":
        kategori_ismi = "Kategori : __Uzay__"
        liste = ['astronot', 'dünya', 'evren', 'galaksi', 'gezegen', 'meteor', 'uydu', 'uzay', 'yörünge', 'yıldız']
    elif kategori_secimi == "okyanus":
        kategori_ismi = "Kategori : __Okyanus__"
        liste = ['ahtapot', 'balina', 'balık', 'batık', 'dalga', 'denizaltı', 'fırtına', 'gemi', 'girdap', 'kalamar', 'kaplumbağa', 'karanlık', 'kum', 'köpekbalığı', 'mercan', 'okyanus', 'yengeç', 'yosun', 'yunus', 'ıstakoz']
    elif kategori_secimi == "developer":
        kategori_ismi = "Kategori : __Developer__"
        liste = ["Mehmet"]

    secilen_kelime = random.choice(liste)

    print(secilen_kelime)

    uzunluk = len(secilen_kelime)
    harf_yerleri = []
    cumle=""
    kullanilan_harfler = []

    for x in range(uzunluk):
        harf_yerleri.append("--  ")

    for y in harf_yerleri:
        cumle += y
    embed = discord.Embed(title=f"**Adam Asmaca**\n{kategori_ismi}",description=f"**{cumle}**",colour=discord.Colour.from_rgb(5,5,5))
    embed.set_thumbnail(url=MHT)
    embed.set_image(url=guncel_resim)
    await ctx.send(embed=embed)


    while control:
        await ctx.send("**Lütfen Harf giriniz veya Tahminde bulununuz.**")
        msg = await Bot.wait_for("message",check=check)
        msg = msg.content
        msg = msg.lower()

        if msg == "exit":
            embed = discord.Embed(title=f"**Adam Asmaca**\n{kategori_ismi}\n:no_entry: Oyun Sonlandırıldı :no_entry:\nKelime : {secilen_kelime}",colour=discord.Colour.from_rgb(150,5,5))
            embed.set_thumbnail(url=MHT)
            embed.set_image(url=guncel_resim)
            await ctx.send(embed=embed)
            break

        elif msg[0] == ".":
            continue

        elif msg == f"{secilen_kelime}":
            embed = discord.Embed(title=f"**Adam Asmaca\n{kategori_ismi}\n:tada: Kazandın :tada:**\n\n{secilen_kelime}", url="https://www.com",colour=discord.Colour.from_rgb(5,255,5))
            embed.set_thumbnail(url=MHT)
            embed.set_image(url=guncel_resim)
            await ctx.send(embed=embed)
            break



        elif len(msg) > 1:
            await ctx.send("**Yanlış Tahmin ya da birden fazla harf girdiniz (yorum yazmak için '.'(nokta) kullanarak cümleye başlayın)!!!**")
            kalan_hak -= 1
            if kalan_hak == 5:
                guncel_resim = kafa

                embed = discord.Embed(title=f"**Adam Asmaca**\n{kategori_ismi}", description=f"**{cumle}**",
                                      colour=discord.Colour.from_rgb(255, 5, 5))
                embed.add_field(name="**Yanlış tahmin**", value=f"Kullanılan Harfler : {kullanilan_harfler}")
                embed.set_thumbnail(url=MHT)
                embed.set_image(url=guncel_resim)

                hata = await ctx.send(embed=embed)
                await asyncio.sleep(0.1)

                embed = discord.Embed(title=f"**Adam Asmaca**\n{kategori_ismi}", description=f"**{cumle}**",
                                      colour=discord.Colour.from_rgb(5, 5, 5))
                embed.add_field(name="**Yanlış tahmin**", value=f"Kullanılan Harfler : {kullanilan_harfler}")
                embed.set_thumbnail(url=MHT)
                embed.set_image(url=guncel_resim)
                await hata.edit(embed=embed)

                continue
            if kalan_hak == 4:
                guncel_resim = govde
                embed = discord.Embed(title=f"**Adam Asmaca**\n{kategori_ismi}", description=f"**{cumle}**",
                                      colour=discord.Colour.from_rgb(255, 5, 5))
                embed.add_field(name="**Yanlış tahmin**", value=f"Kullanılan Harfler : {kullanilan_harfler}")
                embed.set_thumbnail(url=MHT)
                embed.set_image(url=guncel_resim)
                hata = await ctx.send(embed=embed)
                await asyncio.sleep(0.1)

                embed = discord.Embed(title=f"**Adam Asmaca**\n{kategori_ismi}", description=f"**{cumle}**",
                                      colour=discord.Colour.from_rgb(5, 5, 5))
                embed.add_field(name="**Yanlış tahmin**", value=f"Kullanılan Harfler : {kullanilan_harfler}")
                embed.set_thumbnail(url=MHT)
                embed.set_image(url=guncel_resim)
                await hata.edit(embed=embed)
                continue
            if kalan_hak == 3:
                guncel_resim = bacak1
                embed = discord.Embed(title=f"**Adam Asmaca**\n{kategori_ismi}", description=f"**{cumle}**",
                                      colour=discord.Colour.from_rgb(255, 5, 5))
                embed.add_field(name="**Yanlış tahmin**", value=f"Kullanılan Harfler : {kullanilan_harfler}")
                embed.set_thumbnail(url=MHT)
                embed.set_image(url=guncel_resim)
                hata = await ctx.send(embed=embed)
                await asyncio.sleep(0.1)

                embed = discord.Embed(title=f"**Adam Asmaca**\n{kategori_ismi}", description=f"**{cumle}**",
                                      colour=discord.Colour.from_rgb(5, 5, 5))
                embed.add_field(name="**Yanlış tahmin**", value=f"Kullanılan Harfler : {kullanilan_harfler}")
                embed.set_thumbnail(url=MHT)
                embed.set_image(url=guncel_resim)
                await hata.edit(embed=embed)
                continue
            if kalan_hak == 2:
                guncel_resim = bacak2
                embed = discord.Embed(title=f"**Adam Asmaca**\n{kategori_ismi}", description=f"**{cumle}**",
                                      colour=discord.Colour.from_rgb(255, 5, 5))
                embed.add_field(name="**Yanlış tahmin**", value=f"Kullanılan Harfler : {kullanilan_harfler}")
                embed.set_thumbnail(url=MHT)
                embed.set_image(url=guncel_resim)
                hata = await ctx.send(embed=embed)
                await asyncio.sleep(0.1)

                embed = discord.Embed(title=f"**Adam Asmaca**\n{kategori_ismi}", description=f"**{cumle}**",
                                      colour=discord.Colour.from_rgb(5, 5, 5))
                embed.add_field(name="**Yanlış tahmin**", value=f"Kullanılan Harfler : {kullanilan_harfler}")
                embed.set_thumbnail(url=MHT)
                embed.set_image(url=guncel_resim)
                await hata.edit(embed=embed)
                continue
            if kalan_hak == 1:
                guncel_resim = kol1
                embed = discord.Embed(title=f"**Adam Asmaca**\n{kategori_ismi}", description=f"**{cumle}**",
                                      colour=discord.Colour.from_rgb(255, 5, 5))
                embed.add_field(name="**Yanlış tahmin**", value=f"Kullanılan Harfler : {kullanilan_harfler}")
                embed.set_thumbnail(url=MHT)
                embed.set_image(url=guncel_resim)

                hata = await ctx.send(embed=embed)
                await asyncio.sleep(0.1)

                embed = discord.Embed(title=f"**Adam Asmaca**\n{kategori_ismi}", description=f"**{cumle}**",
                                      colour=discord.Colour.from_rgb(5, 5, 5))
                embed.add_field(name="**Yanlış tahmin**", value=f"Kullanılan Harfler : {kullanilan_harfler}")
                embed.set_thumbnail(url=MHT)
                embed.set_image(url=guncel_resim)
                await hata.edit(embed=embed)
                continue
            if kalan_hak == 0:
                guncel_resim = son

                embed = discord.Embed(
                    title=f"**Adam Asmaca**\n{kategori_ismi}\n:skull: Kaybettin :skull:  \nKelime : {secilen_kelime}",
                    colour=discord.Colour.from_rgb(255, 5, 5))
                embed.add_field(name="**Yanlış tahmin**", value=f"Kullanılan Harfler : {kullanilan_harfler}")
                embed.set_thumbnail(url=MHT)
                embed.set_image(url=guncel_resim)
                await ctx.send(embed=embed)
                break


        elif msg in secilen_kelime:
            print("devamke")
        else:
            if kullanilan_harfler.count(msg) >= 1:
                await ctx.send(f"**bu harfi zaten kullandınız.  [ {msg} ]**")
                continue
            elif len(msg) == 1:
                kullanilan_harfler.append(msg)
            kalan_hak -=1
            if kalan_hak == 5:
                guncel_resim = kafa

                embed = discord.Embed(title=f"**Adam Asmaca**\n{kategori_ismi}",description=f"**{cumle}**",colour=discord.Colour.from_rgb(255,5,5))
                embed.add_field(name="**Yanlış Harf**",value=f"Kullanılan Harfler : {kullanilan_harfler}")
                embed.set_thumbnail(url=MHT)
                embed.set_image(url=guncel_resim)

                hata =await ctx.send(embed=embed)
                await asyncio.sleep(0.1)

                embed = discord.Embed(title=f"**Adam Asmaca**\n{kategori_ismi}", description=f"**{cumle}**",colour=discord.Colour.from_rgb(5, 5, 5))
                embed.add_field(name="**Yanlış Harf**",value=f"Kullanılan Harfler : {kullanilan_harfler}")
                embed.set_thumbnail(url=MHT)
                embed.set_image(url=guncel_resim)
                await hata.edit(embed=embed)



                continue
            if kalan_hak == 4:
                guncel_resim = govde
                embed = discord.Embed(title=f"**Adam Asmaca**\n{kategori_ismi}",description=f"**{cumle}**",colour=discord.Colour.from_rgb(255,5,5))
                embed.add_field(name="**Yanlış Harf**",value=f"Kullanılan Harfler : {kullanilan_harfler}")
                embed.set_thumbnail(url=MHT)
                embed.set_image(url=guncel_resim)
                hata = await ctx.send(embed=embed)
                await asyncio.sleep(0.1)

                embed = discord.Embed(title=f"**Adam Asmaca**\n{kategori_ismi}", description=f"**{cumle}**",
                                      colour=discord.Colour.from_rgb(5, 5, 5))
                embed.add_field(name="**Yanlış Harf**",value=f"Kullanılan Harfler : {kullanilan_harfler}")
                embed.set_thumbnail(url=MHT)
                embed.set_image(url=guncel_resim)
                await hata.edit(embed=embed)
                continue
            if kalan_hak == 3:
                guncel_resim = bacak1
                embed = discord.Embed(title=f"**Adam Asmaca**\n{kategori_ismi}",description=f"**{cumle}**",colour=discord.Colour.from_rgb(255,5,5))
                embed.add_field(name="**Yanlış Harf**",value=f"Kullanılan Harfler : {kullanilan_harfler}")
                embed.set_thumbnail(url=MHT)
                embed.set_image(url=guncel_resim)
                hata = await ctx.send(embed=embed)
                await asyncio.sleep(0.1)

                embed = discord.Embed(title=f"**Adam Asmaca**\n{kategori_ismi}", description=f"**{cumle}**",
                                      colour=discord.Colour.from_rgb(5, 5, 5))
                embed.add_field(name="**Yanlış Harf**",value=f"Kullanılan Harfler : {kullanilan_harfler}")
                embed.set_thumbnail(url=MHT)
                embed.set_image(url=guncel_resim)
                await hata.edit(embed=embed)
                continue
            if kalan_hak == 2:
                guncel_resim = bacak2
                embed = discord.Embed(title=f"**Adam Asmaca**\n{kategori_ismi}",description=f"**{cumle}**",colour=discord.Colour.from_rgb(255,5,5))
                embed.add_field(name="**Yanlış Harf**",value=f"Kullanılan Harfler : {kullanilan_harfler}")
                embed.set_thumbnail(url=MHT)
                embed.set_image(url=guncel_resim)
                hata = await ctx.send(embed=embed)
                await asyncio.sleep(0.1)

                embed = discord.Embed(title=f"**Adam Asmaca**\n{kategori_ismi}", description=f"**{cumle}**",
                                      colour=discord.Colour.from_rgb(5, 5, 5))
                embed.add_field(name="**Yanlış Harf**",value=f"Kullanılan Harfler : {kullanilan_harfler}")
                embed.set_thumbnail(url=MHT)
                embed.set_image(url=guncel_resim)
                await hata.edit(embed=embed)
                continue
            if kalan_hak == 1:
                guncel_resim = kol1
                embed = discord.Embed(title=f"**Adam Asmaca**\n{kategori_ismi}",description=f"**{cumle}**",colour=discord.Colour.from_rgb(255,5,5))
                embed.add_field(name="**Yanlış Harf**",value=f"Kullanılan Harfler : {kullanilan_harfler}")
                embed.set_thumbnail(url=MHT)
                embed.set_image(url=guncel_resim)

                hata = await ctx.send(embed=embed)
                await asyncio.sleep(0.1)

                embed = discord.Embed(title=f"**Adam Asmaca**\n{kategori_ismi}", description=f"**{cumle}**",
                                      colour=discord.Colour.from_rgb(5, 5, 5))
                embed.add_field(name="**Yanlış Harf**",value=f"Kullanılan Harfler : {kullanilan_harfler}")
                embed.set_thumbnail(url=MHT)
                embed.set_image(url=guncel_resim)
                await hata.edit(embed=embed)
                continue
            if kalan_hak == 0:
                guncel_resim = son

                embed = discord.Embed(title=f"**Adam Asmaca**\n{kategori_ismi}\n:skull: Kaybettin :skull:  \nKelime : {secilen_kelime}",colour=discord.Colour.from_rgb(255,5,5))
                embed.add_field(name="**Yanlış Harf**",value=f"Kullanılan Harfler : {kullanilan_harfler}")
                embed.set_thumbnail(url=MHT)
                embed.set_image(url=guncel_resim)
                await ctx.send(embed=embed)
                break


        count = -1
        for i in secilen_kelime:
            count += 1
            if msg == i:

                print(count)
                harf_yerleri.pop(count)

                harf_yerleri.insert(count,f"{msg}  ")
                print(harf_yerleri)
        cumle = ""
        for y in harf_yerleri:
            cumle += y
        if kullanilan_harfler.count(msg) >= 1:
            await ctx.send(f"**bu harfi zaten kullandınız.  [ {msg} ]**")
            continue
        else:
            kullanilan_harfler.append(msg)

        embed = discord.Embed(title=f"**Adam Asmaca**\n{kategori_ismi}",description=f"**{cumle}**",colour=discord.Colour.from_rgb(5,255,5))
        embed.set_thumbnail(url=MHT)
        embed.add_field(name="**Doğru Harf**", value=f"Kullanılan Harfler : {kullanilan_harfler}")
        embed.set_image(url=guncel_resim)
        dogru = await ctx.send(embed=embed)
        await asyncio.sleep(0.1)

        embed = discord.Embed(title=f"**Adam Asmaca**\n{kategori_ismi}", description=f"**{cumle}**",
                              colour=discord.Colour.from_rgb(5, 5, 5))
        embed.set_thumbnail(url=MHT)
        embed.add_field(name="**Doğru Harf**", value=f"Kullanılan Harfler : {kullanilan_harfler}")
        embed.set_image(url=guncel_resim)
        await dogru.edit(embed=embed)


        if "--  " in harf_yerleri:
            print("devamke")
            continue
        else:
            embed = discord.Embed(title=f"**Adam Asmaca\n{kategori_ismi}\nKazandın :tada:**",description=f"**{cumle}**",url="https://www.com",colour=discord.Colour.from_rgb(5,255,5))
            embed.set_image(url=guncel_resim)
            embed.add_field(name="**Kullanılan Harfler**", value=f"{kullanilan_harfler}")
            embed.set_thumbnail(url=MHT)
            await ctx.send(embed=embed)
            print("Kazandın")
            control= 0

@Bot.command(brief="-help avatar",description="botun bulunduğu sunucudaki birisinin profil fotoğrafını tam halini görmek ve almak için bu komutu yazabilirsiniz. kullanıcıyı etiketlemeniz gerekir\n\nÖrnek Kullanım:\n-avatar @user\n")
async def avatar(ctx, member: discord.User):
    user = await Bot.fetch_user(member.id)
    #await ctx.send(member.avatar_url)
    await ctx.send(user.avatar_url)


@Bot.command(brief="-help yazıtura",description="Yazı Tura oyunu başlatır. 3 Seçenekten biri gelir (Yazı,Tura,Dik) dik gelme olasılığı oldukça düşüktür.")
async def yazıtura(ctx):
    yazi = "https://i.hizliresim.com/qANl5V.png"
    tura = "https://i.hizliresim.com/Z5zV8z.png"
    dik = "https://c.tenor.com/MDVk57u-7KgAAAAd/yaz%C4%B1tura-dik-geldi.gif"

    para = ["YAZI","TURA"]
    sayi = random.randint(1,100)
    if sayi <= 1:
        sonuc = "DİK"
    else:
        sonuc = random.choice(para)

    embed1 = discord.Embed(title=f"Para Atılıyor . . .")
    msg = await ctx.send(embed=embed1)
    await asyncio.sleep(delay=1)
    embed2 = discord.Embed(title=f"Para Havada Dönüyor . . .")
    await msg.edit(embed=embed2)
    await asyncio.sleep(delay=1)
    embed3 = discord.Embed(title=f"Para Düştü . . .")
    await msg.edit(embed=embed3)
    await asyncio.sleep(delay=1)
    embed4 = discord.Embed(title=f"{sonuc} Geldi")

    if sonuc == "TURA":
        embed4.set_thumbnail(url=tura)
    if sonuc == "YAZI":
        embed4.set_thumbnail(url=yazi)
    if sonuc == "DİK":
        embed4.set_thumbnail(url=dik)

    await msg.edit(embed=embed4)


@Bot.command(aliases=["developer"])
async def developer_info(ctx):
    yas = 2021 - 2002
    bilgi = f"""--------------------------------------------------
isim / soy isim : Mehmet Kaya
iletişim / instagram : mehmet__kaya1903
iletişim / discord : MehmetK#2002
Bölümü : Bilgisayar Mühendisliği
--------------------------------------------------

    """
    await ctx.send(bilgi)

@Bot.command(aliases=["fb"],brief="-help feedback",description="Bot Geliştiricisine Öneri veya Hataları söylemek için kullanabilirsiniz. Geri Bildirimde bulunmanız Botun gelişmesi için büyük önem taşımaktadır bu yüzden lütfen bot ile ilgili her türlü konuda Geri Bildirimde bulunun.\n\nÖrnek Kullanım:\n-feedback 'Cümlenizi komutu yazdıktan sonra istediğiniz şekilde yazabilirsiniz\n'")
async def feedback(ctx,*args):
    args = list(args)
    cumle = ""

    for x in args:
        x = x.replace("İ", "i")
        x = x.lower()
        x = x.replace("ğ","g")
        x = x.replace("ü", "u")
        x = x.replace("ş", "s")
        x = x.replace("ö", "o")
        x = x.replace("ç", "c")
        x = x.replace("ı", "i")
        cumle += f"{x} "
    cumle +=f"\n"
    file = open("feedbacks.txt","a")
    file.writelines(f"* {cumle}")
    file.close()
    await ctx.send("Geri bildiriminiz alınmıştır.")

@Bot.command(brief="sadece developer erişebilir")
@commands.has_role(905747509148786698)
async def fboku(ctx):
    file = open("feedbacks.txt","r")
    feedbacks = file.read()
    await ctx.send(feedbacks)

@Bot.command(brief="-help zar",description="Zar atar.")
async def zar(ctx):
    one = "https://cdn.pixabay.com/photo/2013/07/12/16/22/number-150790_960_720.png"
    two = "https://cdn.pixabay.com/photo/2013/07/12/16/22/number-150791_960_720.png"
    three = "https://cdn.pixabay.com/photo/2013/07/12/16/22/number-150792_960_720.png"
    four = "https://cdn.pixabay.com/photo/2013/07/12/16/22/number-150793_960_720.png"
    five = "https://cdn.pixabay.com/photo/2013/07/12/16/22/number-150794_960_720.png"
    six = "https://cdn.pixabay.com/photo/2013/07/12/16/22/number-150795_960_720.png"
    numbers = [":one:", ":two:", ":three:", ":four:", ":five:", ":six:"]
    sayilar_png = [one, two, three, four, five, six]
    embed = discord.Embed(title=":game_die: Zar Atılıyor . . .")
    embed.set_thumbnail(
        url="https://w7.pngwing.com/pngs/704/249/png-transparent-dice-scalable-graphics-dice-s-game-rectangle-dice.png")

    zar = await ctx.send(embed=embed)
    embed_two = discord.Embed(title=f":game_die: Zar Atıldı")
    embed_two.set_thumbnail(url=random.choice(sayilar_png))
    await asyncio.sleep(delay=1)

    await zar.edit(embed=embed_two)

@Bot.command(aliases=["sf","serveri","infoServer"])
async def serverinf(ctx):
    a = Bot.guilds
    servers = ""
    for x in a:
        servers +=f"{x}\n"

    await ctx.send(servers)
Bot.run(TOKEN)
