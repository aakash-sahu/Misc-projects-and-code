# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 09:54:03 2018

@author: p624274
"""

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

EXAMPLE_TEXT = "Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."

print(sent_tokenize(EXAMPLE_TEXT))

print(word_tokenize(EXAMPLE_TEXT))

for i in sent_tokenize(EXAMPLE_TEXT):
    print(i)
    
for i in word_tokenize(EXAMPLE_TEXT):
    print(i)

#Stop words
from nltk.corpus import stopwords

stopwords.words("english")

example_sent = "This is a sample sentence, showing off the stop words filtration."

#stop_words = stopwords.words("english") #--creates list
stop_words = set(stopwords.words("english"))
print(stop_words)

word_tokens = word_tokenize(example_sent)
word_tokens2 = word_tokenize(EXAMPLE_TEXT)

filtered_sentence = []
filtered_sentence2 = []

for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)
        
filtered_sentence
print(stop_words)
print(filtered_sentence)


for w in word_tokens2:
    if w not in stop_words:
        filtered_sentence2.append(w)
        
print(EXAMPLE_TEXT)        
print(filtered_sentence2)
 
#short form       
filtered_sentence3 = [w for w in word_tokens if not w in stop_words] 
print(filtered_sentence3)  
        
#Stemming
##another stemmer
sno = nltk.stem.SnowballStemmer('english')

from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

ps = PorterStemmer()        
example_words = ["python","pythoner","pythoning","pythoned","pythonly"]        
for w in example_words:
    print(ps.stem(w))  

for w in word_tokens:
    print(ps.stem(w))
    
for w in word_tokens2:
    print(ps.stem(w))    
        
for w in word_tokens:
    print(sno.stem(w))

for w in word_tokens2:
    print(sno.stem(w))  

#Part of speech tagging
import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt") 

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)
print(tokenized)

#tokenized2 = sent_tokenize(sample_text) 
#print(tokenized2)

def process_content():
    try:
        for i in tokenized[:5]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            print(tagged)
        
    except Exception as e:
        print(str(e))
        
process_content()

#alternate
for i in sent_tokenize(sample_text)[:5]:
    words2 = word_tokenize(i)
    print(nltk.pos_tag(words2)) 

#Chunking
def process_content2():
    try:
        for i in tokenized[5:15]:
            words_chunk = nltk.word_tokenize(i)
            tagged_chunk = nltk.pos_tag(words_chunk)
            #chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
            chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged_chunk)
            #print(chunked)
            #for subtree in chunked.subtrees():
               # print(subtree)

#            for subtree in chunked.subtrees(filter=lambda t: t.label() == 'Chunk'):
#               print(subtree) 
            chunked.draw() 
            

    except Exception as e:
        print(str(e))
    

process_content2()

#Chunking practise
def process_content3():
    try:
        for i in tokenized[:50]:
            words_chunk = nltk.word_tokenize(i)
            tagged_chunk = nltk.pos_tag(words_chunk)
            #chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
            chunkGram = r"""Chunk: {<JJ.?>+<VB.?>*<NN.?>+}"""
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged_chunk)
            #print(chunked)
            for subtree in chunked.subtrees():
                print(subtree)

            #for subtree in chunked.subtrees(filter=lambda t: t.label() == 'Chunk'):
             #  print(subtree) 
            #chunked.draw() 
            

    except Exception as e:
        print(str(e))
    

process_content3()

  
##Chinking
#            chunkGram = r"""Chunk: {<.*>+}
 #                                   }<VB.?|IN|DT|TO>+{"""
import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_content4(sen1, sen2):
    try:
        for i in tokenized[sen1:sen2]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)

            chunkGram = r"""Chunk: {<.*>+}
                                    }<NN.?|,*|\.*>+{"""

            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)

            #chunked.draw()
            print(chunked)
            #for subtree in chunked.subtrees():
              #  print(subtree)

            for subtree in chunked.subtrees(filter=lambda t: t.label() == 'Chunk'):
               print(subtree)
    except Exception as e:
        print(str(e))

process_content4(5,30)

#named entity recognition
def process_content5():
    try:
        for i in tokenized[10:20]:
            words = nltk.word_tokenize(i)
           # print(words)
            tagged = nltk.pos_tag(words)
#            print(tagged)
            namedEnt = nltk.ne_chunk(tagged, binary=False)
            #namedEnt.draw()
            print(namedEnt)
#            print('\n')
            for subtree in namedEnt:
#               if hasattr(subtree, 'label'): 
#                   print(subtree.label(), ' '.join(c[0] for c in subtree))
                print(subtree)
            print('\n')
    except Exception as e:
           print(str(e))


process_content5()

##Lemmatizing
from nltk import WordNetLemmatizer
from nltk import PorterStemmer

