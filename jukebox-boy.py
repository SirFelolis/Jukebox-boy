import asyncio
import discord
from discord.ext import commands
import tokens

if not discord.opus.is_loaded():
	discord.opus.load_opus()

bot = commands.Bot(command_prefix="!", description="Jukebox boi")

user_agent = "Insert user agent here"

players = {}
default_vol = 100

# @commands.group(pass_context=True)
# async def musique(ctx):
#     if ctx.invoked_subcommand is None:
#        bot.say("Sorry my dude, it's not wednesay")

@bot.command(name="join", pass_context=True)
async def join_vc_and_play_stream(ctx, *, channel: discord.Channel = None):
    """Joins a channel"""
    try:
        if channel is None:
            # Tell user they're a retard and need to spesify what channel
            await bot.say("```xl\nTell me what channel!```")

            # Exit out of the function to make sure we don't do anything stupid like try and join None
            return

        # Set a voice client object
        voice_client = await bot.join_voice_channel(channel)

        # Stereo audio bitch
        voice_client.encoder_options(sample_rate=48000, channels=2)

        player = voice_client.create_ffmpeg_player("http://listen.moe:9999/stream", headers={"User-agent": user_agent})

        player.volume = default_vol / 100

        players.update({ctx.message.server.id: player})

        player.start()
        await bot.say("```xl\nJoined {0.channel} to play weeb music```".format(voice_client))
    except asyncio.TimeoutError:
        await bot.say("```xl\nTimed out trying to enter the hood.```")
    except discord.ClientException:
        await bot.say("```xl\nCan't go ditchin' people for sushi.```")
@bot.command(name="!weeb", pass_context=True)
async def start_weeb_music(ctx):
    # Tune in to weeb radio
    player = voice_client.create_ffmpeg_player("http://listen.moe:9999/stream", headers={"User-agent": user_agent})
    players.update({ctx.message.server.id: player})
    player.start()

@bot.command(name="pause", pass_context=True)
async def pause_audio_stream(ctx):
    """Pauses the musique"""
    player = players[ctx.message.server.id]

    player.pause()

    await bot.say("```xl\nWho stopped the damn music?!```")

@bot.command(name="resume", pass_context=True)
async def resume_audio_stream(ctx):
    """Unpauses the musique"""
    if players[ctx.message.server.id] is None:
        await bot.say("```xl\nThere's no music queued```")
    player = players[ctx.message.server.id]

    player.resume()

    await bot.say("```xl\nYou damn right```")

@bot.command(name="vol", pass_context=True)
async def change_volume(ctx, volume: int = 100):
    player = players[ctx.message.server.id]
    player.volume = volume / 100

    if (player.volume * 100) > 200:
        await bot.say("```xl\nNuh uh, I don't wanna go deaf```")
        return
    await bot.say("```py\nJust turned this knob to {}, that 'kay with y'all?```".format(str(volume)))

@bot.command(name="check_vol", pass_context=True)
async def check_volume( ctx):
    """ Checks the volume for the servers voice channel that it's in"""
    player = players[ctx.message.server.id]
    await bot.say(player.volume*100)

@bot.command(name="leave", pass_context=True)
async def leave_vc(ctx):
    """Leaves the voice channel and stops the stream"""
    voice = bot.voice_client_in(ctx.message.server)
    # If the bot isn't in a voice channel
    if voice is None:
        await bot.say("```xl\nNu uh, I'm nowhere buddy```")
        return
    player = players[ctx.message.server.id]
    player.stop()
    await voice.disconnect()
    # Pop the player from the list
    players.pop(ctx.message.server.id)



bot.run(tokens.key)


