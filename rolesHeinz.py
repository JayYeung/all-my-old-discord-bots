import discord
import random
import hashlib
import requests
import json
import math
from discord.utils import get


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.content == 'give me admin':
            #role = get(message.server.roles, name='Admin')
            await client.add_roles(message.author, "Admin")
        
        KEY = "e79ff87e-249d-44ed-9428-0986c9268773"
        args = message.content.split(" ")

        ign=""
        if(args[0]=="/im"):
            if(len(args)==1):
                await message.channel.send("specify ign")

            NAME = args[1]

            # Query Mojang to get UUID
            b = requests.get(url="https://api.mojang.com/users/profiles/minecraft/"+NAME);
            if(not b.status_code==200):
                await message.channel.send("enter a valid username please")
                return;
            uuid = b.json()["id"];


            # Query HypixelAPI to check status of Player
            r = requests.get(url = "http://api.hypixel.net/player?key="+KEY+";uuid="+uuid)
            data = r.json()

            #dumb stuff to get level
            BASE = 10000; GROWTH = 2500;
            REVERSE_PQ_PREFIX = -(BASE - 0.5 * GROWTH) / GROWTH;
            REVERSE_CONST = REVERSE_PQ_PREFIX * REVERSE_PQ_PREFIX;
            GROWTH_DIVIDES_2 = 2 / GROWTH;
            lvl=int((1 + REVERSE_PQ_PREFIX + math.sqrt(REVERSE_CONST + GROWTH_DIVIDES_2 * data["player"]["networkExp"])))
            
                
            await message.channel.send(myString)
            



client = MyClient()
client.run('NzUyNjQwMTcyNjU4Nzg2MzQ2.X1akyA.i2RvlgtSUXyMA8wd_ROA5ppmS9c')
