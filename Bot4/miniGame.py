import asyncio
import discord
from discord.ext import commands, tasks
from dokusan import generators
from dokusan import solvers, renderers
from dokusan.boards import BoxSize, Sudoku
import random
import time
import requests
from bs4 import BeautifulSoup
from datetime import datetime


intents = discord.Intents(messages=True, guilds=True, reactions=True, presences=True, members=True)
Bot = commands.Bot(command_prefix="-", intents=intents)

kare = ":white_large_square:"
x = ":x:"
o = ":o:"
num1=":one:"
num2=":two:"
num3=":three:"
num4=":four:"
num5=":five:"
num6=":six:"
num7=":seven:"
num8=":eight:"
num9=":nine:"
@Bot.event
async def on_ready():
    print("ben hazırım")
@Bot.event
async def on_message(message):
    await Bot.process_commands(message)

@Bot.command()
async def xox(ctx,secim):
    if int(secim) == 1:
        liste = [num1, num2, num3, num4, num5, num6, num7, num8, num9]
    else:
        liste = [kare, kare, kare, kare, kare, kare, kare, kare, kare]
    control = 1
                #0    1    2
                #3    4    5
                #6    7    8



    await ctx.send(f"\n**KARE SEÇİN  (1-9)**")
    await ctx.send(f"{liste[0]}{liste[1]}{liste[2]}\n{liste[3]}{liste[4]}{liste[5]}\n{liste[6]}{liste[7]}{liste[8]}\n")

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    while(control == 1):


        if liste[0] == liste[1] == liste[2] == x or liste[0] == liste[1] == liste[2] == o:
            await ctx.send(f"**{liste[0]}** KAZANDI")
            break
        if liste[3] == liste[4] == liste[5] == x or liste[3] == liste[4] == liste[5] == o:
            await ctx.send(f"**{liste[3]}** KAZANDI")
            break
        if liste[6] == liste[7] == liste[8] == x or liste[6] == liste[7] == liste[8] == o:
            await ctx.send(f"**{liste[6]}** KAZANDI")
            break
        if liste[0] == liste[3] == liste[6] == x or liste[0] == liste[3] == liste[6] == o:
            await ctx.send(f"**{liste[0]}** KAZANDI")
            break
        if liste[1] == liste[4] == liste[7] == x or liste[1] == liste[4] == liste[7] == o:
            await ctx.send(f"**{liste[1]}** KAZANDI")
            break
        if liste[2] == liste[5] == liste[8] == x or liste[2] == liste[5] == liste[8] == o:
            await ctx.send(f"**{liste[2]}** KAZANDI")
            break
        if liste[0] == liste[4] == liste[8] == x or liste[0] == liste[4] == liste[8] == o:
            await ctx.send(f"**{liste[0]}** KAZANDI")
            break
        if liste[2] == liste[4] == liste[6] == x or liste[2] == liste[4] == liste[6] == o:
            await ctx.send(f"**{liste[2]}** KAZANDI")
            break
        if (liste[0] != kare and liste[1] != kare and liste[2] != kare and liste[3] != kare and liste[4] != kare and liste[5] != kare and liste[6] != kare and liste[7] != kare and liste[8] != kare)and\
                (liste[0] != num1 and liste[1] != num2 and liste[2] != num3 and liste[3] != num4 and liste[
            4] != num5 and liste[5] != num6 and liste[6] != num7 and liste[7] != num8 and liste[8] != num9):
            await ctx.send(f"**BERABERE :o: - :x:**")
            break


        try:
            await ctx.send("OYUN SIRASI  :  :x:")
            msg = await Bot.wait_for("message", check=check)

            if msg.content == "exit":
                break
            if liste[int(msg.content)-1] == x or liste[int(msg.content)-1] == o:
                await ctx.send(F"  **[{msg.content}]**  BU KUTU DOLU")
            else:
                liste[int(msg.content)-1] = x
                await ctx.send(f"{liste[0]}{liste[1]}{liste[2]}\n{liste[3]}{liste[4]}{liste[5]}\n{liste[6]}{liste[7]}{liste[8]}\n")
                await ctx.send(f"**KARE SEÇİN  (1-9)   2**")
                if liste[0] == liste[1] == liste[2] == x or liste[0] == liste[1] == liste[2] == o:
                    await ctx.send(f"**{liste[0]}** KAZANDI")
                    break
                if liste[3] == liste[4] == liste[5] == x or liste[3] == liste[4] == liste[5] == o:
                    await ctx.send(f"**{liste[3]}** KAZANDI")
                    break
                if liste[6] == liste[7] == liste[8] == x or liste[6] == liste[7] == liste[8] == o:
                    await ctx.send(f"**{liste[6]}** KAZANDI")
                    break
                if liste[0] == liste[3] == liste[6] == x or liste[0] == liste[3] == liste[6] == o:
                    await ctx.send(f"**{liste[0]}** KAZANDI")
                    break
                if liste[1] == liste[4] == liste[7] == x or liste[1] == liste[4] == liste[7] == o:
                    await ctx.send(f"**{liste[1]}** KAZANDI")
                    break
                if liste[2] == liste[5] == liste[8] == x or liste[2] == liste[5] == liste[8] == o:
                    await ctx.send(f"**{liste[2]}** KAZANDI")
                    break
                if liste[0] == liste[4] == liste[8] == x or liste[0] == liste[4] == liste[4] == o:
                    await ctx.send(f"**{liste[0]}** KAZANDI")
                    break
                if liste[2] == liste[4] == liste[6] == x or liste[2] == liste[4] == liste[6] == o:
                    await ctx.send(f"**{liste[2]}** KAZANDI")
                    break
                if (liste[0] != kare and liste[1] != kare and liste[2] != kare and liste[3] != kare and liste[
                    4] != kare and liste[5] != kare and liste[6] != kare and liste[7] != kare and liste[8] != kare) and (
                        liste[0] != num1 and liste[1] != num2 and liste[2] != num3 and liste[3] != num4 and liste[
                    4] != num5 and liste[5] != num6 and liste[6] != num7 and liste[7] != num8 and liste[8] != num9):
                    await ctx.send(f"**BERABERE :o: - :x:**")
                    break

                while (True):


                    try:
                        await ctx.send("OYUN SIRASI  :  :o:")
                        msg = await Bot.wait_for("message", check=check)
                        if msg.content == "exit":
                            control = 0
                            break
                        if liste[int(msg.content) - 1] == x or liste[int(msg.content) - 1] == o:
                            await ctx.send(F"  **[{msg.content}]**  BU KUTU DOLU")
                        else:
                            liste[int(msg.content) - 1] = o
                            await ctx.send(f"{liste[0]}{liste[1]}{liste[2]}\n{liste[3]}{liste[4]}{liste[5]}\n{liste[6]}{liste[7]}{liste[8]}\n")
                            await ctx.send(f"**KARE SEÇİN  (1-9)   1**")
                            break


                    except:
                        await ctx.send("LÜTFEN SADECE 1-9 ARASI BİR DEĞER GİRİN...")




        except:
            await ctx.send("LÜTFEN SADECE 1-9 ARASI BİR DEĞER GİRİN...")
