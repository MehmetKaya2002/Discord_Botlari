import discord
from discord.ext import commands, tasks
import random
import requests
from bs4 import BeautifulSoup
import time
import ast
import asyncio


intents = discord.Intents(messages=True, guilds=True, reactions=True, presences=True, members=True)
Bot = commands.Bot(command_prefix="-", intents=intents)

fiyatlar = {
    "redluger": "Red Luger \n - TL ",
    "greenluger": "Green Luger \n - TL",
    "frostbite": "Frostbite \n - TL",
    "frostsaber": "Frostsaber \n - TL",
    "cookieblade": "Cookieblade \n - TL",
    "peppermint": "Peppermint \n - TL",
    "chill": "Chill \n - TL ",
    "eternal1": " Eternal 1 \n - TL",
    "eternal2": "Eternal 2 \n - TL",
    "eternal3": "Eternal 3\n - TL",
    "eternal4": "Eternal 4 \n - TL",
    "nah": "-",
    "fıstık": "PAHA BİÇİLEMEZ",
    "lightbringer": "Lightbringer \n - TL",
    "prismatic": "Prismatic \n - TL ",
    "bioblade": "Bioblade \n - TL",
    "gemstone": "Gemstone \n - TL",
    "clockwork": "Clockwork \n - TL",
    "deathshard": "Deathshard \n - TL",
    "fang": "Fang \n - TL",
    "flames": "Flames \n - TL",
    "heat": " Heat \n - TL",
    "laser": "Laser \n - TL ",
    "luger": "Luger \n - TL ",
    "nightblade": "Nightblade\n - TL",
    "pixel": "Pixel \n - TL",
    "saw": "Saw \n - TL",
    "shark": "Shark \n - TL",
    "tides": "Tides \n - TL",
    "america": "America \n - TL",
    "blood": "Blood \n - TL",
    "cowboy": "Cowboy \n - TL",
    "ghost": "Ghost \n - TL",
    "golden": " Golden \n - TL",
    "vlaser": "Laser \n - TL",
    "phaser": "Phaser \n - TL",
    "prince": "Prince\n - TL",
    "shadow": "shadow \n - TL",
    "splitter": "splitter \n - TL",
    "eggblade": " eggblade \n - TL",
    "darkbringer": "darkbringer \n - TL",
    "heartblade": "heartblade \n - TL",
    "icewing": "icewing\n - TL",
    "redseer": "redseer \n - TL",
    "blueseer": "blueseer \n - TL",
    "orangeseer": "orangeseer \n - TL",
    "purpleseer": "purpleseer \n - TL",
    "yellowseer": "yellowseer \n - TL",
    # "cseer": "cseer \n - TL ",
    "ghostblade": "ghostblade \n - TL",
    "battleaxe": "battle axe \n - TL",
    "hallowsblade": " hallowsblade \n -",
    "boneblade": "boneblade \n - TL",
    "vampireedge": "vampireedge \n - TL",
    "pumpking": "pumpking\n - TL",
    "snowflake": "snowflake \n - TL",
    "wintersedge": "wintersedge \n - TL",
    "iceshard": "iceshard \n - TL",
    "icedragon": "icedragon \n - TL",
    "battleaxe2": "battle axe 2 \n - TL",
    "handsaw": "handsaw \n - TL",
    "cboneblade": "cboneblade \n - TL",
    "batwing": "batwing \n - TL",
    "spider": "spider \n - TL",
    "hallowsedge": "hallowsedge \n - TL",
    "chromalaser": "Chroma Laser \n - TL",
    "claser": "Chroma Laser \n - TL",
    "cgingerblade": "Chroma Gingerblade \n - TL",
    "slasher": "Slasher \n 10 TL",
    "candy": "Candy Set\n - TL ",
    "sugar": "Candy Set\n - TL ",
    "candyset": "Candy Set \n - TL ",
    "sugarset": "Candy Set \n - TL ",
    "iceset": "İce Set \n - TL",
    "icebreaker": "İce Set \n - TL",
    "iceblaster": "İce Set \n - TL",
    "ewset": "Elderwood Set \n - TL",
    "elderwoodsycthe": "Elderwood Set \n - TL",
    "elderwood": "Elderwood Set \n - TL",
    "elderwoodrevolver": "Elderwood Set \n - TL",
    "ew": "Elderwood Set \n - TL ",
    "ewrevolver": "Elderwood Set \n - TL",
    "ewsycthe": "Elderwood Set \n - TL ",
    "eternalcaneset": "Eternalcane Set \n - TL",
    "ecaneset": "Eternalcane Set \n - TL",
    "lugercane": "Eternalcane Set \n - TL",
    "lcane": "Eternalcane Set \n - TL",
    "eternalcane": "Eternalcane Set \n - TL",
    "ecane": "Eternalcane Set \n - TL",
    "lugercaneset": "Eternalcane Set \n - TL",
    "eternalset": "Eternalcane Set \n - TL",
    "ogset": "Old Glory Set\n - TL",
    "oldglory": "Old Glory Set\n - TL",
    "amerilaser": "Old Glory Set\n - TL",
    "oldgloryset": "Old Glory Set\n - TL",
    "xmasset": "Xmas Set\n - TL",
    "xmas": "Xmas Set\n - TL",
    "jinglegun": "Xmas Set\n - TL",
    "çamağacınabenzeyenbıçak": "Xmas Set\n - TL",
    "virtualset": "Virtual Set\n - TL",
    "blasterset": "Virtual Set\n - TL",
    "blaster": "Virtual Set\n - TL",
    "virtual": "Virtual Set\n - TL",
    "gingerset": "Ginger Set\n - TL",
    "ginger": "Ginger Set\n - TL",
    "gingerluger": "Ginger Set\n - TL",
    "gingerblade": "Ginger Set\n - TL",
    "hallowset": "Hallow Set\n - TL",
    "hallow": "Hallow Set\n - TL",
    "hallowgun": "Hallow Set\n - TL",
    "hallowsycthe": "Hallow Set\n - TL",

}

