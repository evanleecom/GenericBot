from discord.ext import commands
from settings import Settings, logging

bot = commands.Bot(command_prefix="$")

@bot.event
async def on_ready():
    logging.info('Client is ready')
    logging.info('%s: %s' % (bot.user.id, bot.user.name))

@bot.event
async def on_error(error):
    logging.error('%s Error raised at:', error)

@bot.command(pass_context=True)
async def ping(ctx):
    # Get the latency of the bot
    latency = bot.latency  # Included in the Discord.py library
    # Send it to the user
    await ctx.send(latency)

@bot.command(pass_context=True)
async def cat(ctx):
    await ctx.send("meow")

@bot.command(pass_context=True)
async def count(ctx):
    await ctx.send("one")

@bot.command(pass_context=True)
async def nigger(ctx):
    await ctx.send("https://media.tenor.com/images/97334fa8ceb27ac60731d68a9b1e48b8/tenor.gif")

@bot.command(pass_context=True)
async def jailbait(ctx):
    await ctx.send("https://media1.tenor.com/images/1de67159288c2583f1d457cb19b49462/tenor.gif?itemid=13450966")

@bot.command(pass_context=True)
async def blowjob(ctx):
    await ctx.send("https://images.sex.com/images/pinporn/2017/01/28/300/17283928.gif")

if __name__ == "__main__":
    logging.info('Application Start')
    bot.run(Settings['token'])
    