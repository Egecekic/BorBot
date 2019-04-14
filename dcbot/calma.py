import discord 
import youtube_dl
from discord.ext import commands


players = {}
Client = discord.Client()
client = commands.Bot(command_prefix = ".")

@client.event 
async def on_ready():
    print("Botumuz Hazırdsır :)")



@client.command(pass_context = True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)
@client.command(pass_context = True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()

@client.command(pass_context = True)
async def play (ctx,url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    players[server.id]= player
    player.start()

client.run("NTY0NzY2NTUyNjI5NDQ0NjA5.XKtPhw.AokzPx4cS3RYwXf5Zn55bze4lDA")