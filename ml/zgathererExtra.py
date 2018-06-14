import newspaper
from news_classifier_api import categorizeApi

inp = [
"https://www.indiatoday.in/",
"https://www.techcrunch.com/",
"https://www.timesofindia.indiatimes.com/",
"https://www.hindustantimes.com/",
"https://www.deccanherald.com/",
"http://www.thehindu.com/",
"http://www.bbc.com/",
"https://edition.cnn.com/world",
"https://www.wired.com/",
"https://news.google.com/news/?ned=in&gl=IN&hl=en-IN",
"https://www.ft.com/"
]

def getNewsData():
    for source in inp:
        paper = newspaper.build(source, memoize_articles=False)

        urls = []
        for article in paper.articles:
            urls.append(article.url)
            # print (article.url)

        # print (urls)

        for i in urls:
            art = newspaper.Article(i)
            art.download()
            art.parse()

            item = {
                "title": art.title,
                "body": art.text,
            }

            print (item)

# source = "https://www.bbc.com/",
# paper = newspaper.build(source, memoize_articles=False) 
# urls = []
# print (source)
# for article in paper.articles:
#     urls.append(article.url)
#     print (article.url)
#     # print (article.url)

# print (urls)

# for i in urls:
#     art = newspaper.Article(i)
#     art.download()
#     art.parse()

#     item = {
#         "title": art.title,
#         "body": art.text,
#         "cat": categorizeApi(art.text)
#     }
#     print (item)
