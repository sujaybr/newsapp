import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk.corpus import words

from bccDataLoad import *


stop_words = stopwords.words('english')
lemmatizer = WordNetLemmatizer()
ps = PorterStemmer()


while True:
	a = str(input())

	a = word_tokenize(a)
	gra = nltk.pos_tag(a)

	wordsps = [ps.stem(w) for w in a if w not in stop_words]
	wordslemma = [lemmatizer.lemmatize(w[0], pos = w[1]) for w in a if w[0] not in stop_words]

	fdstem = nltk.FreqDist(wordsps)
	fdlemma = nltk.FreqDist(wordslemma)

	print ("PorterStemmer:")
	print (wordsps)
	print ()

	print ("WordNetLemmatizer: ")
	print (wordslemma)
	print ()
	
	print ("FreqDist PorterStemmer: ")
	print (fdstem.most_common(30))
	print ()

	print ("FreqDist WordNetLemmatizer: ")
	print (fdlemma.most_common(30))
	print ()