simgeler = {
    "cgemstone": "https://static.wikia.nocookie.net/murder-mystery-2/images/9/91/Chromagemstone.png/revision/latest?cb=20201201210935",
    "redluger": "https://static.wikia.nocookie.net/murder-mystery-2/images/a/a6/RedLuger_improved.png/revision/latest?cb=20210610134056",
    "greenluger": "https://static.wikia.nocookie.net/murder-mystery-2/images/f/f5/Green_Luger.png/revision/latest?cb=20170314160455",
    "frostbite": "https://static.wikia.nocookie.net/murder-mystery-2/images/f/f2/Frostbite_improved.png/revision/latest?cb=20210607225926",
    "frostsaber": "https://static.wikia.nocookie.net/murder-mystery-2/images/2/29/Frostsaber.png/revision/latest?cb=20180727103659",
    "cookieblade": "https://static.wikia.nocookie.net/murder-mystery-2/images/f/f4/Cookieblade_%28transparent%29.png/revision/latest?cb=20210204082105",
    "peppermint": "https://static.wikia.nocookie.net/murder-mystery-2/images/e/e8/Peppermint_Knife.png/revision/latest?cb=20210204081905",
    "chill": "https://static.wikia.nocookie.net/murder-mystery-2/images/7/7b/Chill.png/revision/latest?cb=20170913205236",
    "eternal1": "https://static.wikia.nocookie.net/murder-mystery-2/images/b/bb/Ete.png/revision/latest?cb=20200226205156",
    "eternal2": "https://static.wikia.nocookie.net/murder-mystery-2/images/8/85/Eternal_2.png/revision/latest?cb=20190128130938",
    "eternal3": "https://static.wikia.nocookie.net/murder-mystery-2/images/a/af/Eternal_III.png/revision/latest?cb=20201129110713",
    "eternal4": "https://static.wikia.nocookie.net/murder-mystery-2/images/8/89/Eternal_IIII.png/revision/latest?cb=20201129110258",
    "nah": "https://i.pinimg.com/originals/c7/9a/33/c79a334626f3043c445099fee86cd382.gif",
    "fıstık": "https://lh3.googleusercontent.com/YUg58BYrPJbP9JUo9vV9iY8_fzolh3Lwwqw7wWA9Wxa-cpRGiFCn4VhGak8yGzeApvRSbhEhNjedcSaJ7nb45Nj9PAES1lzic-1XG-sua8ycNey62EJMlQBB9UVCpavUwEHqWg_yFT2yzpg30Bz3na19CDqgkSGE11OvxW9yQ1BL-AKuXLQZjJ8ilUpjsNSosCZtFHiUWDZ7z_ewET_i_UFSdQ5AfBexi9Om8bGwPDu_ZTqI4N4lp6teLAw1lKyMLEONG7imdUom6sxgaWDI-f6tmVhueyKy3pB2IYJcwaPMKCCWoWnsV15l-rLCM0e_2Tjn3IvSfwCY6Nq15D5US2GqQ8-Cd5JnfJwj_a0R-blLcw-lh7bKJoYfOsf01ozNzWwA9o3R0dCtWFtljbg3FfqCnONPupbVrEaPb9YOVvgmNiSvrGPc7VtBlxeFBzwFs1ys08bwHsx-j4KNerJ2tCcWwUw21QF0OpTndpXPbNNXck77n7j3_uAOfObKrGR_Pb5x82G-3sFXFx0esclUlmw5FfpBIzSRTHAYdonLTClw9GvppmqpwZDGj1cVLBUoxgoZquTlUSayQZ2c9mm7GcP-_3ApVssoRwEpwW0YMl2GzxvWq75mI0GKy2vkS8Be_Eg2d3R4Xx_Qlh7wFZwMSyYqOlibLJnBod7fm9ZjHD2zs1zdFtHIeVZlh3KALAm7pSnNhic2I4ntWLbbvXicvCqBmHaY3j_YWUiG9ZvNT_UeJQiRX-7I_cyO5WdiBTNCE6jkHwgF39cHbAK9TQ=w61-h72-no",
    "lightbringer": "https://static.wikia.nocookie.net/murder-mystery-2/images/e/e8/Lightbringer_v2.png/revision/latest?cb=20201129111035",
    "prismatic": "https://static.wikia.nocookie.net/murder-mystery-2/images/1/16/RobloxScreenShot20200717_133541320_%282%29.png/revision/latest?cb=20201201211109",
    "bioblade": "https://static.wikia.nocookie.net/murder-mystery-2/images/b/bf/Mm2bioblade.png/revision/latest?cb=20201201211421",
    "gemstone": "https://static.wikia.nocookie.net/murder-mystery-2/images/0/0a/Gemstone.png/revision/latest?cb=20201201210714",
    "clockwork": "https://static.wikia.nocookie.net/murder-mystery-2/images/b/b2/Clockwork.png/revision/latest?cb=20190128130431",
    "deathshard": "https://static.wikia.nocookie.net/murder-mystery-2/images/9/99/Deathshard-0-0.png/revision/latest?cb=20190124005942",
    "fang": "https://static.wikia.nocookie.net/murder-mystery-2/images/e/ec/Fang-0.png/revision/latest?cb=20170510182317",
    "flames": "https://static.wikia.nocookie.net/murder-mystery-2/images/2/27/762bf5f41a818fa97e57508183bc88be.png/revision/latest?cb=20170314174612",
    "heat": "https://static.wikia.nocookie.net/murder-mystery-2/images/c/c4/Heat.png/revision/latest?cb=20170510182406",
    "laser": "https://static.wikia.nocookie.net/murder-mystery-2/images/a/a1/Laser.png/revision/latest?cb=20170314160313",
    "luger": "https://static.wikia.nocookie.net/murder-mystery-2/images/f/fa/Lugerv2.png/revision/latest?cb=20201129113059",
    "nightblade": "https://static.wikia.nocookie.net/murder-mystery-2/images/c/c1/Nightblade.png/revision/latest?cb=20190128130546",
    "pixel": "https://static.wikia.nocookie.net/murder-mystery-2/images/3/34/Mm2_pixel.png/revision/latest?cb=20201025192946",
    "saw": "https://static.wikia.nocookie.net/murder-mystery-2/images/0/0a/Saw.png/revision/latest?cb=20170314155813",
    "shark": "https://static.wikia.nocookie.net/murder-mystery-2/images/1/14/Shark.png/revision/latest?cb=20210204081632",
    "tides": "https://static.wikia.nocookie.net/murder-mystery-2/images/8/86/Tides.png/revision/latest?cb=20170314155852",
    "america": "https://static.wikia.nocookie.net/murder-mystery-2/images/4/46/America.png/revision/latest?cb=20170510013349",
    "blood": "https://static.wikia.nocookie.net/murder-mystery-2/images/d/d3/144307188.png/revision/latest?cb=20210121142451",
    "cowboy": "https://static.wikia.nocookie.net/murder-mystery-2/images/9/96/144290769.png/revision/latest?cb=20210121142258",
    "ghost": "https://static.wikia.nocookie.net/murder-mystery-2/images/f/fc/1628e909869d8d7e03c91b86a3378143.png/revision/latest?cb=20170314174408",
    "golden": "https://static.wikia.nocookie.net/murder-mystery-2/images/5/55/Golden.png/revision/latest?cb=20170510013327",
    "vlaser": "https://static.wikia.nocookie.net/murder-mystery-2/images/f/f7/54798135.png/revision/latest?cb=20210121142411",
    "phaser": "https://static.wikia.nocookie.net/murder-mystery-2/images/8/8c/Mm2phaser.png/revision/latest?cb=20201027204109",
    "prince": "https://static.wikia.nocookie.net/murder-mystery-2/images/b/b4/Prince.png/revision/latest?cb=20170510013603",
    "shadow": "https://static.wikia.nocookie.net/murder-mystery-2/images/7/76/C1ba264d6f7d7ef6ade0c3ff1ad42587.png/revision/latest?cb=20170314174449",
    "splitter": "https://static.wikia.nocookie.net/murder-mystery-2/images/3/3f/Splitter.png/revision/latest?cb=20170510013636",
    "eggblade": "https://static.wikia.nocookie.net/murder-mystery-2/images/9/98/Eggblade_improved.png/revision/latest?cb=20210609230310",
    "darkbringer": "https://static.wikia.nocookie.net/murder-mystery-2/images/0/0e/Dark.png/revision/latest?cb=20200902102542",
    "heartblade": "https://static.wikia.nocookie.net/murder-mystery-2/images/6/65/HeartBlade.png/revision/latest?cb=20210310190038",
    "icewing": "https://static.wikia.nocookie.net/murder-mystery-2/images/1/1a/Icewingknife.png/revision/latest?cb=20210221133627",
    "redseer": "https://static.wikia.nocookie.net/murder-mystery-2/images/d/dd/Redseer.png/revision/latest?cb=20200123140034",
    "blueseer": "https://static.wikia.nocookie.net/murder-mystery-2/images/f/f3/1aad7564-2836-43c5-befb-686aedf7bf9b.png/revision/latest?cb=20201211142043",
    "orangeseer": "https://static.wikia.nocookie.net/murder-mystery-2/images/c/c8/OrangeseerNEW.png/revision/latest?cb=20200423164043",
    "purpleseer": "https://static.wikia.nocookie.net/murder-mystery-2/images/5/50/Purpleseer.png/revision/latest?cb=20200423164120",
    "yellowseer": "https://static.wikia.nocookie.net/murder-mystery-2/images/2/25/Yellowseer.png/revision/latest?cb=20200423164002",
    "cseer": "https://static.wikia.nocookie.net/murder-mystery-2/images/2/25/Chromaseer.png/revision/latest?cb=20190725091616",
    "ghostblade": "https://static.wikia.nocookie.net/murder-mystery-2/images/1/10/Ghostbladev2.png/revision/latest?cb=20201129115934",
    "battleaxe": "https://static.wikia.nocookie.net/murder-mystery-2/images/6/63/BattleAxe.png/revision/latest?cb=20171029045445",
    "hallowsblade": "https://static.wikia.nocookie.net/murder-mystery-2/images/6/68/Hallowsblade.png/revision/latest?cb=20201129105952",
    "boneblade": "https://static.wikia.nocookie.net/murder-mystery-2/images/f/fc/Boneblade.png/revision/latest?cb=20190128130908",
    "vampireedge": "https://static.wikia.nocookie.net/murder-mystery-2/images/b/ba/Vampiresedge.png/revision/latest?cb=20201129132821",
    "pumpking": "https://static.wikia.nocookie.net/murder-mystery-2/images/d/d8/Pumpking.png/revision/latest?cb=20171029045613",
    "snowflake": "https://static.wikia.nocookie.net/murder-mystery-2/images/2/22/Snowflake-0.png/revision/latest?cb=20190124005759",
    "wintersedge": "https://static.wikia.nocookie.net/murder-mystery-2/images/f/fb/WinterEdge.png/revision/latest?cb=20180727103649",
    "iceshard": "https://static.wikia.nocookie.net/murder-mystery-2/images/b/ba/IceShard.png/revision/latest?cb=20180727103709",
    "icedragon": "https://static.wikia.nocookie.net/murder-mystery-2/images/5/58/Ice_Dragon2.png/revision/latest?cb=20190203171702",
    "battleaxe2": "https://static.wikia.nocookie.net/murder-mystery-2/images/1/13/BattleAxe2.2.png/revision/latest?cb=20190128130815",
    "handsaw": "https://static.wikia.nocookie.net/murder-mystery-2/images/b/bb/Handsaw_Png.png/revision/latest?cb=20210520152704",
    "cboneblade": "https://static.wikia.nocookie.net/murder-mystery-2/images/a/a4/Chroma_Boneblade.png/revision/latest?cb=20190128130917",
    "batwing": "https://static.wikia.nocookie.net/murder-mystery-2/images/3/31/Batwing_%28Rotated%29.png/revision/latest?cb=20201203192901",
    "spider": "https://static.wikia.nocookie.net/murder-mystery-2/images/8/84/Spider.png/revision/latest?cb=20170510182520",
    "hallowsedge": "https://static.wikia.nocookie.net/murder-mystery-2/images/f/fc/Gfhdh-0.png/revision/latest?cb=20200615213545",
    "claser": "https://static.wikia.nocookie.net/murder-mystery-2/images/2/22/Chromalaser-0.png/revision/latest?cb=20190725092628",
    "chromalaser": "https://static.wikia.nocookie.net/murder-mystery-2/images/2/22/Chromalaser-0.png/revision/latest?cb=20190725092628",
    "cgingerblade": "https://static.wikia.nocookie.net/murder-mystery-2/images/8/80/Chroma_Gingerblade.png/revision/latest?cb=20190101184620",
    "candy": "https://media.discordapp.net/attachments/792515887139127317/792516236658999306/candyset.png",
    "sugar": "https://media.discordapp.net/attachments/792515887139127317/792516236658999306/candyset.png",
    "candyset": "https://media.discordapp.net/attachments/792515887139127317/792516236658999306/candyset.png",
    "sugarset": "https://media.discordapp.net/attachments/792515887139127317/792516236658999306/candyset.png",
    "iceset": "https://lh3.googleusercontent.com/pw/ACtC-3dIkYo-j1var0ms8qFfKpvCV4xI1-cieTuErE5kQEQQW5lDFU1a8oy3cbCNxd4fI_RCH3gHU2RqF-TApq8_BYFeFS4Cc379Y0zxawDJF9Jboj32OPv5nNSFjGdEaS1re5vdihPNAMxpf1VXUqFkjBHYOg=s420-no?authuser=0",
    "iceblaster": "https://lh3.googleusercontent.com/pw/ACtC-3dIkYo-j1var0ms8qFfKpvCV4xI1-cieTuErE5kQEQQW5lDFU1a8oy3cbCNxd4fI_RCH3gHU2RqF-TApq8_BYFeFS4Cc379Y0zxawDJF9Jboj32OPv5nNSFjGdEaS1re5vdihPNAMxpf1VXUqFkjBHYOg=s420-no?authuser=0",
    "icebreaker": "https://lh3.googleusercontent.com/pw/ACtC-3dIkYo-j1var0ms8qFfKpvCV4xI1-cieTuErE5kQEQQW5lDFU1a8oy3cbCNxd4fI_RCH3gHU2RqF-TApq8_BYFeFS4Cc379Y0zxawDJF9Jboj32OPv5nNSFjGdEaS1re5vdihPNAMxpf1VXUqFkjBHYOg=s420-no?authuser=0",
    "ewset": "https://lh3.googleusercontent.com/pw/ACtC-3frGvda5X-883ci5XnRyB08dB36cq9S8Kw6PXnfP4RWAa-Uj61I4fDRRoe9Wz3dWAuBpChQmub6xbjSVelAuwtrruFgXlqn0m8aJ97xGS0H20boagipC9BkIQ2LCjG1WU2B1VjGXMnwscPzBevKdEoRnw=s420-no?authuser=0",
    "elderwoodsycthe": "https://lh3.googleusercontent.com/pw/ACtC-3frGvda5X-883ci5XnRyB08dB36cq9S8Kw6PXnfP4RWAa-Uj61I4fDRRoe9Wz3dWAuBpChQmub6xbjSVelAuwtrruFgXlqn0m8aJ97xGS0H20boagipC9BkIQ2LCjG1WU2B1VjGXMnwscPzBevKdEoRnw=s420-no?authuser=0",
    "elderwood": "https://lh3.googleusercontent.com/pw/ACtC-3frGvda5X-883ci5XnRyB08dB36cq9S8Kw6PXnfP4RWAa-Uj61I4fDRRoe9Wz3dWAuBpChQmub6xbjSVelAuwtrruFgXlqn0m8aJ97xGS0H20boagipC9BkIQ2LCjG1WU2B1VjGXMnwscPzBevKdEoRnw=s420-no?authuser=0",
    "elderwoodrevolver": "https://lh3.googleusercontent.com/pw/ACtC-3frGvda5X-883ci5XnRyB08dB36cq9S8Kw6PXnfP4RWAa-Uj61I4fDRRoe9Wz3dWAuBpChQmub6xbjSVelAuwtrruFgXlqn0m8aJ97xGS0H20boagipC9BkIQ2LCjG1WU2B1VjGXMnwscPzBevKdEoRnw=s420-no?authuser=0",
    "ew": "https://lh3.googleusercontent.com/pw/ACtC-3frGvda5X-883ci5XnRyB08dB36cq9S8Kw6PXnfP4RWAa-Uj61I4fDRRoe9Wz3dWAuBpChQmub6xbjSVelAuwtrruFgXlqn0m8aJ97xGS0H20boagipC9BkIQ2LCjG1WU2B1VjGXMnwscPzBevKdEoRnw=s420-no?authuser=0",
    "ewrevolver": "https://lh3.googleusercontent.com/pw/ACtC-3frGvda5X-883ci5XnRyB08dB36cq9S8Kw6PXnfP4RWAa-Uj61I4fDRRoe9Wz3dWAuBpChQmub6xbjSVelAuwtrruFgXlqn0m8aJ97xGS0H20boagipC9BkIQ2LCjG1WU2B1VjGXMnwscPzBevKdEoRnw=s420-no?authuser=0",
    "ewsycthe": "https://lh3.googleusercontent.com/pw/ACtC-3frGvda5X-883ci5XnRyB08dB36cq9S8Kw6PXnfP4RWAa-Uj61I4fDRRoe9Wz3dWAuBpChQmub6xbjSVelAuwtrruFgXlqn0m8aJ97xGS0H20boagipC9BkIQ2LCjG1WU2B1VjGXMnwscPzBevKdEoRnw=s420-no?authuser=0",
    "eternalcaneset": "https://lh3.googleusercontent.com/pw/ACtC-3dPgO2f1EYGlLM06BxZSkX8oEsS5f1SOdLady77vXhxjK0cplIlgo2okNcnrnimRwRwpMUT6_bK-1v3wY-ZRvrtuUssS0SjFswEzpMVZT_M5WtPFfkBL_tHN63qryDFt7SY5MrA1_VbIWoPdMR7wqKbUg=s450-no?authuser=0",
    "ecaneset": "https://lh3.googleusercontent.com/pw/ACtC-3dPgO2f1EYGlLM06BxZSkX8oEsS5f1SOdLady77vXhxjK0cplIlgo2okNcnrnimRwRwpMUT6_bK-1v3wY-ZRvrtuUssS0SjFswEzpMVZT_M5WtPFfkBL_tHN63qryDFt7SY5MrA1_VbIWoPdMR7wqKbUg=s450-no?authuser=0",
    "lugercane": "https://lh3.googleusercontent.com/pw/ACtC-3dPgO2f1EYGlLM06BxZSkX8oEsS5f1SOdLady77vXhxjK0cplIlgo2okNcnrnimRwRwpMUT6_bK-1v3wY-ZRvrtuUssS0SjFswEzpMVZT_M5WtPFfkBL_tHN63qryDFt7SY5MrA1_VbIWoPdMR7wqKbUg=s450-no?authuser=0",
    "lcane": "https://lh3.googleusercontent.com/pw/ACtC-3dPgO2f1EYGlLM06BxZSkX8oEsS5f1SOdLady77vXhxjK0cplIlgo2okNcnrnimRwRwpMUT6_bK-1v3wY-ZRvrtuUssS0SjFswEzpMVZT_M5WtPFfkBL_tHN63qryDFt7SY5MrA1_VbIWoPdMR7wqKbUg=s450-no?authuser=0",
    "eternalcane": "https://lh3.googleusercontent.com/pw/ACtC-3dPgO2f1EYGlLM06BxZSkX8oEsS5f1SOdLady77vXhxjK0cplIlgo2okNcnrnimRwRwpMUT6_bK-1v3wY-ZRvrtuUssS0SjFswEzpMVZT_M5WtPFfkBL_tHN63qryDFt7SY5MrA1_VbIWoPdMR7wqKbUg=s450-no?authuser=0",
    "ecane": "https://lh3.googleusercontent.com/pw/ACtC-3dPgO2f1EYGlLM06BxZSkX8oEsS5f1SOdLady77vXhxjK0cplIlgo2okNcnrnimRwRwpMUT6_bK-1v3wY-ZRvrtuUssS0SjFswEzpMVZT_M5WtPFfkBL_tHN63qryDFt7SY5MrA1_VbIWoPdMR7wqKbUg=s450-no?authuser=0",
    "lugercaneset": "https://lh3.googleusercontent.com/pw/ACtC-3dPgO2f1EYGlLM06BxZSkX8oEsS5f1SOdLady77vXhxjK0cplIlgo2okNcnrnimRwRwpMUT6_bK-1v3wY-ZRvrtuUssS0SjFswEzpMVZT_M5WtPFfkBL_tHN63qryDFt7SY5MrA1_VbIWoPdMR7wqKbUg=s450-no?authuser=0",
    "eternalset": "https://lh3.googleusercontent.com/pw/ACtC-3dPgO2f1EYGlLM06BxZSkX8oEsS5f1SOdLady77vXhxjK0cplIlgo2okNcnrnimRwRwpMUT6_bK-1v3wY-ZRvrtuUssS0SjFswEzpMVZT_M5WtPFfkBL_tHN63qryDFt7SY5MrA1_VbIWoPdMR7wqKbUg=s450-no?authuser=0",
    "ogset": "https://lh3.googleusercontent.com/pw/ACtC-3c4NSyy5Sw3rnsIDbifKofy2PCM5tXKrb7MdwOzqsqz0EoaEoQNhvcsLAX5hRgSOA9PvXrq_TZNZm-90819cZB-f3GiPFtcxOYy3m3lIV1k1NkRaBukgH_hscIi_oyFITPZZpEgd0s0WfBoIUGhvOlSqA=s450-no?authuser=0",
    "oldglory": "https://lh3.googleusercontent.com/pw/ACtC-3c4NSyy5Sw3rnsIDbifKofy2PCM5tXKrb7MdwOzqsqz0EoaEoQNhvcsLAX5hRgSOA9PvXrq_TZNZm-90819cZB-f3GiPFtcxOYy3m3lIV1k1NkRaBukgH_hscIi_oyFITPZZpEgd0s0WfBoIUGhvOlSqA=s450-no?authuser=0",
    "amerilaser": "https://lh3.googleusercontent.com/pw/ACtC-3c4NSyy5Sw3rnsIDbifKofy2PCM5tXKrb7MdwOzqsqz0EoaEoQNhvcsLAX5hRgSOA9PvXrq_TZNZm-90819cZB-f3GiPFtcxOYy3m3lIV1k1NkRaBukgH_hscIi_oyFITPZZpEgd0s0WfBoIUGhvOlSqA=s450-no?authuser=0",
    "oldgloryset": "https://lh3.googleusercontent.com/pw/ACtC-3c4NSyy5Sw3rnsIDbifKofy2PCM5tXKrb7MdwOzqsqz0EoaEoQNhvcsLAX5hRgSOA9PvXrq_TZNZm-90819cZB-f3GiPFtcxOYy3m3lIV1k1NkRaBukgH_hscIi_oyFITPZZpEgd0s0WfBoIUGhvOlSqA=s450-no?authuser=0",
    "xmasset": "https://lh3.googleusercontent.com/pw/ACtC-3fAQJ8Ujnst22NipOSvWoQwt6C6w3x73ewN6NTuPTceBKZLG-GmEV3dIZjMhJ5SeLw6KAlW42CQHQOEU86qz1nIVZekQRcg2XHEp-6WW0Dobu0FVhTISw7FUEKkIehLgd2daidzTKRr8ZxHrkzNpu1w0w=s450-no?authuser=0",
    "xmas": "https://lh3.googleusercontent.com/pw/ACtC-3fAQJ8Ujnst22NipOSvWoQwt6C6w3x73ewN6NTuPTceBKZLG-GmEV3dIZjMhJ5SeLw6KAlW42CQHQOEU86qz1nIVZekQRcg2XHEp-6WW0Dobu0FVhTISw7FUEKkIehLgd2daidzTKRr8ZxHrkzNpu1w0w=s450-no?authuser=0",
    "jinglegun": "https://lh3.googleusercontent.com/pw/ACtC-3fAQJ8Ujnst22NipOSvWoQwt6C6w3x73ewN6NTuPTceBKZLG-GmEV3dIZjMhJ5SeLw6KAlW42CQHQOEU86qz1nIVZekQRcg2XHEp-6WW0Dobu0FVhTISw7FUEKkIehLgd2daidzTKRr8ZxHrkzNpu1w0w=s450-no?authuser=0",
    "çamağacınabenzeyenbıçak": "https://lh3.googleusercontent.com/pw/ACtC-3fAQJ8Ujnst22NipOSvWoQwt6C6w3x73ewN6NTuPTceBKZLG-GmEV3dIZjMhJ5SeLw6KAlW42CQHQOEU86qz1nIVZekQRcg2XHEp-6WW0Dobu0FVhTISw7FUEKkIehLgd2daidzTKRr8ZxHrkzNpu1w0w=s450-no?authuser=0",
    "virtualset": "https://lh3.googleusercontent.com/pw/ACtC-3dx2lEr9uFeprzrk99XoldZGPRjcVcKozlEicG-iJLI1WIAPVNXxdBYKK3m3KEQMvcewEEvI9bKbY5qMrosNZLm9BCnDsAtsnr6l5uRKRF9ROQU29dZ3ZYrPFNsfMEfOeY4417NsR9ucz6eanIA-kgnqA=s450-no?authuser=0",
    "blasterset": "https://lh3.googleusercontent.com/pw/ACtC-3dx2lEr9uFeprzrk99XoldZGPRjcVcKozlEicG-iJLI1WIAPVNXxdBYKK3m3KEQMvcewEEvI9bKbY5qMrosNZLm9BCnDsAtsnr6l5uRKRF9ROQU29dZ3ZYrPFNsfMEfOeY4417NsR9ucz6eanIA-kgnqA=s450-no?authuser=0",
    "blaster": "https://lh3.googleusercontent.com/pw/ACtC-3dx2lEr9uFeprzrk99XoldZGPRjcVcKozlEicG-iJLI1WIAPVNXxdBYKK3m3KEQMvcewEEvI9bKbY5qMrosNZLm9BCnDsAtsnr6l5uRKRF9ROQU29dZ3ZYrPFNsfMEfOeY4417NsR9ucz6eanIA-kgnqA=s450-no?authuser=0",
    "virtual": "https://lh3.googleusercontent.com/pw/ACtC-3dx2lEr9uFeprzrk99XoldZGPRjcVcKozlEicG-iJLI1WIAPVNXxdBYKK3m3KEQMvcewEEvI9bKbY5qMrosNZLm9BCnDsAtsnr6l5uRKRF9ROQU29dZ3ZYrPFNsfMEfOeY4417NsR9ucz6eanIA-kgnqA=s450-no?authuser=0",
    "gingerset": "https://lh3.googleusercontent.com/pw/ACtC-3egR-k3KdYIPMRFiR4_8EnYc6B7hvwzVZsAjsyVB0xumoxLjTTdPQt_4TG8-6WzydkXraY5_DVKuAbNCyT09pXvzxcFtiFIHbRjrqTk1WZrIcvhHkowpDcCppBeff2911w10A3ByqNqLW-y9H4RdnVkQQ=s450-no?authuser=0",
    "ginger": "https://lh3.googleusercontent.com/pw/ACtC-3egR-k3KdYIPMRFiR4_8EnYc6B7hvwzVZsAjsyVB0xumoxLjTTdPQt_4TG8-6WzydkXraY5_DVKuAbNCyT09pXvzxcFtiFIHbRjrqTk1WZrIcvhHkowpDcCppBeff2911w10A3ByqNqLW-y9H4RdnVkQQ=s450-no?authuser=0",
    "gingerluger": "https://lh3.googleusercontent.com/pw/ACtC-3egR-k3KdYIPMRFiR4_8EnYc6B7hvwzVZsAjsyVB0xumoxLjTTdPQt_4TG8-6WzydkXraY5_DVKuAbNCyT09pXvzxcFtiFIHbRjrqTk1WZrIcvhHkowpDcCppBeff2911w10A3ByqNqLW-y9H4RdnVkQQ=s450-no?authuser=0",
    "gingerblade": "https://lh3.googleusercontent.com/pw/ACtC-3egR-k3KdYIPMRFiR4_8EnYc6B7hvwzVZsAjsyVB0xumoxLjTTdPQt_4TG8-6WzydkXraY5_DVKuAbNCyT09pXvzxcFtiFIHbRjrqTk1WZrIcvhHkowpDcCppBeff2911w10A3ByqNqLW-y9H4RdnVkQQ=s450-no?authuser=0",
    "hallowset": "https://lh3.googleusercontent.com/pw/ACtC-3eT5y5EYWg-pkqBWE8VRznvJpXaG4fig3NZ73TfpInR7VhT3Y6SOAEvMItNTibpbDGMPbpXo6S-oPDbvEsfATnfn8WkwMfUgG0gCgeXHfu9gaXQMaR1i-EXH2GkfYyX7ZPbaUgFNa49yUKh18HZmv6JUA=s450-no?authuser=0",
    "hallow": "https://lh3.googleusercontent.com/pw/ACtC-3eT5y5EYWg-pkqBWE8VRznvJpXaG4fig3NZ73TfpInR7VhT3Y6SOAEvMItNTibpbDGMPbpXo6S-oPDbvEsfATnfn8WkwMfUgG0gCgeXHfu9gaXQMaR1i-EXH2GkfYyX7ZPbaUgFNa49yUKh18HZmv6JUA=s450-no?authuser=0",
    "hallowgun": "https://lh3.googleusercontent.com/pw/ACtC-3eT5y5EYWg-pkqBWE8VRznvJpXaG4fig3NZ73TfpInR7VhT3Y6SOAEvMItNTibpbDGMPbpXo6S-oPDbvEsfATnfn8WkwMfUgG0gCgeXHfu9gaXQMaR1i-EXH2GkfYyX7ZPbaUgFNa49yUKh18HZmv6JUA=s450-no?authuser=0",
    "hallowsycthe": "https://lh3.googleusercontent.com/pw/ACtC-3eT5y5EYWg-pkqBWE8VRznvJpXaG4fig3NZ73TfpInR7VhT3Y6SOAEvMItNTibpbDGMPbpXo6S-oPDbvEsfATnfn8WkwMfUgG0gCgeXHfu9gaXQMaR1i-EXH2GkfYyX7ZPbaUgFNa49yUKh18HZmv6JUA=s450-no?authuser=0",
    "slasher": "https://static.wikia.nocookie.net/murder-mystery-2/images/9/9a/Slasher.png/revision/latest/scale-to-width-down/310?cb=20170314155535",
}


