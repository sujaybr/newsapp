from pymongo import MongoClient

mongo = MongoClient("mongodb://raghu:raghu@ds113640.mlab.com:13640/newsdb")
db = mongo['newsdb']

def getCategoryDataFromDB(cat):
    data = db.newsdata.find({"cat": cat})
    res = []
    for i in data:
        res.append(i)
    return res

