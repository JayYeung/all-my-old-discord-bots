import discord
import random

client = discord.Client()

@client.event
async def on_ready():
    #information
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if('{0.author}'.format(message)=="Voice#4597"):
        return
    args=message.content.split(" ")
    
    if(args[0]=="join"):
        myString="uh trying to join *"+message.author.voice.channel.name+"*"
        await message.channel.send(myString)

        vc = await message.author.voice.channel.connect()
    
    elif (args[0] == "leave"):
        myString="uh trying to leave *"+message.author.voice.channel.name+"*"
        await message.channel.send(myString)
        
        for vc in client.voice_clients:
            if vc.guild == message.guild:
                await vc.disconnect()
    elif(args[0] == "play" ):
        for vc in client.voice_clients:
            guild = vc.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source='cuteminion.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)


client.run('NzUzODQwODQ3ODkxNDY0MjIy.X1sC_w.qzS7halJr2xmRtpeiJ6u_8XuUhc')
