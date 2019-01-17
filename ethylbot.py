import asyncio
import discord
import random

TOKEN = 'NTM1NDM2MjcwOTMxODA0MTYx.DyIJdA.UQrkj7d1at-3Gz94X2zUHZQfIrI'
client = discord.Client()

insults = ["you stupid cunt", "fucking faggot", "dumb fucking retard", "neck yourself cunt", "grow a brain shithead", "jump off a cliff nibba"]

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(':insult'):
        args = message.content.split(" ")
        if len(args) > 1:
            msg = args[1] + " " + insults[random.randint(0, len(insults) - 1)]
            await client.send_message(message.channel, msg)
        else:
            msg = '{0.author.mention} '.format(message) + insults[random.randint(0, len(insults) - 1)]
            await client.send_message(message.channel, msg)
    if message.content.startswith(':ascii'):
        with open('ascii.png', 'rb') as picture:
            msg = 'julsberts ascii table {0.author.mention}'.format(message)
            await client.send_message(message.channel, msg)
            await client.send_file(message.channel, picture)
    if message.content.startswith(':blitz'):
            msg = 'https://blitzresearch.itch.io/blitzplus'
            await client.send_message(message.channel, msg)
    if message.content.startswith(':blitzplus'):
            msg = 'https://blitzresearch.itch.io/blitzplus'
            await client.send_message(message.channel, msg)
    if message.content.startswith(':devcpp'):
            msg = 'https://sourceforge.net/projects/orwelldevcpp/'
            await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
