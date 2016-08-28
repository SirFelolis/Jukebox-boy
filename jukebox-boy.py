import asyncio
import discord
from discord.ext import commands
import tokens

bot = commands.Bot(command_prefix='!', description="Jukebox boi!!!!!!!!!!!!!!")

if not discord.opus.is_loaded():
	discord.opus.load_opus()

print('Logging in...')

@bot.command(pass_context=True)
async def play(ctx, url):
	voice = await bot.join_voice_channel(ctx.message.author.voice.voice_channel)
	player = await voice.create_ytdl_player(url=url)
	player.start()

@bot.command(pass_context=True)
async def join(ctx):
	voice = await bot.join_voice_channel(ctx.message.author.voice.voice_channel)

@bot.event
async def on_ready():
    print('------------------')
    print('Logged in as ' + bot.user.name)
    print('ID: ' + bot.user.id)
    print('------------------')


bot.run(tokens.key)
