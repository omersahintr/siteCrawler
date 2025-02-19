import requests as req
from bs4 import BeautifulSoup

url = input("Web Site: ")
connectUrl = req.get(url)
soupWebText = BeautifulSoup(connectUrl.text, "html.parser")


def h1_counter(url):
    i_1=0
    for h1s in soupWebText.find_all("h1"):
        if h1s.text != None:
            i_1+=1
            print("H1",h1s.text)
    print("H1 Count: ",i_1)
    h2_counter(url)

def h2_counter(url):
    i_2=0
    for h2s in soupWebText.find_all("h2"):
        if h2s.text != None:
            i_2+=1
            print("\tH2",i_2,"-", h2s.text)
    print("H2 Count: ",i_2)
    h3_counter(url)

def h3_counter(url):
    i3=0
    for h3s in soupWebText.find_all("h3"):
        if h3s.text != None:
            i3+=1
            print("\tH3", i3, "-",h3s.text)
    print("H3 Count: ", i3)
try:
    h1_counter(url) # h1 heading content
except:
    pass

