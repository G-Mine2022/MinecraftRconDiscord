import discord
from discord.ext import commands
from discord import utils
from mcrcon import MCRcon
server = MCRcon('95.216.62.180', '11EBE8FAAD79635586', port=25573)
server.connect()

intents = discord.Intents.all()
TOKEN = "MTAxMDA4MTYyMzk0Mjg4OTQ4Mg.Gtx9jK.6ltCaUDDTIJwByylMhfMW_Ri4_jJ7csfIbGx3k"

channel = 1009732910343016448
bot = commands.Bot(command_prefix=('/'), intents=intents)
bot.remove_command( 'help' )

@bot.command()
async def cmd(ctx, cmd):
    if ctx.channel.id == channel:
        await ctx.send('Server output:\n'+server.command(cmd.replace('_', ' ')))

bot.run(TOKEN)
