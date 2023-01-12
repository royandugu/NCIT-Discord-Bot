import os
import discord
import requests

from bs4 import BeautifulSoup
from dotenv import load_dotenv 

#Fetching token and setting up the bot as client
load_dotenv()
TOKEN = os.getenv('TOKEN')
client=discord.Client(intents=discord.Intents.default()) 

#Scrape sight
url="https://ncit.edu.np/news"


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

# @tasks.loop(seconds=10) //Here we will scrap like scrap every 10 seconds or so
# async def loop():
#     print("I'm running!")
#     # your repetitive task


client.run(TOKEN)