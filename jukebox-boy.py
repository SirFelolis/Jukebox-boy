import asyncio
import discord
from discord.ext import commands
import tokens

if not discord.opus.is_loaded():
	discord.opus.load_opus()

bot = commands.Bot(command_prefix="!")

#class Musique:

#	def __init__self(self, bot):
#		self.bot = bot
#		self.players = {}
#		self.default_vol = 100

#	@commands.group(pass_context=True)
#	async def musique(self, ctx):
#		if ctx.invoked_subcommand is None:
#			self.bot.say("Sorry my dude, it's not wednesay")

#	@musique.command(name="join", pass_context=True)
#	async def join_vc_and_play_stream(self, ctx, *, channel: discord.Channel = None):
#		try:
#			voice_client = await self.bot.join_voice_channel(channel)

@bot.command(pass_context=True)
async def play(ctx, url):
	voice = await bot.join_voice_channel(ctx.message.author.voice.voice_channel)
	player = await voice.create_ytdl_player(url=url)
	player.start()

@bot.command(pass_context=True)
async def join(ctx):
	voice = await bot.join_voice_channel(ctx.message.author.voice.voice_channel)

print('Logging in...')

@bot.event
async def on_ready():
  print('------------------')
  print('Logged in as ' + bot.user.name)
  print('ID: ' + bot.user.id)
  print('------------------')

bot.run(tokens.key)
