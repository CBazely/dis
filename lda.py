
import pandas as pd
import numpy as np
import xml.etree.cElementTree as et

print('hi')
df = pd.read_csv('users.csv')
print(df)

about = df.loc[:,'AboutMe']
doc_complete = df.loc[:,'AboutMe']
doc_complete.fillna("", inplace=True)
print(about)

from bs4 import BeautifulSoup

emphasized = []
for x in doc_complete:
	y = ""
	#print(type(x))
	#print(x)
	x2 = BeautifulSoup(x, 'html.parser')
	x = x2.get_text()
	y = y + str(x2.find_all("strong"))
	print(y)
	emphasized.append(y)
	#print(type(x))
	#print(x)



#print(locs)
import nltk

nltk.download('stopwords')
nltk.download('wordnet')

from nltk.corpus import stopwords 
from nltk.stem.wordnet import WordNetLemmatizer
import string
stop = set(stopwords.words('english'))
exclude = set(string.punctuation) 
lemma = WordNetLemmatizer()

def clean(doc):
    x = BeautifulSoup(doc, 'html.parser')
    doc = x.get_text()
    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    return normalized

#doc_clean = [clean(doc).split() for doc in doc_complete]  
print(doc_clean)

# Importing Gensim
import gensim
from gensim import corpora

# Creating the term dictionary of our courpus, where every unique term is assigned an index. 
dictionary = corpora.Dictionary(doc_clean)

# Converting list of documents (corpus) into Document Term Matrix using dictionary prepared above.
doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]

# Creating the object for LDA model using gensim library
Lda = gensim.models.ldamodel.LdaModel

# Running and Trainign LDA model on the document term matrix.
ldamodel = Lda(doc_term_matrix, num_topics=3, id2word = dictionary, passes=50)

#print(ldamodel.print_topics(num_topics=3, num_words=3))