@Bot.event
async def on_ready():
    print("ben hazırım")
    durum.start()


@tasks.loop(seconds=5)
async def durum():
    durum_liste = ["-f (ürün adı)", "-zar", "-set", "-seer", "-eternal"]

    durum = random.choice(durum_liste)
    await Bot.change_presence(activity=discord.Game(name=durum))


@Bot.event
async def on_message(message):
    await Bot.process_commands(message)
    #if message.content.startswith("f"):
        #await message.channel.send(f"{message.author.mention} komutun doğru kullanımı : \n  -f (ürün adı)")

    if message.content.startswith("🚬"):
        liste = ["😢", "🥲", "😭", "😥", "😓", "😕", "😶", "😐"]

        await message.channel.send(f"{random.choice(liste)} :smoking:")




@Bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="giriş-çıkış")
    await channel.send(f"{member.mention} Hoşgeldiniz")
    print(f"{member} Hoşgeldiniz")


@Bot.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.text_channels, name="giriş-çıkış")
    await channel.send(f"{member.mention} Veda etti :(")
    print(f"{member} Veda etti :(")




@Bot.command()
@commands.has_role(848218868480475156)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)


@Bot.command()

async def cekilis0(ctx, arg):
    arg = int(arg)
    sonuc = ""
    b = 0

    kullanicilar = []
    liste = []
    sayimL = []

    sonSayim = ""
    for x in Bot.guilds[0].members:
        x = str(x)
        x = x[:-5]
        kullanicilar.append(x)

    for x in range(arg):
        a = random.choice(Bot.guilds[0].members)

        a = str(a)
        a = a[:-5]
        liste.append(a)

        b += 1
        a = str(b) + "- " + a
        sonuc = sonuc + a + "\n"

    sayac = 0
    for z in kullanicilar:

        for c in range(len(liste)):
            if z == liste[c]:
                sayac += 1
                # print(str(sayac) + " .... " + liste[c])

            else:
                continue

        if sayac != 0:
            sayim = f" {str(sayac)} kere   {z}\n "
            sayimL.append(sayim)
            print(f"{str(sayac)} kere   {z}\n")
        sayac = 0

    for sayimisim in sayimL:
        sonSayim = sonSayim + f" {sayimisim}  \n"
        print(sonSayim)

    await ctx.send(len(sonuc))
    try:
        await ctx.send(f"{sonuc}")
        await ctx.send(f"-----------------------\n\n\n{sonSayim}")
    except:
        await ctx.send(f"-----------------------\n\n\n{sonSayim}")

