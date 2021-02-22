import discord 

client = discord.client

@client.event
async def on_ready():
  print('We have loggin as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
   return

  if message.content.startwith('#hello'):
    await message.channel.send('Hello')

client.run






