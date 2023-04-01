import requests
from bs4 import BeautifulSoup

####extract p tags text to .txt file
def getStory():
    file.write(title.text + "\n")
    for line in article.find('div', class_="story").children:
        file.write(line.text)
    file.write("\n")


# open file
file = open("articles.txt", "w", -1)
# URL for cbc news in windsor
URL = "https://www.cbc.ca/news/canada/windsor"
resp = requests.get(URL)
soup = BeautifulSoup(resp.text, 'html.parser')

#parse main page for each article
for link in soup.find_all('a', class_="card"):
    article_link = "https://www.cbc.ca/"+link.get('href')
    new_resp = requests.get(article_link)
    article = BeautifulSoup(new_resp.text, 'html.parser')
    ###process text from new page
    title = article.find('h1', class_="detailHeadline")
    if title is not None:
        getStory()
##print(soup.prettify())