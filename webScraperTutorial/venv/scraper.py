import urllib
import urllib.request
from bs4 import BeautifulSoup

theUrl = "https://twitter.com/realDonaldTrump"
thePage = urllib.request.urlopen(theUrl)
soup = BeautifulSoup(thePage, "html.parser")

# print(soup.title.text)

# print(soup.findAll('a')[0])

# print(soup.find('a'))

print(soup.find('div', {"class":"ProfileHeaderCard"}).find('p').text)

i = 1

for tweets in soup.findAll('div', {"class":"content"}):
    print(i)
    print(tweets.find('p').text)
    i = i+1



