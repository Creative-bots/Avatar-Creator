import os
import discord
from discord.ext import commands

bot =  commands.Bot(command_prefix='!', intents=discord.Intents.all())

async def load_cogs():
    print('Loading cogs...')
    for file in os.listdir(os.getcwd() + '/cogs'):
        if file.endswith('.py') and file != '__init__.py':
            await bot.load_extension('cogs.' + file[:-3])
            print(f'Loaded {file}')


@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! 🏓 {bot.latency * 1000}')

@bot.event
async def on_ready():
    await load_cogs()
    print(f'Connected to Discord as {bot.user}')

bot.run(os.environ.get('DISCORD_TOKEN'))
