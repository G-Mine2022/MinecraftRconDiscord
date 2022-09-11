import discord
from discord.ext import commands
from discord import utils
from mcrcon import MCRcon
server = MCRcon('server ip', 'rcon password', port=your_port)
server.connect()

intents = discord.Intents.all()
TOKEN = "token" #put your token here

channel_cmd = 00000 #channel id
channel_send = 00000 #channel id

bot = commands.Bot(command_prefix=('/'), intents=intents)
bot.remove_command( 'help' )

@bot.command()
async def cmd(ctx, *,cmd):
    if ctx.channel.id == channel_cmd:
        await ctx.send('Server output:\n'+server.command(cmd))#command usage: /cmd say 123
@bot.command()
async def send(ctx, ch_id, *, message):
    if ctx.channel.id == channel_send:
        channel = bot.get_channel(int(ch_id))
        await channel.send(message)

bot.run(TOKEN)
