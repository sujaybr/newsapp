import nltk
import random
from bccDataLoadForNaive import *
from nltk.stem import PorterStemmer

ps = PorterStemmer()
documents = getBusiness() + getEntertainment() + getPolitics() + getSports() + getTech()

# print (len(documents))
random.shuffle(documents)

allwords = [w.lower() for w in allWords()]

allwords = nltk.FreqDist(allwords)

# print (allwords.most_common(20))

word_features = list(allwords.keys())[:3000]

def find_features(document):
	words = set(document)

	feature = {}
	for w in word_features:
		feature[w] = w in words

	return feature


featuresets = [(find_features(rev), category) for (rev, category) in documents]

# print (len(featuresets))
# print ("done")

training = featuresets[:350]
testing = featuresets[350:]

classifier = nltk.NaiveBayesClassifier.train(training)

print ("accuracy", nltk.classify.accuracy(classifier, testing))
classifier.show_most_informative_features(200)

print ("enter text")
while True:
	a = str(input())

	a = ps.stem(a)
	# print (classifier.classify(find_features(a)))
	featurized_doc = {c:True for c in a.split()}
	tagged_label = classifier.classify(featurized_doc)
	print(tagged_label)