@Bot.command()
async def kutla(ctx):
    target = await Bot.fetch_user(784845899972083743)
    await target.send("https://www.youtube.com/watch?v=kOvLkkJc_l0")
@Bot.command()
@commands.has_role(850430759096680459)
async def tüm(ctx):
    for x in fiyatlar:
        print(fiyatlar[x])
        print(simgeler[x])
        embed = discord.Embed(title=fiyatlar[x], colour=discord.Colour.from_rgb(252, 15, 192))
        embed.set_thumbnail(url=simgeler[x])
        await ctx.send(embed=embed)


@Bot.command(aliases=["M", "fiyat", "Fiyat", "f", "money", "Money"])
async def m(ctx, *args):
    msj = ""
    for x in range(len(args)):
        kelime = args[x]
        msj = msj + kelime

    msj = msj.lower()
    msj = msj.replace(" ", "")

    choosed = fiyatlar[msj]
    print(msj)

    color = discord.Colour.from_rgb(252, 15, 192)
    if msj == "america" or msj == "blood" or msj == "cowboy" or msj == "ghost" or msj == "vlaser" or msj == "phaser" or msj == "prince" or msj == "shadow" or msj == "splitter" or msj == "golden":
        color = discord.Colour.from_rgb(255, 255, 0)

    if msj == "batwing":
        color = discord.Colour.from_rgb(102, 0, 153)
    if msj == "icewing":
        color = discord.Colour.from_rgb(102, 0, 153)
    embed = discord.Embed(title=choosed, colour=color)
    if msj == "greenluger":
        embed = discord.Embed(title=choosed, colour=color, description="~~ 20 TL ~~")
    embed.set_thumbnail(url=simgeler[msj])

    await ctx.send(embed=embed)


