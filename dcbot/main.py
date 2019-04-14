import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import sayac
import youtube_dl
#import calma

Client = discord.Client() #Initialise Client --
client = commands.Bot(command_prefix = ".") #Initialise client bot

players = {}

my_var = 1  # pylint: disable=unused-variable

kari_sayar = int(0)

argolar = ["ORSPU","RTE","ZENCI","DÖL","EGE","AMCUK","OÇ","OC","AQ","NEGRO","TUNA"]
bypass_list =[]
@client.event 
async def on_ready():
    print("Botumuz Hazırdır :)") #This will be called when the bot connects to the server

@client.command(pass_context = True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)

@client.event
async def on_message(message):
    contents = message.content.split(" ")
    for word in contents : 
        if word.upper() in argolar:
            if not message.author.id in bypass_list:
                try:
                    await client.delete_message(message)
                    userID = message.author.id

                    await client.send_message(message.channel, "ADAM OL <@%s>!!! BURA AİLE SVSİ" % userID)
                except discord.errors.NotFound:
                    return
    if message.content.upper() == "YENİLİKLER" :
        await client.send_message(message.channel, """
        Botumuzun artık argo kelimlere karsı gelismiş bir algoritmik defans sistemi vardır.

        Dert çekenler için özel gelistirilmis dinleme modu ile odada size katılıp dert ortağı,çok iyi bir dinleyici olabilecek

        Yeni cami eklendi 

        
        """)


    if message.content == "açım":
        await client.send_message(message.channel, "https://www.yemeksepeti.com/edirne")
    elif message.content == "fakir açım":
        await client.send_message(message.channel, "https://www.yemeksepeti.com/edirne-yemek-firsatlari")
    elif message.content == "cami":
        await client.send_message(message.channel, ":mosque:")
    elif message.content == "ulu cami":
        await client.send_message(message.channel, ":mosque: :mosque: :mosque:")
    elif message.content == "seni seviyorum borbot":
        await client.send_message(message.channel, ":heart: :yellow_heart: :green_heart:")
    elif message.content.upper() == "GURT":
        await client.send_message(message.channel,"cCc :flag_tr: cCc",)
    elif message.content.upper() == "KARI":
        for i in (1,10):
            kari_sayar +=i
        await client.send_message(message.channel, print(kari_sayar))
    if message.content.upper().startswith('!PING'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Pong!" % (userID))
    elif message.content.upper() == "ATAKAN":
        await client.send_message(message.channel, "atakan = :soccer:")
    elif message.content.upper() == "KARA DELIK":
        await client.send_message(message.channel,"https://cdn.eso.org/images/screen/eso1907a.jpg")
    elif message.content == "uludağ":
        await client.send_message(message.channel,":mountain:")

client.run("NTY0NzY2NTUyNjI5NDQ0NjA5.XKtPhw.AokzPx4cS3RYwXf5Zn55bze4lDA")

