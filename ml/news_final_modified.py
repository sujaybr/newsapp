#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File              : dev/ml/nltk/news/news_freq_document_density.py
# Author            : Sujay <sujaybr9@gmail.com>
# Last Modified By  : Sujay <sujaybr9@gmail.com>

import math
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from bccDataLoad_for_density import *
import matplotlib.pyplot as plt

stop_words = stopwords.words('english') + ['said' + 'v']

ps = PorterStemmer()

business_file = entertainment_file = politics_file = sport_file = tech_file = []

#gets the data word tokeinzed, lemmatized(stemmed) and finally removes the stopwords
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

	data = nltk.FreqDist(data)
	return data

# computes the document density of each word
# document_density(word) = (number of documents / number of documents with word)
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
		return 1 / count

# load data
print ("loading business data")
business = getFreqDist("business")
print ("loading entertainment data")
entertainment = getFreqDist("entertainment")
print ("loading politics data")
politics = getFreqDist("politics")
print("loading sports data")
sport = getFreqDist("sport")
print ("loading tech data")
tech = getFreqDist("tech")

print ()


print ("enter text to be classified")
while(True):
	a = str(input())

	a = [w for w in word_tokenize(proc(a)) if w not in stop_words]

	# to avoid dbz error
	bu = ent = pol = spo = tec = 1e-19

	for w in a:

		# compute the word density or weight
		# word density = tf(term frequency) * idf(inverse document frequency)
		# tf = data.frequency(word) and idf = (1 / number of documents with word) or (log(document density(word)))
		w = ps.stem(w)
		document_density = compute_document_density(w)

		if w in business:
			bu += business.freq(w) * document_density
		if w in entertainment:
			ent += entertainment.freq(w) * document_density
		if w in politics:
			pol += politics.freq(w) * document_density
		if w in sport:
			spo += sport.freq(w) * document_density
		if w in tech:
			tec += tech.freq(w) * document_density


	# max of all computations wins
	maxa = max(bu, ent, pol, spo, tec)
	if maxa != 0.0:
		if bu == maxa:
			print (w, document_density, maxa, "business")
		elif ent == maxa:
			print (w, document_density, maxa, "entertainment")
		elif pol == maxa:
			print (w, document_density, maxa, "politics")
		elif spo == maxa:
			print (w, document_density, maxa, "sports")
		else:
			print (w, document_density, maxa, "tech")

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
		tick_label = ['business', 'entertainment', 'politics', 'sports', 'tecnology']

		plt.bar(left, height, tick_label = tick_label, width = 0.8)
		plt.xlabel('Categories')
		plt.ylabel('Values')
		plt.title('')
		plt.show()

		print ("\t\tBusiness\t{}\t{}".format(bu, maxa/bu))
		print ("\t\tEntertainment\t{}\t{}".format(ent, maxa/ent))
		print ("\t\tPolitics\t{}\t{}".format(pol, maxa/pol))
		print ("\t\tSports\t{}\t{}".format(spo, maxa/spo))
		print ("\t\tTech\t{}\t{}".format(tec, maxa/tec))

	else:
		print ("Classification not Done")
		print ("\t\tBusiness\t{}".format(bu))
		print ("\t\tEntertainment\t{}".format(ent))
		print ("\t\tPolitics\t{}".format(pol))
		print ("\t\tSports\t{}".format(spo))
		print ("\t\tTech\t{}".format(tec))

	print ()
