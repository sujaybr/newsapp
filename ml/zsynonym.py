import nltk
from nltk.corpus import wordnet

s=[]
a = []

for i in wordnet.synsets("good"):
    for j in i.lemmas():
        s.append(j.name())
        if j.antonyms():
            a.append(j.antonyms()[0])


print(set(s))
print(set(a))
