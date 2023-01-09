import os
import discord

import selenium.webdriver as webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

from dotenv import load_dotenv 

load_dotenv()
TOKEN = os.getenv('TOKEN')
client=discord.Client(intents=discord.Intents.default()) 


#Paremeters
user_agent=os.getenv('USER_AGENT')
driver_path="msedgedriver.exe"
edge_service=Service(driver_path) #A class that is responsible for starting and stopping the msedgedriver
edge_options=Options() #initialization
edge_options.add_argument(f'user-agent:{user_agent}')

#Loading the browser
#browser.get("https://ncit.edu.np/news")

@client.event
async def on_ready():
    print("The bot has logged in")    
    browser=webdriver.Edge(service=edge_service , options=edge_options) #using microsoft edge browser
    
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
browser.quit()