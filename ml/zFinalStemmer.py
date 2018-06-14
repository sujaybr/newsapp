from nltk.stem import WordNetLemmatizer, PorterStemmer
import nltk
from nltk.corpus import stopwords, wordnet


lemmatizer = WordNetLemmatizer()
ps = PorterStemmer()


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

def findStem(word):

	tense = nltk.pos_tag([word])

	if word == lemmatizer.lemmatize(word, pos = getValueForPos(tense[0][1])):
		return ps.stem(word)
	else:
		return ps.stem(lemmatizer.lemmatize(word, pos = getValueForPos(tense[0][1])))
