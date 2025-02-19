import requests as req
from bs4 import BeautifulSoup

siteUrl = input("Entry URL: ") #"https://omersahin.com.tr"
foundLinks = []

def make_req(url):
    spider = req.get(url)
    soup = BeautifulSoup(spider.text, "html.parser")
    return soup

# HTML Parse Process:

def crawler(url):
    countLink = 1
    links = make_req(url)

    for linkhref in links.find_all("a"): #<a href="https....">
        foundLink = linkhref.get("href") # href="https...."

        if foundLink:
            if "#" in foundLink:
                foundLink = foundLink.split("#")[0]
            if foundLink not in foundLinks:
                foundLinks.append(foundLink)
                print(countLink, "-", foundLink)
                crawler(foundLink) #recursive process.
        countLink += 1
try: #for error passing
    crawler(siteUrl)
except:
    pass


