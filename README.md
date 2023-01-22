# Dependencies
1. discord (obviously)
2. bs4 (BeautifulSoup)
3. requests
4. python-dotenv

## Note
1. Learn about this intents thingy
2. We are not being able to access message content because of some options fix them << still we don't even need message content but if we want to add some bot interfaces>>
3. I don't know try Chrome


## Problem
Let's say euta certain range mah yesle data scrap gari raheko hunxa. Then how do we detect that the thing that we just found is new one (a new post)

1. Scrapping gareko part maii link thappiyo vane 
2. Bot le afno previous message sanga compare garxa (feasable). First figure out ki naya link thappiyo vane pani list ko kun chain position mah thappinxa. Then specifically check that position ko link bot le pahila message gareko link ko naii content ho ki naya content ho (or just store that position link somewhere).

## The massive problem is that if the website is updated, the bot will crash. So, Graph API can be another solution