from bs4 import BeautifulSoup
import requests
#getting data from the wesite
response=requests.get(url="https://news.ycombinator.com/")
content=response.text
soup=BeautifulSoup(content,"html.parser")
text=soup.find_all(name="span",class_="titleline")
text_list=[item.get_text() for item in text]
links_list=[item.find("a").get("href") for item in text]
point=soup.find_all(name="span", class_="score")
article_point=[int(item.get_text().split()[0])for item in point]
max_value=max(article_point)
index_no=article_point.index(max_value,0)
#we can get based on their points
print(f"news with highest point is {text_list[index_no]} \n it's link: {links_list[index_no]}")