lemmatizer = WordNetLemmatizer()
ps = PorterStemmer()

def lemmatizee():
    try:
        for i in tokenized[10:15]:
            words = nltk.word_tokenize(i)
            print(words)
            for j in words:
             lem = lemmatizer.lemmatize(j)
             print(lem)
             print(ps.stem(j))
#            tagged = nltk.pos_tag(words)
##            print(tagged)
#            namedEnt = nltk.ne_chunk(tagged, binary=False)
#            #namedEnt.draw()
#            print(namedEnt)
##            print('\n')
#            for subtree in namedEnt:
##               if hasattr(subtree, 'label'): 
##                   print(subtree.label(), ' '.join(c[0] for c in subtree))
#                print(subtree)
            print('\n')
    except Exception as e:
           print(str(e))


lemmatizee()

#Corpus
import nltk
print(nltk.__file__)

from nltk import sent_tokenize, PunktSentenceTokenizer

from nltk.corpus import gutenberg
#sample text
sample = gutenberg.raw("bible-kjv.txt")

tok = sent_tokenize(sample)        

for i in range(5):
    print(tok[i])

print(tok[5:10])        

from nltk.corpus import nps_chat        

ch = nps_chat.raw("10-26-teens_706posts.xml")
#ch2 = nps_chat.

tok2 = sent_tokenize(ch)

for i in range(10):
    print(tok2[i])
    
print(tok2[1:50]) 

#wordnet

from nltk.corpus import wordnet       

syns = wordnet.synsets("program")        
print(syns)

print(syns[0])

print(syns[0].name())

print(syns[0].lemmas()[0].name())

print(syns[0].definition())

print(syns[0].examples())

syns2 = wordnet.synsets("cat")        
print(syns2)

print(syns2[1])

print(syns2[1].name())

print(syns2[1].lemmas()[2].name())

print(syns2[1].definition())

print(syns2[1].examples())


#synonymns and antonyms
synonyms = []
antonyms = []

for syn in wordnet.synsets("good"):
    #print(syn)
    for l in syn.lemmas():
       # print(l)
        print("syn:",l.name())
        synonyms.append(l.name())
        #for k in l.antonyms():
        #if l.antonyms():
        for  k in range(len(l.antonyms())):
                    antonyms.append(l.antonyms()[k].name())
                    print("antonym:",l.antonyms()[k].name())
                #antonyms.append(l.antonyms()[0].name())
                #print("k:",k.name())
    print('\n')
       
print(set(synonyms))
print(set(antonyms))            
print(wordnet.synsets("good"))

#Wu palmer method - word similarity

w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('boat.n.01')
print(w1.wup_similarity(w2))

w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('car.n.01')
print(w1.wup_similarity(w2))

w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('cat.n.01')
print(w1.wup_similarity(w2))

s1 = 'ship.n.01'
s2 = 'cat.n.01'
print(s1.wup_similarity(s2))

w1 = wordnet.synsets('man')
w2 = wordnet.synsets('goat')
for l in w1:
    print(l)
    for k in w2:
        print(k)
        print(l.wup_similarity(k))
    print('\n')    

#Text classification

import random
from nltk.corpus import movie_reviews

documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)] 
doc2 =[]
for category in movie_reviews.categories():
    for fileid in movie_reviews.fileids(category):
        doc2.append((list(movie_reviews.words(fileid)), category))
    
random.shuffle(documents)

print(documents[1])

all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)
print(all_words.most_common(15))
print(all_words["stupid"])
#print(all_words.contains("st"))
#print(all_words.least_common(15))


sent = 'This is an example sentence'
fdist = nltk.FreqDist()
for word in nltk.word_tokenize(sent):
 fdist[word.lower()] += 1
 
 #fdist = FreqDist(word.lower() for word in word_tokenize(sent))

word_features = list(all_words.keys())[:3000]


def find_features(document):
    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features

print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))

featuresets = [(find_features(rev), category) for (rev, category) in documents]

print(featuresets[1])
f =[]
for x,y in documents[:5]:
    #print(x,'\n',y)
    f.append((find_features(x),y))

print(f[1])   

#Naive Bayes algorithm
# set that we'll train our classifier with
training_set = featuresets[:1900]

# set that we'll test against.
testing_set = featuresets[1900:] 

classifier = nltk.NaiveBayesClassifier.train(training_set)

print("Classifier accuracy percent:",(nltk.classify.accuracy(classifier, testing_set))*100)

classifier.show_most_informative_features(15)


from nltk.corpus import wordnet as wn
for ss in wn.synsets('love'): # Each synset represents a diff concept.
  print(ss.definition)
  print(ss.lemma_names)
  print("\n")
  
  
