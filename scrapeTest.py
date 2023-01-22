import requests
from bs4 import BeautifulSoup

url = "https://ncit.edu.np/news"

#Getting the HTML
response=requests.get(url) 
content=response.content

#parsing the HTML
soup=BeautifulSoup(content,"html.parser")
title=soup.title
first_anchor=soup.a
print(first_anchor)


#Getting all anchor tags <<Add it into links only if it is not avaliable>>
anchors=soup.find_all('a')
print(type(soup))
print(type(title))
new_links=list()
for links in anchors:
    new_links.append(links.get("href")) #Ncit page mah full absolute address naii deko raixa

print(new_links)
