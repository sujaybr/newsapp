import requests
from bs4 import BeautifulSoup

all = [
"https://economictimes.indiatimes.com/rssfeedsdefault.cms",
"http://zeenews.india.com/rss/asia-news.xml",
"http://zeenews.india.com/rss/world-news.xml",
"http://zeenews.india.com/rss/india-national-news.xml",
"https://www.reddit.com/r/popular.rss",
"https://www.reddit.com/r/all.rss",
"https://www.reddit.com/r/headlines.rss",
"https://www.reddit.com/r/news.rss",
"https://economictimes.indiatimes.com/rssfeedstopstories.cms"
]

tech = [
"https://gadgets.ndtv.com/rss/feeds",
"https://gadgets.ndtv.com/rss/news",
"https://gadgets.ndtv.com/rss/reviews",
"https://gadgets.ndtv.com/rss/features",
"http://zeenews.india.com/rss/technology-news.xml",
"https://economictimes.indiatimes.com/tech/rssfeeds/13357270.cms"
"https://gadgets.ndtv.com/rss/opinion",
"https://gadgets.ndtv.com/rss/mobiles/feeds",
"https://gadgets.ndtv.com/rss/android/feeds",
"https://gadgets.ndtv.com/rss/apps/feeds",
"https://gadgets.ndtv.com/rss/apps/feeds",
"https://gadgets.ndtv.com/rss/internet/feeds",
"https://auto.ndtv.com/rss/newsrss",
"https://gadgets.ndtv.com/rss/science/feeds",
"https://www.reddit.com/r/tech.rss",
"https://www.reddit.com/r/technology.rss",
"https://www.reddit.com/r/technews.rss",
"https://www.reddit.com/r/gadgets.rss",
"https://gadgets.ndtv.com/rss/games/feeds",
"https://gadgets.ndtv.com/rss/culture/feeds",
"https://gadgets.ndtv.com/rss/india/feeds",
"https://www.hindustantimes.com/rss/tech-news/rssfeed.xml",
]

sports = [
"https://sports.ndtv.com/rss/all",
"https://www.reddit.com/r/sports.rss",
"https://www.reddit.com/r/nba.rss",
"https://sports.ndtv.com/rss/cricket",
"https://sports.ndtv.com/rss/football",
"https://sports.ndtv.com/rss/hockey",
"http://zeenews.india.com/rss/sports-news.xml",
"https://economictimes.indiatimes.com/industry/sports/rssfeeds/58571631.cms",
"http://www.thehindu.com/sport/?service=rss"
]

politics = [
"http://www.rediff.com/rss/election.xml",
"https://www.reddit.com/r/politics.rss",
"https://www.reddit.com/r/IndianPolitics.rss",
"https://www.reddit.com/r/rajneeti.rss",
"https://www.reddit.com/r/indiadiscussion.rss",
"https://www.reddit.com/r/PoliticalDiscussion.rss",
"https://www.reddit.com/r/india.rss",
]

business = [
"http://www.rediff.com/rss/moneyrss.xml",
"https://www.reddit.com/r/business.rss",
"https://www.reddit.com/r/finance.rss",
"https://www.reddit.com/r/Entrepreneur.rss",
"https://www.reddit.com/r/startups.rss",
"http://www.rediff.com/rss/bslide.xml",
"https://www.ft.com/world/asia-pacific/india?format=rss",
"http://zeenews.india.com/rss/business.xml",
"http://www.thehindu.com/business/?service=rss"
]

entertainment = [
"https://www.reddit.com/r/entertainment.rss",
"https://www.reddit.com/r/hometheater.rss",
"https://www.reddit.com/r/marvelstudios.rss",
"http://www.rediff.com/rss/moviesrss.xml",
"http://www.rediff.com/rss/moviesinterrss.xml",
"http://zeenews.india.com/rss/science-environment-news.xml",
"http://zeenews.india.com/rss/entertainment-news.xml"
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

def scrapeForWordAndCat(cat, word):
    if cat == "business":
        urls = business[:] + all[:]
    elif cat == "sports":
        urls = sports[:] + all[:]
    elif cat == "politics":
        urls = politics[:] + all[:]
    elif cat == "entertainment":
        urls == entertainment[:] + all[:]
    elif cat == "tech":
        urls = tech[:] + all[:]

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

            collect += "".join(para)
            news_data.append(collect)
            print(news_data)

    res = []
    for i in news_data:
        if word in i:

            # write the data to the category file dynamically
            f = open('./userData/' + word + '.txt', 'w')
            f.write(i)
            res.append(i)

    # print (res)
    return "".join(res)

# scrapeForWordAndCat("sports", "cricket")
