#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File              : dev/ml/nltk/news/news_freq_document_density.py
# Author            : Sujay <sujaybr9@gmail.com>
# Last Modified By  : Sujay <sujaybr9@gmail.com>

from math import log as l
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import newspaper
import requests
from time import gmtime, strftime
from nltk.stem import PorterStemmer
import getExtraCategories
# from bccDataLoad_for_density import *
#extra to be removed
import operator
from pymongo import MongoClient


mongo = MongoClient("mongodb://raghu:raghu@ds113640.mlab.com:13640/newsdb")
db = mongo['newsdb']

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
"http://www.ndtv.com/",
"https://news.google.com/news/?ned=in&gl=IN&hl=en-IN",
"https://www.ft.com/",
"http://www.espn.in/",
"https://economictimes.indiatimes.com"
]

#get the data
def getFreqDist(data):
	global tech_file, business_file, sport_file, entertainment_file, politics_file
	if data == "business":
		data = [ps.stem(w) for w in word_tokenize(getBusiness()) if w not in stop_words]
		business_file = set(data)
	elif data == "entertainment":
		data = [ps.stem(w) for w in word_tokenize(getEntertainment()) if w not in stop_words]
		entertainment_file = set(data)
	elif data == "politics":
		data = [ps.stem(w) for w in word_tokenize(getPolitics()) if w not in stop_words]
		politics_file = set(data)
	elif data == "sport":
		data = [ps.stem(w) for w in word_tokenize(getSports()) if w not in stop_words]
		sport_file = set(data)
	else:
		data = [ps.stem(w) for w in word_tokenize(getTech()) if w not in stop_words]
		tech_file = set(data)

	# data = [ps.stem(w) for w in data if w not in stop_words]
	data = nltk.FreqDist(data)

	# print(data.most_common(50))
	return data

def compute_document_density(data):
	global tech_file, business_file, sport_file, entertainment_file, politics_file

	count = 0
	if data in politics_file:
		count += 1
	if data in entertainment_file:
		count += 1
	if data in sport_file:
		count += 1
	if data in tech_file:
		count += 1
	if data in business_file:
		count += 1

	if count == 0:
		return 0
	else:
		return l(5 / count)

stop_words = stopwords.words('english') + ['said' + 'v']
ps = PorterStemmer()
business_file = entertainment_file = politics_file = sport_file = tech_file = []

#data
print ("loading data")
# business = getFreqDist("business")
# print ()
# entertainment = getFreqDist("entertainment")
# print ()
# politics = getFreqDist("politics")
# print ()
# sport = getFreqDist("sport")
# print ()
# tech = getFreqDist("tech")
# tech.plot(20)

print ()


print ("fetching data for classification")
allCats = getExtraCategories.getAllCategories()
for i in allCats:
    r = requests.get("https://newsapi.org/v2/everything?q=" + i + "&sortBy=publishedAt&apiKey=6d4c3258977f4ee0b8b1b2ff98675730&language=en&pageSize=100")
    data = r.json()

    for j in data['articles']:
        
        item = {
                "title": j['title'],
                "body": j['description'],
                "url": j['url'],
                "datetime": strftime("%d-%m-%Y", gmtime()),
                "cat": i
        }
        print (item)
        db.newsdata.insert(item)


#for source in inp:
#        try:
#            paper = newspaper.build(source, memoize_articles=False)

#            print ("loaded paper")

#            urls = []
#            for article in paper.articles:
#                    urls.append(article.url)
#                    # print (article.url)

#            print ("got urls")
#            print (urls)

#            for i in urls:
#                    print ("querying each url")

#                    try:
#                        art = newspaper.Article(i)
#                        art.download()
#                        art.parse()

#                        item = {
#                                "title": art.title,
#                                "body": art.text,
#                                "url": i,
#                                "datetime": strftime("%d-%m-%Y", gmtime()),
#                                "cat": ""
#                        }

#                        val = ""

#                                # print (item)

#                    except:
#                        print ("wrong url error")
#                        item = {
#                                "title": "",
#                                "body": "",
#                                "datetime": "",
#                                "cat": ""
#                        }

#                    a = str(item['body'])
#                    a = [w for w in word_tokenize(proc(a)) if w not in stop_words]

#                    # print (a)
#                    bu = ent = pol = spo = tec = 1e-19

#                    #indicates the count of the document density
#                    t1 = t2 = t3 = t4 = t5 = 0

#                    for w in a:

#                            #included document density
#                            tbu = tent = tpol = tspo = ttec = 1e-19

#                            w = ps.stem(w)
#                            document_density = compute_document_density(w)

#                            if w in business:
#                                    tbu = business.freq(w) * document_density
#                            if w in entertainment:
#                                    tent = entertainment.freq(w) * document_density
#                            if w in politics:
#                                    tpol = politics.freq(w) * document_density
#                            if w in sport:
#                                    tspo = sport.freq(w) * document_density
#                            if w in tech:
#                                    ttec = tech.freq(w) * document_density

#                            maxa = max(tbu, tent, tpol, tspo, ttec)

#                            if maxa != 0.0:
#                                    if tbu == maxa:
#                                            print (w, document_density, maxa, "business")
#                                    elif tent == maxa:
#                                            print (w, document_density, maxa, "entertainment")
#                                    elif tpol == maxa:
#                                            print (w, document_density, maxa, "politics")
#                                    elif tspo == maxa:
#                                            print (w, document_density, maxa, "sports")
#                                    else:
#                                            print (w, document_density, maxa, "tech")


#                            if document_density == l(5 / 1):
#                                    t1 += maxa
#                            elif document_density == l(5 / 2):
#                                    t2 += maxa
#                            elif document_density == l(5 / 3):
#                                    t3 += maxa
#                            elif document_density == l(5 / 4):
#                                    t4 += maxa
#                            else:
#                                    t5 += maxa

#                            bu += tbu
#                            ent += tent
#                            pol += tpol
#                            spo += tspo
#                            tec += ttec

#                    # print ()
#                    tsum = t1 + t2 + t3 + t4 + t5
#                    if tsum != 0:
#                            t1 = t1 * 100 / tsum
#                            t2 = t2 * 100 / tsum
#                            t3 = t3 * 100 / tsum
#                            t4 = t4 * 100 / tsum
#                            t5 = t5 * 100 / tsum

#                    # print ("density analysis Percentage", t1, t2, t3, t4, t5)
#                    maxa = max(bu, ent, pol, spo, tec)
#                    print ()

#                    if maxa != 1e-19:
#                            print ("RESULT: ")
#                            if bu == maxa:
#                                    # print ("business")
#                                    val = "business"
#                            elif ent == maxa:
#                                    # print ("entertainment")
#                                    val = "entertainment"
#                            elif pol == maxa:
#                                    # print ("politics")
#                                    val = "politics"
#                            elif spo == maxa:
#                                    # print ("sports")
#                                    val = "sports"
#                            elif tec == maxa:
#                                    # print ("tech")
#                                    val = "tech"
#                    else:
#                                    val = "none"

#                    item['cat'] = val
#                    print (item)

#                    # if "death" in item['body'] or "murder" in item['body'] or "killed" in item['body'] or len(item['body']) < 150 or "rape" in item['body'] or item['cat'] is "none" or item['title'] == "":
#                    #     pass
#                    # else:
#                    #     db.newsdata.insert(item)
#                    # print ()
#        except:
#                print ("error")
#                continue
