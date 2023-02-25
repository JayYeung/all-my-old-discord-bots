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
        KEY = "e79ff87e-249d-44ed-9428-0986c9268773"

        if('{0.author}'.format(message)=="weird idea#6667" and args[0]!="/sc"):
            print("POOP")
            return;     
        if(args[0]=="/sc"):
            if(len(args)==1):
                await message.channel.send("specify second arg (staff, ping, or check)")
                return
            with open('C:/Users/mayps/AppData/Local/Programs/Python/Python37-32/staff.json') as f:
                myDict = json.load(f)

            if(args[1]=="staff" or args[1]=="ping"):
                if(len(args)==2):
                    await message.channel.send("specify third arg (add, remove, or list)")
                    return
                person=args[1]
                if(args[2]=="add"):
                    if(len(args)==3):
                        await message.channel.send("specify who you want to add to the list (e.i. /sc staff add rukt)")
                    else:
                        for i in args[3:]:
                            b = requests.get(url="https://api.mojang.com/users/profiles/minecraft/"+i)
                            if(i in myDict[person]):
                                myString=i+" has been added already!"
                                await message.channel.send(myString)
                            elif(not b.status_code==200 and args[1]!="ping"):
                                await message.channel.send(i+" is not a valid username!")
                            else:
                                myString="adding "+i+"!"
                                await message.channel.send(myString)
                                myDict[person].append(i)
                    await message.channel.send(myDict[person])
                elif(args[2]=="delete" or args[2]=="remove"):
                    if(len(args)==3):
                        await message.channel.send("specify who you want to delete to your list (e.i. /sc staff delete rukt) or delete the whole list with /sc staff delete ALL")
                    elif(args[3].lower()=="all"):
                        myDict[person]=[]
                    else:
                        for i in args[3:]:
                            if(i in myDict[person]):
                                myString="deleting "+i+"!"
                                await message.channel.send(myString)
                                myDict[person].remove(i)
                            else:
                                myString=i+" is not in the list already!"
                                await message.channel.send(myString)
                    await message.channel.send(myDict[person])
                elif(args[2]=="list"):
                    await message.channel.send(myDict[person])
            if(args[1]=="check" or args[1]=="online"):
                onpit=[]
                on=[]
                off=[]
                for i in myDict["staff"]:
                    #await message.channel.send(i)
                    b = requests.get(url="https://api.mojang.com/users/profiles/minecraft/"+i);
                    if(not b.status_code == 200):
                        await message.channel.send(i+" is not a valid username! please remove it from ur list")
                        continue
                    uuid = b.json()["id"];
                    r = requests.get(url = "http://api.hypixel.net/status?key="+KEY+";uuid="+uuid)
                    data = r.json()
                    if(data['session']['online']):
                        if(data['session']['gameType']=='PIT'):
                            onpit.append(i)
                        else:
                            on.append(i)
                    else:
                        off.append(i)

                check=False
                for i in onpit:
                    if(i not in myDict["pit"]):
                        await message.channel.send(i+" joined pit")
                        check=True
                for i in on:
                    if((i not in myDict["pit"]) and (i not in myDict["online"])):
                        await message.channel.send(i+" joined hypixel")   
                        check=True
                        
                myDict["pit"]=onpit
                myDict["online"]=on
                myDict["offline"]=off
                await message.channel.send(myDict["pit"])
                await message.channel.send(myDict["online"])
                await message.channel.send(myDict["offline"])
                if(check):
                    for j in myDict["ping"]:
                        await message.channel.send(j)
                if(len(args)==3 and args[2]=="once"):
                    return;
                await message.channel.send("/sc online")

            with open('C:/Users/mayps/AppData/Local/Programs/Python/Python37-32/staff.json', 'w') as f:
                json.dump(myDict, f)
        
        

        


client = MyClient()
client.run('NjkyNjE0MjkzOTQ2MTA1OTU3.XnxFUw.vm6gia7nZw9V6JSx1e1mwwtRP0M')
