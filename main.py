import discord
import asyncio
from discord import Webhook, AsyncWebhookAdapter
import aiohttp

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online)
    print('logged in as Melony')

@client.event
async def on_message(message):
    if "MessageType.premium_guild" in str(message.type):
        channel = client.guilds[0].get_channel(897614176783073311)
        print(channel)
        embed = discord.Embed(title="SERVER BOOST | Axols Palace", description=f"We have a new boost", color=(16750330))
        await message.channel.send(embed=embed)

@client.event
async def on_member_join(member):
    print(f'{member.name} has joined the server')
    channel = client.guilds[0].get_channel(897614176783073311)
    print(channel)
    embed = discord.Embed(title="MEMBER JOIN | Axols Palace", description=f"{member.name} has joined the server. Axol is really happy to see you.", color=(3140255))
    embed.set_thumbnail(url=member.avatar_url)
    await channel.send(embed=embed)
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url('WEBHOOK TOKEN HERE', adapter=AsyncWebhookAdapter(session))
        await webhook.send(f'Hello {member.name} We are glad you are able to join us. Please make sure you read the rules and enjoy your stay here')

@client.event
async def on_member_remove(member):
    print(f'{member.name} has left the server')
    channel = client.guilds[0].get_channel(897614176783073311)
    print(channel)
    embed = discord.Embed(title="MEMBER LEAVE | Axols Palace", description=f"{member.name} has left the server. Axol questions why", color=(16711680))
    await channel.send(embed=embed)



client.run("INSERTBOTTOKEN")
