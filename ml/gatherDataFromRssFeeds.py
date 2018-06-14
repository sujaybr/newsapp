import requests
from bs4 import BeautifulSoup

urls = [
"https://www.hindustantimes.com/rss/topnews/rssfeed.xml",
"https://gadgets.ndtv.com/rss/feeds",
"https://gadgets.ndtv.com/rss/news",
"https://gadgets.ndtv.com/rss/reviews",
"https://gadgets.ndtv.com/rss/features",
"https://gadgets.ndtv.com/rss/opinion",
"https://gadgets.ndtv.com/rss/mobiles/feeds",
"https://gadgets.ndtv.com/rss/android/feeds",
"https://gadgets.ndtv.com/rss/apps/feeds",
"https://gadgets.ndtv.com/rss/apps/feeds",
"https://gadgets.ndtv.com/rss/internet/feeds",
"https://gadgets.ndtv.com/rss/india/feeds",
"https://gadgets.ndtv.com/rss/games/feeds",
"https://gadgets.ndtv.com/rss/science/feeds",
"https://gadgets.ndtv.com/rss/culture/feeds",
"https://gadgets.ndtv.com/rss/science/feeds",
"https://sports.ndtv.com/rss/all",
"https://auto.ndtv.com/rss/newsrss",
]

def scrape():
    for url in urls:
        print ("url " + url)
        r = requests.get(url)
        soup = BeautifulSoup(r.content,'xml')

        news_data = []

        data = soup.findAll('item')

        for rows in data:
            collect = {}
            collect['title'] = rows.title.text
            collect['description'] = rows.description.text
            link = rows.link.text
            c = requests.get(link)
            next_soup = BeautifulSoup(c.content,'html5lib')
            paragraph = next_soup.findAll('p')
            para = []

            for r in paragraph:
                para.append(r.text)

            collect['content'] = para
            news_data.append(collect)
            print(news_data)
    return news_data

def scrapeForWord(cat):
    for url in urls:
        print ("url " + url)
        r = requests.get(url)
        soup = BeautifulSoup(r.content,'xml')

        news_data = []

        data = soup.findAll('item')

        for rows in data:
            collect = ""
            collect += rows.title.text
            collect += rows.description.text
            link = rows.link.text
            c = requests.get(link)
            next_soup = BeautifulSoup(c.content,'html5lib')
            paragraph = next_soup.findAll('p')
            para = []

            for r in paragraph:
                para.append(r.text)

            collect += para
            news_data.append(collect)
            print(news_data)

    res = []
    for i in news_data:
        if cat in i:
            res.append(i)

    return res

scrape()

