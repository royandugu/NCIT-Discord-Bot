import os
import discord

from dotenv import load_dotenv 

load_dotenv()

TOKEN = os.getenv('TOKEN')
client=discord.Client(intents=discord.Intents.default()) 

@client.event
async def on_ready():
    print(f"Logged in as {format(client)}")

@client.event
async def on_message(message):
    print(message)

client.run(TOKEN)