@Bot.command()
async def kutla(ctx):
    target = await Bot.fetch_user(784845899972083743)
    await target.send("https://www.youtube.com/watch?v=kOvLkkJc_l0")
@Bot.command()
async def xox2(ctx,user: discord.Member,secim):
    control = 1
                #0    1    2
                #3    4    5
                #6    7    8

    if int(secim) == 1:
        liste = [num1, num2, num3, num4, num5, num6, num7, num8, num9]
    else:
        liste = [kare, kare, kare, kare, kare, kare, kare, kare, kare]

    await ctx.send(f"\n**KARE SEÇİN  (1-9)**")
    await ctx.send(f"{liste[0]}{liste[1]}{liste[2]}\n{liste[3]}{liste[4]}{liste[5]}\n{liste[6]}{liste[7]}{liste[8]}\n")

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel
    def check2(msg):
        return (msg.author == user or msg.author == ctx.author)and msg.channel == ctx.channel

    while(control == 1):


        if liste[0] == liste[1] == liste[2] == x or liste[0] == liste[1] == liste[2] == o:
            await ctx.send(f"**{liste[0]}** KAZANDI")
            break
        if liste[3] == liste[4] == liste[5] == x or liste[3] == liste[4] == liste[5] == o:
            await ctx.send(f"**{liste[3]}** KAZANDI")
            break
        if liste[6] == liste[7] == liste[8] == x or liste[6] == liste[7] == liste[8] == o:
            await ctx.send(f"**{liste[6]}** KAZANDI")
            break
        if liste[0] == liste[3] == liste[6] == x or liste[0] == liste[3] == liste[6] == o:
            await ctx.send(f"**{liste[0]}** KAZANDI")
            break
        if liste[1] == liste[4] == liste[7] == x or liste[1] == liste[4] == liste[7] == o:
            await ctx.send(f"**{liste[1]}** KAZANDI")
            break
        if liste[2] == liste[5] == liste[8] == x or liste[2] == liste[5] == liste[8] == o:
            await ctx.send(f"**{liste[2]}** KAZANDI")
            break
        if liste[0] == liste[4] == liste[8] == x or liste[0] == liste[4] == liste[4] == o:
            await ctx.send(f"**{liste[0]}** KAZANDI")
            break
        if liste[2] == liste[4] == liste[6] == x or liste[2] == liste[4] == liste[6] == o:
            await ctx.send(f"**{liste[2]}** KAZANDI")
            break
        if (liste[0] != kare and liste[1] != kare and liste[2] != kare and liste[3] != kare and liste[4] != kare and
            liste[5] != kare and liste[6] != kare and liste[7] != kare and liste[8] != kare) and (
                liste[0] != num1 and liste[1] != num2 and liste[2] != num3 and liste[3] != num4 and liste[
            4] != num5 and liste[5] != num6 and liste[6] != num7 and liste[7] != num8 and liste[8] != num9):
            await ctx.send(f"**BERABERE :o: - :x:**")
            break

        count2 = 0
        try:
            await ctx.send("OYUN SIRASI  :  :x:")
            count2 += 1
            print(count2)
            if count2 >= 2:
                control = 0
                await ctx.send("OYUN SONLANDI...")
                break
            msg = await Bot.wait_for("message", check=check,timeout=20)


            if msg.content == "exit":
                await ctx.send(f"ÇIKIŞ YAPILDI")
                break
            if liste[int(msg.content)-1] == x or liste[int(msg.content)-1] == o:
                await ctx.send(F"  **[{msg.content}]**  BU KUTU DOLU")
            else:
                liste[int(msg.content)-1] = x
                await ctx.send(f"{liste[0]}{liste[1]}{liste[2]}\n{liste[3]}{liste[4]}{liste[5]}\n{liste[6]}{liste[7]}{liste[8]}\n")
                await ctx.send(f"**KARE SEÇİN  (1-9)   2**")
                if liste[0] == liste[1] == liste[2] == x or liste[0] == liste[1] == liste[2] == o:
                    await ctx.send(f"**{liste[0]}** KAZANDI")
                    break
                if liste[3] == liste[4] == liste[5] == x or liste[3] == liste[4] == liste[5] == o:
                    await ctx.send(f"**{liste[3]}** KAZANDI")
                    break
                if liste[6] == liste[7] == liste[8] == x or liste[6] == liste[7] == liste[8] == o:
                    await ctx.send(f"**{liste[6]}** KAZANDI")
                    break
                if liste[0] == liste[3] == liste[6] == x or liste[0] == liste[3] == liste[6] == o:
                    await ctx.send(f"**{liste[0]}** KAZANDI")
                    break
                if liste[1] == liste[4] == liste[7] == x or liste[1] == liste[4] == liste[7] == o:
                    await ctx.send(f"**{liste[1]}** KAZANDI")
                    break
                if liste[2] == liste[5] == liste[8] == x or liste[2] == liste[5] == liste[8] == o:
                    await ctx.send(f"**{liste[2]}** KAZANDI")
                    break
                if liste[0] == liste[4] == liste[8] == x or liste[0] == liste[4] == liste[4] == o:
                    await ctx.send(f"**{liste[0]}** KAZANDI")
                    break
                if liste[2] == liste[4] == liste[6] == x or liste[2] == liste[4] == liste[6] == o:
                    await ctx.send(f"**{liste[2]}** KAZANDI")
                    break
                if (liste[0] != kare and liste[1] != kare and liste[2] != kare and liste[3] != kare and liste[
                    4] != kare and liste[5] != kare and liste[6] != kare and liste[7] != kare and liste[8] != kare) and (
                        liste[0] != num1 and liste[1] != num2 and liste[2] != num3 and liste[3] != num4 and liste[
                    4] != num5 and liste[5] != num6 and liste[6] != num7 and liste[7] != num8 and liste[8] != num9):
                    await ctx.send(f"**BERABERE :o: - :x:**")
                    break
                while (True):

                    count1 = 0
                    try:

                        await ctx.send("OYUN SIRASI  :  :o:")
                        count1 += 1
                        print(count1)
                        if count1 >=2:
                            control = 0
                            await ctx.send("OYUN SONLANDI...")
                            break
                        msg = await Bot.wait_for("message",check=check2,timeout=20)



                        if liste[int(msg.content) - 1] == x or liste[int(msg.content) - 1] == o:
                            await ctx.send(F"  **[{msg.content}]**  BU KUTU DOLU")
                        else:
                            liste[int(msg.content) - 1] = o
                            await ctx.send(f"{liste[0]}{liste[1]}{liste[2]}\n{liste[3]}{liste[4]}{liste[5]}\n{liste[6]}{liste[7]}{liste[8]}\n")
                            await ctx.send(f"**KARE SEÇİN  (1-9)   1**")
                            break


                    except:
                        await ctx.send(f"{user.mention} LÜTFEN SADECE 1-9 ARASI BİR DEĞER GİRİN...")

        except:
            await ctx.send(f"{ctx.author.mention} LÜTFEN SADECE 1-9 ARASI BİR DEĞER GİRİN...")







