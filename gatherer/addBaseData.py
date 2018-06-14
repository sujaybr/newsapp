import requests
import newspaper
# from news_classifier_api import categorizeApi

inp = [
# "https://www.indiatoday.in/",
# "https://www.techcrunch.com/",
# "https://www.firstpost.com/category/politics",
# "https://www.news18.com/politics/",
# "http://www.espn.in/",
# "http://www.espn.in/cricket/team/_/id/6/india/",
# "https://sports.ndtv.com/",
# "http://movies.ndtv.com/",
# "https://gadgets.ndtv.com/",
"https://economictimes.indiatimes.com/news/politics-nation",
# "https://www.ndtv.com/business",
# "https://www.timesofindia.indiatimes.com/",
# "https://www.hindustantimes.com/",
# "https://www.deccanherald.com/",
# "http://www.thehindu.com/",
# "http://www.bbc.com/",
# "https://edition.cnn.com/world",
# "https://www.wired.com/",
# "https://news.google.com/news/?ned=in&gl=IN&hl=en-IN",
# "https://www.ft.com/"
]

out = []
source = inp[0]

# for source in inp:
paper = newspaper.build(source, memoize_articles=False)

urls = []
for article in paper.articles:
    urls.append(article.url)
    # print (article.url)

print ("got all the urls")
print (len(urls))

for i in urls:

    # for getting only movies data from movies.ndtv.com
    # if "movies" not in i:
    #     continue

    # # for getting only  data from gadgets.ndtv.com
    # if "gadgets" not in i:
    #     continue

    # for getting only  data from movies.ndtv.com
    if "politics" not in i:
        continue

    try:
        art = newspaper.Article(i)
        art.download()
        art.parse()

        print ("processing " + str(urls.index(i)))
        print (art.text[:100])
        out.append(art.text)

    except:
        print ("errorrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")



out = "".join(out)
print (len(out))

print ("written to data files")

a = open("../ml/BCC_news_data/scraped_data/politics.txt", 'a')
a.write(out)
a.close()


# r = requests.get("https://newsapi.org/v2/everything?q=stocks&sortBy=publishedAt&apiKey=e8704cf44921496593e63fc898537993")

# r = r.json()

# out = []
# for i in r['articles']:
#     out.append(i['title'] + " " + i['description'])

# out = "".join(out)
# print (out)

# a = open("../ml/BCC_news_data/scraped_data/business.txt", 'a')
# a.write(out)

# print (r)
