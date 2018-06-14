from pymongo import MongoClient
from bccDataLoad_for_accuracy import *

mongo = MongoClient("mongodb://raghu:raghu@ds113640.mlab.com:13640/newsdb")
db = mongo['newsdb']

business = agetBusiness()
sports = agetSports()
tech = agetTech()
politics = agetPolitics()
entertainment = agetEntertainment()

# print (business[0])
# print (sports[0])
# print (tech[0])
# print (politics[0])
# print (entertainment[0])

print ("loading data")
for i in business[:20]:
    db.accuracy.insert({"data": i, "cat": "business", "result":""})
for i in sports[:20]:
    db.accuracy.insert({"data": i, "cat": "sports", "result":""})
for i in tech[:20]:
    db.accuracy.insert({"data": i, "cat": "tech", "result":""})
for i in politics[:20]:
    db.accuracy.insert({"data": i, "cat": "politics", "result":""})
for i in entertainment[:20]:
    db.accuracy.insert({"data": i, "cat": "entertainment", "result":""})
