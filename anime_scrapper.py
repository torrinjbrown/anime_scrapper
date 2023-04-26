#This is going to scrap the information from My Anime List Website and have it inputed to the user_anime.py




#Importing beautifulsoup to be able to parse and grab the page contents of the site
from bs4 import BeautifulSoup
from urllib.request import urlopen

#Importing request so there can be a pull request for the html information on the site
import requests

#Creating a url name to hold the url of the anime season
url = "https://myanimelist.net/anime/season"
#Using the page name to be able to get the url for the site
page = requests.get(url)


#Soup will hold parsing the html contents 
#page.content grabs the contents of the site
soup = BeautifulSoup(page.text, "html.parser")
#Results will help find the elements id 

# Creating a for loop to be able to grab all of the header 3 tags
for header in soup.find_all("h2"):
    if 
    for score in soup.find_all("div", class_="scormem-item score score-label score-8"):
    #Prints the text for the html
        
        print(header.text.strip())
        print(score.text.strip())
#results = soup.find(id="scormem-container")


#print(results.prettify())

#anime_elements = results.find_all(div="")

#for anime_element in anime_elements:
    #title_element = anime_element.find("h2", class_="h3_anime_subtitle")
    #score_element = anime_element.find("div", class_="title")
    #print(title_element.text)
    #print(score_element.txt)

# page = urlopen(url)

# html_bytes = page.read()
# html = html_bytes.decode("utf-8")

# print(html)