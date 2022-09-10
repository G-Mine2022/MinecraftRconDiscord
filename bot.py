import discord
from discord.ext import commands
from discord import utils
from mcrcon import MCRcon
server = MCRcon('server ip', 'rcon password', port=your_port)
server.connect()

intents = discord.Intents.all()
TOKEN = "token" #put your token here

channel = 00000 #channel id
bot = commands.Bot(command_prefix=('/'), intents=intents)
bot.remove_command( 'help' )

@bot.command()
async def cmd(ctx, cmd):
    if ctx.channel.id == channel:
        await ctx.send('Server output:\n'+server.command(cmd.replace('-', ' ')))#command usage: /cmd say-123

bot.run(TOKEN)
