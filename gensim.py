# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 16:43:47 2018

@author: Aakash
"""
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

import os
import tempfile
TEMP_FOLDER = tempfile.gettempdir()
print('Folder "{}" will be used to save temporary dictionary and corpus.'.format(TEMP_FOLDER))

from gensim import corpora, models, similarities
corpus = [[(0, 1.0), (1, 1.0), (2, 1.0)],
           [(2, 1.0), (3, 1.0), (4, 1.0), (5, 1.0), (6, 1.0), (8, 1.0)],
           [(1, 1.0), (3, 1.0), (4, 1.0), (7, 1.0)],
           [(0, 1.0), (4, 2.0), (7, 1.0)],
          [(3, 1.0), (5, 1.0), (6, 1.0)],
          [(9, 1.0)],
           [(9, 1.0), (10, 1.0)],
          [(9, 1.0), (10, 1.0), (11, 1.0)],
           [(8, 1.0), (10, 1.0), (11, 1.0)]]
print(corpus)

tfidf = models.TfidfModel(corpus)

vec = [(0, 1), (4, 1)]
print(tfidf[vec])

index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=12)

sims = index[tfidf[vec]]

print(list(enumerate(sims)))

#Corpora
from gensim import corpora

documents = ["Human machine interface for lab abc computer applications",
              "A survey of user opinion of computer system response time",
              "The EPS user interface management system",
              "System and human system engineering testing of EPS",
              "Relation of user perceived response time to error measurement",
              "The generation of random binary unordered trees",
              "The intersection graph of paths in trees",
              "Graph minors IV Widths of trees and well quasi ordering",
              "Graph minors A survey"]
 
# remove common words and tokenize
stoplist = set('for a of the and to in'.split())
 
texts = [[word for word in document.lower().split() if word not in stoplist]
        for document in documents]
print(texts) 
# remove words that appear only once
from collections import defaultdict 

frequency = defaultdict(int) 
for text in texts:
    for token in text:
        frequency[token] += 1
        
        
texts = [[token for token in text if frequency[token] > 1]
        for text in texts]


from nltk import sent_tokenize, word_tokenize 
from nltk.corpus import stopwords
import nltk

words =[]
for d in documents:
    words.append(word_tokenize(d.lower()))
    
print(words) 

words2 = [[w for w in word_tokenize(d.lower())]
        for d in documents]   
print(words2)

stop_words = set(stopwords.words("english"))

words2_1 = [[w for w in l if w not in stop_words]
        for l in words2]
##---probably also lemmatize or stem at this point
print(words2_1)

#freq = nltk.FreqDist(words2_1)

dictionary = corpora.Dictionary(texts)
print(dictionary)
print(dictionary.token2id)
#dictionary.save('/tmp/deerwester.dict')  # store the dictionary, for future reference
dictionary.save(os.path.join(TEMP_FOLDER, 'deerwester.dict'))  # store the dictionary, for future reference
    
dictionary2 = corpora.Dictionary(words2_1)
print(dictionary2)
print(dictionary2.token2id)
#dictionary2.save('/tmp/dict2.dict')
dictionary2.save(os.path.join(TEMP_FOLDER, 'dict2.dict'))  # store the dictionary, for future reference 

new_doc = "Human computer interaction"
new_vec = dictionary.doc2bow(new_doc.lower().split())
print(new_vec)  # the word "interaction" does not appear in the dictionary and is ignored

new_doc2 = "Human human computer interaction"
new_vec2 = dictionary2.doc2bow(new_doc2.lower().split())
print(new_vec2)  # the word "interaction" does not appear in the dictionary and is ignored

corpus = [dictionary.doc2bow(text) for text in texts]
corpora.MmCorpus.serialize('/tmp/deerwester.mm', corpus)  # store to disk, for later use
print(corpus) 
corpora.MmCorpus.serialize(os.path.join(TEMP_FOLDER, 'deerwester.mm'), corpus) 

corpus2 = [dictionary2.doc2bow(text) for text in words2_1] 
corpora.MmCorpus.serialize('/tmp/corpora2.mm', corpus2)
print(corpus2) 
corpora.MmCorpus.serialize(os.path.join(TEMP_FOLDER, 'corpora2.mm'), corpus2) 

#Corpus Streaming – One Document at a Tim
class MyCorpus(object):
     def __iter__(self):
         for line in open('C:\\Users\\p624274\\Desktop\\Personal\\Capgemini\\mycorpus.txt'):
             # assume there's one document per line, tokens separated by whitespace
             yield dictionary.doc2bow(line.lower().split())
 
corpus_memory_friendly = MyCorpus()  # doesn't load the corpus into memory!
print(corpus_memory_friendly) 

for vector in corpus_memory_friendly:  # load one vector into memory at a time
    print(vector)
 
from six import iteritems
 # collect statistics about all tokens
dictionary = corpora.Dictionary(line.lower().split() for line in open('C:\\Users\\p624274\\Desktop\\Personal\\Capgemini\\mycorpus.txt'))
# remove stop words and words that appear only once
stop_ids = [dictionary.token2id[stopword] for stopword in stoplist
             if stopword in dictionary.token2id]
once_ids = [tokenid for tokenid, docfreq in iteritems(dictionary.dfs) if docfreq == 1]
dictionary.filter_tokens(stop_ids + once_ids)  # remove stop words and words that appear only once
dictionary.compactify()  # remove gaps in id sequence after words that were removed
print(dictionary)
 
print(list(corpus)) 

#Compatibility with NumPy and SciPy
import gensim
import numpy as np
numpy_matrix = np.random.randint(10, size=[5,2])  # random matrix as an example
corpus = gensim.matutils.Dense2Corpus(numpy_matrix)
numpy_matrix = gensim.matutils.corpus2dense(corpus, num_terms=number_of_corpus_features)

#similar words
from gensim.models import Word2Vec 
gmodel=Word2Vec.load_word2vec_format()
