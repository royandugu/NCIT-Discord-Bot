import os
import discord

from dotenv import load_dotenv 

load_dotenv()

TOKEN = os.getenv('TOKEN')
client=discord.Client() 

@client.event
async def on_ready():
    print(f"Logged in as {format(client)}")

client.run(TOKEN)