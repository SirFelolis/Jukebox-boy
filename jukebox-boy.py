import asyncio
import discord
from discord.ext import commands

print("Logging in...")

@bot.event
async def on_ready():
    print('------------------')
    print('Logged in as ' + bot.user.name)
    print('ID: ' + bot.user.id)
    print('------------------')


bot.run('MTk2NjM2NjMxNjE1MTQzOTM2.ClH-9Q.p4YTlhIm_QPX_wCTXy486Suzrwk')
