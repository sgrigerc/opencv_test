from bs4 import BeautifulSoup
from urllib.request import urlopen
html = urlopen("https://en.wikipedia.org/wiki/Python").read().decode('utf-8')
s = str(html)
soup = BeautifulSoup(s, 'html.parser')
for a in soup.find_all('a', href=True):
    print(a['href'])