@Bot.command()
async def mesaj(ctx, *args):
    print(type(args))
    user = Bot.get_user(343051107788128256)
    msj = ""
    for x in range(len(args)):
        kelime = args[x]
        msj = msj + kelime

    await user.send(msj)
@Bot.command()
async def log(ctx):
    color = discord.Colour.from_rgb(252, 15, 192)

    embed = discord.Embed(title="Logchopper SET \n - TL", colour=color)
    await ctx.send(embed=embed)

@Bot.command(aliases=["setler", "Setler", "SETLER", "Set", "SET", "setlerimiz"])
async def set(ctx):
    color = discord.Colour.from_rgb(252, 15, 192)

    embed = discord.Embed(title=fiyatlar["candy"], colour=color)
    embed.set_thumbnail(url=simgeler["candyset"])
    await ctx.send(embed=embed)

    embed = discord.Embed(title=fiyatlar["iceset"], colour=color)
    embed.set_thumbnail(url=simgeler["iceset"])
    await ctx.send(embed=embed)

    embed = discord.Embed(title=fiyatlar["eternalcaneset"], colour=color)
    embed.set_thumbnail(url=simgeler["eternalcaneset"])
    await ctx.send(embed=embed)

    embed = discord.Embed(title=fiyatlar["virtualset"], colour=color)
    embed.set_thumbnail(url=simgeler["virtualset"])
    await ctx.send(embed=embed)

    embed = discord.Embed(title=fiyatlar["ewset"], colour=color)
    embed.set_thumbnail(url=simgeler["ewset"])
    await ctx.send(embed=embed)

    embed = discord.Embed(title=fiyatlar["xmasset"], colour=color)
    embed.set_thumbnail(url=simgeler["xmasset"])
    await ctx.send(embed=embed)

    embed = discord.Embed(title=fiyatlar["gingerset"], colour=color)
    embed.set_thumbnail(url=simgeler["gingerset"])
    await ctx.send(embed=embed)

    embed = discord.Embed(title=fiyatlar["hallowset"], colour=color)
    embed.set_thumbnail(url=simgeler["hallowset"])
    await ctx.send(embed=embed)

    embed = discord.Embed(title=fiyatlar["oldgloryset"], colour=color)
    embed.set_thumbnail(url=simgeler["oldgloryset"])
    await ctx.send(embed=embed)


