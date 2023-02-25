
# Helper libraries
import discord

bow=['Arrow Armory', 'Bottomless Quiver', 'Chipping', 'Critically Rich',
     'Faster than their shadow', 'Fletching', 'First Shot', 'Gold Boost',
     'Gold Bump', 'Jumpspammer', 'Mixed Combat', 'Moctezuma', 'Pants Radar',
     'Parasite', 'Pin Down', 'Push comes to shove', 'Spammer and Proud',
     'Sprint Drain', 'Sniper', 'Strike Gold', 'Sweaty', "What doesn't kill you",
     'Wasp', 'XP Boost', 'Lucky Shot', 'Mega Longbow',
     'Pullbow', 'Telebow', 'True Shot', 'Volley']
pant=['Billy', 'Boo-boo', 'Creative', 'Cricket', 'Critically Funky',
      'Critically Rich', 'Counter-Offensive', 'Danger Close',
      'David and Goliath', 'Diamond Allergy', 'Eggs', 'Electrolytes',
      'Excess', 'Gold Boost', 'Gold Bump', 'Golden Heart', 'Gotta go fast',
      'Hearts', 'Hunt the Hunter', 'Last Stand', 'Lodbrok', 'McSwimmer',
      'Mirror', 'Negotiator', '"Not" Gladiator', 'Pants Radar', 'Pebble',
      'Peroxide', 'Prick', 'Protection', 'Respawn: Absorption', 'Respawn: Resistance',
      'Revitalize', 'Self Checkout', 'Steaks', 'Strike Gold', 'TNT', 'XP Boost',
      'Assassin', 'Divine Miracle', 'Double-jump', 'Escape Pod', "Gomraw's Heart",
      'Instaboom', 'Phoenix', 'Pit Blob', 'Singularity', 'Snowballs', 'Snowman Army', 'Wolf Pack']
sword=['Spoiler: Berserker', 'Bounty Reaper', 'Bruiser', 'Bullet Time', 'Combo: Damage',
       'Combo: Heal', 'Combo: Swift', 'Combo: XP', 'Counter-Janitor', 'Critically Rich',
       'Crush', 'Diamond Stomp', 'Duelist', 'Fancy Raider', 'Grasshopper', 'Gold and Boosted',
       'Gold Boost', 'Gold Bump', 'Guts', 'King Buster', 'Lifesteal', 'Moctezuma', 'Pain Focus',
       'Pitpocket', 'Pants Radar', 'Punisher', 'Revengeance', 'Revitalize', 'Sierra', 'Shark',
       'Sharp', 'Strike Gold', 'Sweaty', 'XP Boost', 'Billionaire',
       "Combo: Perun's Wrath", 'Combo: Stun', 'Executioner', 'Gamble', 'Healer',
       'Hemorrhage', 'Knockback', 'Speedy Hit', 'The Punch']
mysticType=['Mystic Bow', 'Mystic Sword', 'Mystic Pant']


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        args = message.content.split(" ")
        if(args[0] != "/rate"):
            return;
        itemType=args[1];
        lives=int(args[2]);
        maxLives=int(args[3]);
        numberOfEnchants=int((len(args)-4)/2)
        enchants=[0, 0, 0]
        enchantLevel=[0, 0, 0]
        tokens=0
        for i in range(numberOfEnchants):
            enchantLevel[i]=int(args[2*i+5])
            tokens+=enchantLevel[i]
        if(itemType.lower()=='bow'):
            itemType=0
        elif(itemType.lower()=='sword'):
            itemType=1
        elif(itemType.lower()=='pant'):
            itemType=2
        else:
            await message.channel.send('What is a '+itemType)
            return

        price=max(1, (itemType+1)*lives*tokens/maxLives)
        willSay='I think the '+mysticType[itemType]+' with '+str(lives)+'/'+str(maxLives)+' is worth '+str(price)+ ' of fresh.'
        await message.channel.send(willSay)
        print('Message from {0.author}: {0.content}'.format(message))


client = MyClient() 
client.run('NjkyNTIzOTczNjUyNTEyODk4.XpIXIw.13fDIlw-nlSqOqBlkrnFSr7QdFY')
