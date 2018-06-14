from pymongo import MongoClient

mongo = MongoClient("mongodb://raghu:raghu@ds113640.mlab.com:13640/newsdb")
db = mongo['newsdb']

def getAllCategories():
    newCategory = []
    for i in db.users.find():
        # newCategory.append(i['PositivePriority'])
        newCategory += i['PositivePriority']

    return newCategory

print (getAllCategories())
