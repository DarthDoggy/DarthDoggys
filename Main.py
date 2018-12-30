import discord
from discord.ext import commands
import os

@bot.event
async def on_ready():
  print('Logged in as')
  print(bot.user.name)
  print(bot.user.id)
  
bot = commands.Bot(command_prefix=("d."))

@bot.command(pass_context=True)
async def ping(ctx):
    """Pings the bot and gets a response time."""
    pingtime = time.time()
    pingms = await bot.say("Pinging...")
    ping = (time.time() - pingtime) * 1000
    await bot.edit_message(pingms, "Pong! :ping_pong: ping time is `%dms`" % ping)

bot.run(os.environ['BOT_TOKEN'])
