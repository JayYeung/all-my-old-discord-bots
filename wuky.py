import discord
import random
import hashlib
import requests
import time
import json


class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        args = message.content.split(" ")

        if('{0.author}'.format(message)=="weird idea#6667" or args[0]!="^"):
            print("POOP")
            return;

        if(args[1]=="join"):
            myString="uh trying to join *"+message.author.voice.channel.name+"*"
            await message.channel.send(myString)

            vc = await message.author.voice.channel.connect()
        
        elif (args[1] == "leave"):
            myString="uh trying to leave *"+message.author.voice.channel.name+"*"
            await message.channel.send(myString)
            
            for vc in client.voice_clients:
                if vc.guild == message.guild:
                    await vc.disconnect()


client = MyClient()
client.run('ODg3MDQ2OTAwNDc2NDM2NTEw.YT-czQ.JY6FSaq9u1FUkjF9IDlhpW2UkLg')
