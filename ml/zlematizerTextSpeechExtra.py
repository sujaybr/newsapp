import nltk
from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk.corpus import wordnet

def get_wordnet_pos(treebank_tag):

    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return "n"

a = ""
lemmatizer = WordNetLemmatizer()
ps = PorterStemmer()

print ("enter ")

while True:
	a = str(input())
	iw""ords = nltk.word_tokenize(a)
	words = nltk.pos_tag(words)

	# print (words)

	for w in words:
		# print (w, )
		print(ps.stem(w[0]))
		w = lemmatizer.lemmatize(w[0], pos = get_wordnet_pos(w[1]))
		print (w)


# print (lemmatizer.lemmatize("better", pos=""))
