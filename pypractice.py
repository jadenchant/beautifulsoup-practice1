import requests
from bs4 import BeautifulSoup


url = "https://www.rottentomatoes.com/top/bestofrt/"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
leftColumn = soup.find('div', class_='col-left-center col-full-xs')
titles = leftColumn.find_all('a', class_='unstyled articleLink')
f = open("rottentomatos.txt", 'w+')
for title in titles:
    t = title.text
    title = t[0:len(t) - 7]
    f.write(title)
f.close()