import discord
import asyncio
import os

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        await client.send_message(message.channel, 'test!!!!')

    elif message.content.startswith('!say'):
        await client.send_message(message.channel, 'leave message')
        msg = await client.wait_for_message(timeout=15.0, author=message.author)

        if msg is None:
            await client.send_message(message.channel, '15초내로 입력해주세요. 다시시도: !say')
            return
        else:
            await client.send_message(message.channel, msg.content)

access_token = os.environ["BOT_TOKEN"]
client.run('access_token')
