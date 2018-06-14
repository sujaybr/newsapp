import requests
from pymongo import MongoClient
import getExtraCategories
from flask import session

mongo = MongoClient("mongodb://raghu:raghu@ds113640.mlab.com:13640/newsdb")
db = mongo['newsdb']

def getNewsForCategory(cat):
    allData = []
    if cat == "all":
        cats = ['business', 'sports', 'politics', 'entertainment', 'technology']
        for i in cats:
            for i in db.newsdata.find({"cat":i}):
                temp = {}
                temp['title'] = i['title']
                temp['description'] = i['body']
                temp['url'] = i['url']
                allData.append(temp)
            
        return allData
    else:
        # query for the category
        allData = []
        data = db.newsdata.find({"cat":cat})
        for i in data:
            # Append the data for each article allData.append(i)
            temp = {}
            temp['title'] = i['title']
            temp['description'] = i['body']
            temp['url'] = i['url']
            allData.append(temp)
            
        return allData

