import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk.corpus import words

from bccDataLoad import *
from FinalStemmer import *


stop_words = stopwords.words('english')
lemmatizer = WordNetLemmatizer()
ps = PorterStemmer()

def getValueForPos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return "n"

a = word_tokenize(getBusiness())
a = [w for w in a if w not in stop_words]

freqofa = nltk.FreqDist(a)

print ("actual")
print (freqofa.most_common(30))

while True:
	# a = str(input())

	# a = word_tokenize(data)
	gra = nltk.pos_tag(a)

	wordsps = [ps.stem(w) for w in a if w not in stop_words]
	wordslemma = [lemmatizer.lemmatize(w[0], pos = getValueForPos(w[1])) for w in gra if w[0] not in stop_words]
	finalstemmer = [findStem(w)for w in a if w not in stop_words]
	
	fdstem = nltk.FreqDist(wordsps)
	fdlemma = nltk.FreqDist(wordslemma)
	final = nltk.FreqDist(finalstemmer)

	fdstem = fdstem.most_common(100)
	fdlemma = fdlemma.most_common(100)
	final = final.most_common(100)
	freqofa = freqofa.most_common(100)

	print ()

	# print ("FreqDist PorterStemmer: ")
	# print (fdstem.most_common(100))
	# print ()

	# print ("FreqDist WordNetLemmatizer: ")
	# print (fdlemma.most_common(100))
	# print ()

	# print ("Final stemmer")
	# print (final.most_common(100))
	# print ()

	for i in range(100):
		print (freqofa[i][0], freqofa[i][1], final[i][1])

	break
