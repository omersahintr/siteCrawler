import requests as req

siteUrl = input("Enter the site url: ")

spider = req.get(siteUrl)
print(spider.text)