@Bot.command(aliases=["seerlar", "Seerlar", "Seer"])
async def seer(ctx):
    color = discord.Colour.from_rgb(252, 15, 192)

    embed = discord.Embed(title=fiyatlar["blueseer"], colour=color)
    embed.set_thumbnail(url=simgeler["blueseer"])
    await ctx.send(embed=embed)

    embed = discord.Embed(title=fiyatlar["yellowseer"], colour=color)
    embed.set_thumbnail(url=simgeler["yellowseer"])
    await ctx.send(embed=embed)

    embed = discord.Embed(title=fiyatlar["redseer"], colour=color)
    embed.set_thumbnail(url=simgeler["redseer"])
    await ctx.send(embed=embed)

    embed = discord.Embed(title=fiyatlar["orangeseer"], colour=color)
    embed.set_thumbnail(url=simgeler["orangeseer"])
    await ctx.send(embed=embed)

    embed = discord.Embed(title=fiyatlar["purpleseer"], colour=color)
    embed.set_thumbnail(url=simgeler["purpleseer"])
    await ctx.send(embed=embed)

    embed = discord.Embed(title=fiyatlar["cseer"], colour=color)
    embed.set_thumbnail(url=simgeler["cseer"])
    await ctx.send(embed=embed)


@Bot.command()
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

