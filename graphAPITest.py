import facebook as fb
import os

from dotenv import load_dotenv

load_dotenv()
GRAPH_API_TOKEN = os.getenv("GRAPH_API_TOKEN")
myPage=fb.GraphAPI(GRAPH_API_TOKEN)

content=myPage.get_object('me/feed') #Bruh it fetches all the data
data=content['data'] #This gets all our data
#Get request to me/feed->data list ko last ko content