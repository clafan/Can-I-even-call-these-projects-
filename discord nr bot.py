# Automatically counts, meant to cheese "counting" channels
# I reccomend using 2 accs for this

import discord, asyncio

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        

    async def on_message(self, message):
        if message.channel.id != 1075477571078205541 or message.author == self.user:
            return
            
        await asyncio.sleep(3)
        try:
            
            number = int(message.content)
            
            await message.channel.send(str(number + 1)) 
        except ValueError:
            pass

client = MyClient()
client.run('Your Token here')