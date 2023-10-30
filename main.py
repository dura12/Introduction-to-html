from bs4 import BeautifulSoup
import requests

response=requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
content=response.text
soup=BeautifulSoup(content,"html.parser")
title=soup.find_all(name="h3", class_="title")
all_movies=[(item.get_text()) for item in title]
all_movies.reverse()
with open("movies.txt","w",encoding="utf-8") as file:
    for item in all_movies:
        file.write(f"{item}\n")




















































