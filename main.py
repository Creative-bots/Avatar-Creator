import os
import discord
from discord.ext import commands

bot =  commands.Bot(command_prefix='!', intents=discord.Intents.all())

async def load_cogs():







@bot.command()
async def ping(ctx):


@bot.event
async def on_ready():



bot.run(os.environ.get('DISCORD_TOKEN'))