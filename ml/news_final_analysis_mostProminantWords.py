from math import log as l
import tkinter
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from bccDataLoad_for_density import *

#extra to be removed
import operator

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
	if data in politics_file:
		count += 1

	if count == 0:
		return 0
	else:
		return l(5 / count)

stop_words = stopwords.words('english') + ['said' + 'v']
ps = PorterStemmer()
business_file = entertainment_file = politics_file = sport_file = tech_file = []

#data
print ("loading business data")
business = getFreqDist("business")
# print ()
print ("loading entertainment data")
entertainment = getFreqDist("entertainment")
# print ()
print ("loading politics data")
politics = getFreqDist("politics")
# print ()
print("loading sports data")
sport = getFreqDist("sport")
# print ()
print ("loading tech data")
tech = getFreqDist("tech")
# tech.plot(20)

print ()

res_bu = []
res_ent = []
res_pol = []
res_spo = []
res_tec = []

print ("enter text")
while(True):
	# a = str(input())
	# a = [w for w in word_tokenize(proc(a)) if w not in stop_words]
	# print (a)

	a = set(list(business_file) + list(entertainment_file) + list(politics_file) + list(tech_file) + list(politics_file))

	bu = 1e-19
	ent = 1e-19
	pol = 1e-19
	spo = 1e-19
	tec = 1e-19

	#indicates the count of the document density
	t1 = t2 = t3 = t4 = t5 = 0

	for w in a:

		#included document density
		tbu = 1e-19
		tent = 1e-19
		tpol = 1e-19
		tspo = 1e-19
		ttec = 1e-19

		w = ps.stem(w)
		document_density = compute_document_density(w)

		if w in business:
			tbu = business.freq(w) * document_density
		if w in entertainment:
			tent = entertainment.freq(w) * document_density
		if w in politics:
			tpol = politics.freq(w) * document_density
		if w in sport:
			tspo = sport.freq(w) * document_density
		if w in tech:
			ttec = tech.freq(w) * document_density

		maxa = max(tbu, tent, tpol, tspo, ttec)

		if maxa != 0.0:
			if tbu == maxa:
				res_bu.append((w, document_density, business.freq(w),  maxa, "business"))
			elif tent == maxa:
				# pass
				res_ent.append((w, document_density, entertainment.freq(w), maxa, "entertainment"))
			elif tpol == maxa:
				# pass
				res_pol.append((w, document_density, politics.freq(w),  maxa, "politics"))
			elif tspo == maxa:
				# pass
				res_spo.append((w, document_density, sport.freq(w), maxa, "sports"))
			else:
				# pass
				res_tec.append((w, document_density, tech.freq(w), maxa, "tech"))

	break


res_bu.sort(key = operator.itemgetter(2))
res_ent.sort(key = operator.itemgetter(2))
res_pol.sort(key = operator.itemgetter(2))
res_spo.sort(key = operator.itemgetter(2))
res_tec.sort(key = operator.itemgetter(2))

res_bu.reverse()
res_ent.reverse()
res_pol.reverse()
res_spo.reverse()
res_tec.reverse()

print ("bu")
for i in res_bu[:20]:
	print (i)
print ()
print ("ent")
for i in res_ent[:20]:
	print (i)
print ()
print ("pol")
for i in res_pol[:20]:
	print (i)
print ()
print ("spo")
for i in res_spo[:20]:
	print (i)
print ()
print ("tec")
for i in res_tec[:20]:
	print (i)
print ()
