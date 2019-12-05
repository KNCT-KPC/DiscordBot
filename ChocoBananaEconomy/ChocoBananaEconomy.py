import discord
import os
import re
import sys
client = discord.Client()


@client.event 
async def on_ready():
    print("Welcome to ChocoBananaEconomy!")
    
    #print(os.getcwd())


@client.event
async def on_message(message):
    if message.author.bot:
       return

    rate=200
    prefix="CB"

    #cwd = os.getcwd()

    if message.content.startswith(prefix+"shutdown"):
        await message.channel.send("See you.")
        await client.change_presence(status = discord.Status.offline)
        sys.exit()

    elif message.content.startswith(prefix+"help"):
        await message.channel.send("円とチョコバナナ[CB]を変換するBotです。\n"+prefix+"help:このヘルプを表示します。\n"+prefix+"prefix:現在設定されているprefixを表示します。\n"+prefix+"rate:現在のレートを表示します。\n"+prefix+"cb <数字>:円をチョコバナナ(CB)へ換算します。\n"+prefix+"yen:チョコバナナ(CB)を円へ換算します。\n"+prefix+"shutdown:Botをシャットダウンします。")
    
    elif message.content.startswith(prefix+"prefix"):
        await message.channel.send("現在のprefixは "+prefix+" です。")

    elif message.content.startswith(prefix+"rate"):
        await message.channel.send("現在のレートは1CB="+str(rate)+"円です。")

    elif message.content.startswith(prefix+"cb"):
        msg=message.content
        msg=msg.lstrip(prefix+"cb")
        yen=float(msg)
        yen=str(yen/rate)
        await message.channel.send(msg+"円＝"+yen+"CB")

    elif message.content.startswith(prefix+"yen"):
        msg=message.content
        msg=msg.lstrip(prefix+"yen")
        CB=float(msg)
        CB=str(CB*rate)
        await message.channel.send(msg+"CB＝"+CB+"円")


client.run('Token')