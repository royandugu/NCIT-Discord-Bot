import os
import discord

from dotenv import load_dotenv 
from selenium import webdriver

load_dotenv()

TOKEN = os.getenv('TOKEN')
client=discord.Client(intents=discord.Intents.default()) 

#Loading the browser
browser=webdriver.Edge() #using microsoft edge browser
browser.get("https://ncit.edu.np/news")

@client.event
async def on_ready():
    print("The bot has logged in")    

@client.event
async def on_message(message):
    authorName=message.author #The one who sent the message
    channelName=message.channel #The channel name where they are typing
    content=message.content #The messsage content (currently empty)

    if authorName == client.user: #Making sure the bot doesn't reply to itself 
        return 
    
    if (content.lower() == "hi" or content.lower() == "hello"):
        await message.channel.send(f"Hello {authorName}")
    elif (content.lower() == "bye"):
        await message.channel.send(f"Bye {authorName}")
    else:
        await message.channel.send("I don't understand you cause I am dumb")
    
    print(f"{authorName} has messaged in {channelName}")

    
client.run(TOKEN)