@Bot.command()
async def sudoku(ctx):
    sudoku = generators.random_sudoku(avg_rank=200)
    liste =str(sudoku)
    print(liste)

    cumle = f""
    count = 0
    sayac = 0
    sayi = ""
    for x in range(len(liste)):
        sayac += 1
        if int(liste[count]) == 0:
            sayi = kare
        if int(liste[count]) == 1:
            sayi = num1
        if int(liste[count]) == 2:
            sayi = num2
        if int(liste[count]) == 3:
            sayi = num3
        if int(liste[count]) == 4:
            sayi = num4
        if int(liste[count]) == 5:
            sayi = num5
        if int(liste[count]) == 6:
            sayi = num6
        if int(liste[count]) == 7:
            sayi = num7
        if int(liste[count]) == 8:
            sayi = num8
        if int(liste[count]) == 9:
            sayi = num9

        cumle +=f"{sayi}"
        count += 1
        if sayac >= 9:
            cumle += "\n"
            sayac = 0

    await ctx.send(cumle)




@Bot.command()
async def sdk(ctx):
    sudoku = Sudoku.from_list(
        [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 3, 0, 0, 5],
            [0, 0, 1, 0, 2, 0, 0, 0, 0],
            [0, 0, 0, 5, 0, 7, 0, 0, 0],
            [0, 0, 4, 0, 0, 0, 1, 0, 0],
            [0, 9, 0, 0, 0, 0, 0, 0, 0],
            [5, 0, 0, 0, 0, 0, 0, 7, 3],
            [0, 0, 2, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 4, 0, 0, 0, 9],
        ],
        box_size=BoxSize(3,3),
    )

    solution = solvers.backtrack(sudoku)
    print(renderers.colorful(solution))







@Bot.command()
async def deneme01(ctx):
    emoji = Bot.get_emoji(598060521320742923)
    await ctx.send(emoji)




Bot.run("BURAYA DİSCORD BOT TOKENİ GELİR")