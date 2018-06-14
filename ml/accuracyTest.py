from pymongo import MongoClient

mongo = MongoClient("mongodb://raghu:raghu@ds113640.mlab.com:13640/newsdb")
db = mongo['newsdb']

count = 0
counter = 0
empty = 0
for i in db.accuracy.find():
    counter += 1
    print ("processing " + str(counter))
    if i['cat'] != i['result']:
        count += 1
    if i['result'] == "":
        empty += 1

print (str(100 - count) + "/100")
print (empty)
