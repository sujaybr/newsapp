from pymongo import MongoClient

mongo = MongoClient("mongodb://raghu:raghu@ds113640.mlab.com:13640/newsdb")
db = mongo['newsdb']

def getAllCategories():
    positiveCategory = []
    negativeCategory = []
    for i in db.users.find():
        # newCategory.append(i['PositivePriority'])
        # get the priority details from the db
        positiveCategory += i['PositivePriority']

    return positiveCategory

# print (getAllCategories())
