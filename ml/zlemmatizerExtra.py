from nltk.tokenize import word_tokenize
import nltk
from nltk.stem import WordNetLemmatizer, PorterStemmer

lemmatizer = WordNetLemmatizer()

def tokenize_text(data):
	data = lemmatizer.lemmatize(data)
	return data

while True:
	s = str(input())
	print (tokenize_text(s), )
	ps = PorterStemmer()

	# for w in s:
	print (ps.stem(s))