@Bot.command()
async def deneme(ctx):
    await ctx.send("**deneme**")
@Bot.command(aliases=["eternaller", "Eternal", "Eternaller"])
async def eternal(ctx):
    color = discord.Colour.from_rgb(252, 15, 192)

    embed = discord.Embed(title=fiyatlar["eternal1"], colour=color)
    embed.set_thumbnail(url=simgeler["eternal1"])
    await ctx.send(embed=embed)

    embed = discord.Embed(title=fiyatlar["eternal2"], colour=color)
    embed.set_thumbnail(url=simgeler["eternal2"])
    await ctx.send(embed=embed)

    embed = discord.Embed(title=fiyatlar["eternal3"], colour=color)
    embed.set_thumbnail(url=simgeler["eternal3"])
    await ctx.send(embed=embed)

    embed = discord.Embed(title=fiyatlar["eternal4"], colour=color)
    embed.set_thumbnail(url=simgeler["eternal4"])
    await ctx.send(embed=embed)


@Bot.command()
async def avatar(ctx, member: discord.User):
    user = await Bot.fetch_user(member.id)
    #await ctx.send(member.avatar_url)
    await ctx.send(user.avatar_url)




@Bot.command()
async def value(ctx, arg):
    liste = []
    r = requests.get(f"https://murder-mystery-2.fandom.com/wiki/{arg}")
    soup = BeautifulSoup(r.content, "html.parser")
    veri = soup.findAll("div", attrs={"class": "pi-data-value pi-font"})
    for x in veri:
        x = x.text
        liste.append(x)

    await ctx.send(f"{arg}  \n {liste[-1]} ")


@Bot.command()

async def çekiliş(ctx, *args: discord.User):
    liste = []

    for x in args:
        print(x)
        print(x.name)

        liste.append(x)


    print(liste)

    seçim = random.choice(liste)

    id = seçim.id
    id2 = f"<@!{id}>"
    # print(id2)
    embed = discord.Embed(title=f":tada:  KAZANAN  :tada:\n\n      {seçim.name}   ",
                          colour=discord.Colour.from_rgb(252, 255, 255))
    embed.set_thumbnail(url=seçim.avatar_url)
    await ctx.send(embed=embed)
    await ctx.send(id2)


@Bot.command()
async def info(ctx, user: discord.Member):
    await ctx.send(f'{user.mention}\'s id: `{user.id}`')


@Bot.command()
async def msj(ctx, arg):
    for c in Bot.get_all_channels():
        if c.id == 901157476932661308:
            embed = discord.Embed(title=f":robot:\n\n {arg}\n\n :robot:", colour=discord.Colour.from_rgb(20, 10, 255))
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/avatars/848659805438607380/cc6e1b74418485f0d3c7b8fb97417733.webp?size=1024")
            await c.send(embed=embed)




