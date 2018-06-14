#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File              : dev/ml/nltk/news/news_freq_document_density.py
# Author            : Sujay <sujaybr9@gmail.com>
# Last Modified By  : Sujay <sujaybr9@gmail.com>

from math import log as l
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from bccDataLoad_for_density import *
import matplotlib.pyplot as plt

#extra to be removed
import operator

stop_words = stopwords.words('english') + ['said' + 'v' + 'would' + 'could']
ps = PorterStemmer()
business_file = entertainment_file = politics_file = sport_file = tech_file = []

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
		return 1 / count

#data
print ("loading business data")
business = getFreqDist("business")
# business.pop("said")
# business.pop("say")
# business.plot(30)
# print ()
print ("loading entertainment data")
entertainment = getFreqDist("entertainment")
# entertainment.pop("said")
# entertainment.plot(30)
# print ()
print ("loading politics data")
politics = getFreqDist("politics")
# politics.pop("said")
# politics.plot(30)
# print ()
print("loading sports data")
sport = getFreqDist("sport")
# sport.pop("said")
# sport.plot(30)
# print ()
print ("loading tech data")
tech = getFreqDist("tech")
# tech.pop("said")
# tech.pop("use")
# tech.pop("also")
# tech.pop("new")
# tech.pop("make")
# tech.plot(30)




print ("enter text")
while(True):
	a = str(input())

	a = [w for w in word_tokenize(proc(a)) if w not in stop_words]

	# print (a)
	bu = ent = pol = spo = tec = 1e-19

	#indicates the count of the document density
	t1 = t2 = t3 = t4 = t5 = 0

	for w in a:

		#included document density
		tbu = tent = tpol = tspo = ttec = 1e-19

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
				print (w, document_density, maxa, "business")
			elif tent == maxa:
				print (w, document_density, maxa, "entertainment")
			elif tpol == maxa:
				print (w, document_density, maxa, "politics")
			elif tspo == maxa:
				print (w, document_density, maxa, "sports")
			else:
				print (w, document_density, maxa, "tech")


		if document_density == l(5 / 1):
			t1 += maxa
		elif document_density == l(5 / 2):
			t2 += maxa
		elif document_density == l(5 / 3):
			t3 += maxa
		elif document_density == l(5 / 4):
			t4 += maxa
		else:
			t5 += maxa

		bu += tbu
		ent += tent
		pol += tpol
		spo += tspo
		tec += ttec

	print ()
	tsum = t1 + t2 + t3 + t4 + t5
	if tsum != 0:
		t1 = t1 * 100 / tsum
		t2 = t2 * 100 / tsum
		t3 = t3 * 100 / tsum
		t4 = t4 * 100 / tsum
		t5 = t5 * 100 / tsum

	print ("density analysis Percentage", t1, t2, t3, t4, t5)
	maxa = max(bu, ent, pol, spo, tec)
	print ()

	if maxa != 1e-19:
		print ("RESULT: ")
		if bu == maxa:
			print ("business")
		elif ent == maxa:
			print ("entertainment")
		elif pol == maxa:
			print ("politics")
		elif spo == maxa:
			print ("sports")
		elif tec == maxa:
			print ("tech")

		left = [1, 2, 3, 4, 5]
		height = [bu, ent, pol, spo, tec]
		tick_label = ['bu', 'ent', 'pol', 'spo', 'tec']

		plt.bar(left, height, tick_label = tick_label, width = 0.5)
		plt.xlabel('x - axis')
		plt.ylabel('y - axis')
		plt.title('Relavence Chart')
		plt.show()

		print ("\t\tBusiness\t{}, {}".format(bu, maxa/bu))
		print ("\t\tEntertainment\t{}, {}".format(ent, maxa/ent))
		print ("\t\tPolitics\t{}, {}".format(pol, maxa/pol))
		print ("\t\tSports\t{}, {}".format(spo, maxa/spo))
		print ("\t\tTech\t{}, {}".format(tec, maxa/tec))

	else:
		print ("Classification not Done, see Freq density Classifier")
		print ("\t\tBusiness\t{}".format(bu))
		print ("\t\tEntertainment\t{}".format(ent))
		print ("\t\tPolitics\t{}".format(pol))
		print ("\t\tSports\t{}".format(spo))
		print ("\t\tTech\t{}".format(tec))

	print ()
