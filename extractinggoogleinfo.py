import urllib.request
from bs4 import BeautifulSoup

wikiURL = "https://en.wikipedia.org/wiki/Google"
URL = urllib.request.urlopen(wikiURL)


soup = BeautifulSoup(URL, "html.parser")

text = soup.get_text()
print(text)
outFile = open("output.txt", "w")
with open('output.txt', 'w', encoding='utf-8') as f:
    print(text, file=f)
outFile.close()