@Bot.command()
async def sayaç(ctx, saat=0, dakika=0, saniye=0):
    if saat <= 0:
        saat = 0
    if dakika >= 60:
        saat += 1
        dakika = 0
    if dakika <= 0:
        dakika = 0
    if saniye >= 60:
        dakika += 1
        saniye = 0
    if saniye <= 0:
        saniye = 0

    embed_one = discord.Embed(title=f"sayaç : {saat} : {dakika} : {saniye}")
    msg = await ctx.send(embed=embed_one)

    while True:
        await asyncio.sleep(delay=1)
        saniye -= 1
        if saniye <= -1:
            dakika -= 1
            saniye = 60
            if saat == 0 and dakika == -1:
                break

            if dakika <= -1:
                saat -= 1
                dakika = 60
                if saat == -1:
                    break
                if saat <= 0:
                    saat = 0

        if saat == 0 and dakika == 0 and saniye == -1:
            break

        embed_two = discord.Embed(title=f"sayaç : {saat} : {dakika} : {saniye}")
        await msg.edit(embed=embed_two)

@Bot.command()
async def yazıtura(ctx):
    yazi = "https://i.hizliresim.com/qANl5V.png"
    tura = "https://i.hizliresim.com/Z5zV8z.png"
    dik = "https://c.tenor.com/MDVk57u-7KgAAAAd/yaz%C4%B1tura-dik-geldi.gif"

    para = ["YAZI","TURA"]
    sayi = random.randint(1,100)
    if sayi <= 2:
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


@Bot.command()
async def developer_info(ctx):
    yas = 2021-2002
    bilgi = f"""--------------------------------------------------
isim / soy isim : Mehmet Kaya
instagram : mehmet__kaya1903
Bölümü : Bilgisayar Mühendisliği
--------------------------------------------------
            
    """
    await ctx.send(bilgi)
@Bot.command()
async def şovalye_memo(ctx):
    embed=discord.Embed(title="Şovalye Memo Maceraya Açılan Kapıdan Geçiyor",colour=discord.Colour.from_rgb(172,67,67))
    embed.set_image(url="https://cdn.discordapp.com/attachments/901157476932661308/907403638006231050/pixil-gif-drawing_5.gif")
    msg = await ctx.send(embed=embed)

    time.sleep(1.7)

    embed = discord.Embed(title="Şovalye Memo Maceraya Açılan Kapıdan Geçti.",
                          colour=discord.Colour.from_rgb(172, 67, 67))
    embed.set_image(url="https://cdn.discordapp.com/attachments/901157476932661308/907403596512002059/pixil-frame-20_1.png")
    await msg.edit(embed=embed)

@Bot.command()
async def şovalye_memo2(ctx):
    embed = discord.Embed(title="Şovalye Memo bekliyor",
                          colour=discord.Colour.from_rgb(172, 67, 67))
    embed.set_image(
        url="https://media3.giphy.com/media/UvazEIPfeNN3GdbTO3/giphy.gif?cid=790b76118d910560124df6501d8da4727d17bbd292095d84&rid=giphy.gif&ct=s")
    msg = await ctx.send(embed=embed)

@Bot.command(aliases=["fb"])
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

@Bot.command()
async def fboku(ctx):
    file = open("feedbacks.txt","r")
    feedbacks = file.read()
    await ctx.send(feedbacks)

@Bot.command()
async def müksayı(ctx,arg1:int):
    toplam = 0

    for x in range(arg1-1):
        x+=1
        if arg1 % x == 0:
            toplam += x
            print(x)
        else:
            print("devam")
            continue
    if toplam == arg1:
        print(f"{arg1} mükemmel sayıdır")
        await ctx.send(f"{arg1} mükemmel sayıdır")
    else:
        print("mük sayı değil")


@Bot.command()
async def müksayılar(ctx):
    arg1=0
    while True:
        arg1+=1
        toplam = 0
        for x in range(arg1 - 1):
            x += 1
            if arg1 % x == 0:
                toplam += x
                print(x)
            else:
                continue
        if toplam == arg1:
            print(f"{arg1} mükemmel sayıdır")
            await ctx.send(f"{arg1} mükemmel sayıdır")


@Bot.command()
async def müksayıformül(ctx, arg1: int):
    toplam = 0

    k = arg1


    bolenK=1
    sorgulanacak_sayi = ( 2**(k-1) )*(2**k -1)
    print(sorgulanacak_sayi)
    #for x in range(sorgulanacak_sayi-1):
     #   pass
    x = 0
    while(x<sorgulanacak_sayi):
        print(f"bolen kat sayısı {bolenK}")
        bolen = bolenK*(2**x)
        if bolen == sorgulanacak_sayi:
            break
        if sorgulanacak_sayi % bolen == 0:
            toplam+=bolen
            print(bolen)
            x += 1
        else:
            bolen -= 1
            if sorgulanacak_sayi % bolen == 0:
                toplam += bolen
                print(bolen)
                bolenK = bolen
                x = 1
            else:
                break





    if toplam == sorgulanacak_sayi:
        print(f"{sorgulanacak_sayi} mükemmel sayıdır")
        await ctx.send(f"{sorgulanacak_sayi} mükemmel sayıdır")
@Bot.command()
async def tümmüksayılar(ctx):


    asalSayi= 2
    sayac = 0

    while True:
        toplam = 0
        control = 0
        #### ASAL SAYI BULMA KISMI ###
        i = 2
        while(i<asalSayi):
            if asalSayi % i == 0:
                asalSayi += 1
                control = 1
                break
            else:
                i+=1
                continue


        if control == 0:


            k = asalSayi
            print(f"{k} asal bir sayıdır")
            asalSayi += 1
            ### Mükemmel Sayı Bulma Kısmı ###
            bolenK = 1
            sorgulanacak_sayi = (2 ** (k - 1)) * (2 ** k - 1)
            print(sorgulanacak_sayi)
            # for x in range(sorgulanacak_sayi-1):
            #   pass
            x = 0
            while (x < sorgulanacak_sayi):
                print(f"bolen kat sayısı {bolenK}")
                bolen = bolenK * (2 ** x)
                if bolen == sorgulanacak_sayi:
                    break
                if sorgulanacak_sayi % bolen == 0:
                    toplam += bolen
                    print(bolen)
                    x += 1
                    continue
                else:
                    bolen -= 1
                    if sorgulanacak_sayi % bolen == 0:
                        toplam += bolen
                        print(bolen)
                        bolenK = bolen
                        x = 1
                        continue
                    else:
                        break

            if toplam == sorgulanacak_sayi:
                sayac+= 1
                print(f"{sayac}- kat sayısı {asalSayi -1}{sorgulanacak_sayi} mükemmel sayıdır")
                await ctx.send(f"{sayac}-  kat sayısı {asalSayi -1}- {sorgulanacak_sayi} mükemmel sayıdır")



@Bot.command()
async def bolenler(ctx,arg1:int):
    liste = []

    sayi = arg1
    i = 2
    while (i < sayi):
        if (sayi % i == 0):
            liste.append(i)
        i += 1
    await ctx.send(f"{liste}\n\n bölen sayısı : {len(liste)}")
    print(liste)
Bot.run("BURAYA DİSCORD BOT TOKENİ GELİR")
