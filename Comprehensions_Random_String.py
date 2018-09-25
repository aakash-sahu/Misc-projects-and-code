# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 15:15:15 2018

@author: p624274
"""

##################
###Comprehension##
##################

nums = [1,2,3,4,5,6,7,8,9,10]

my_list = [(letter, num) for num in range(4) for letter in 'abcd']

print(my_list)


letters = ['a','b','c','d','e','f','g','h','i','j']

my_dict = {letter:num for letter in letters for num in nums}

my_dict = {letter:num for letter, num in zip(letters, nums)}

print(my_dict)

nums = [1,2,3,1,2,5,6,6,8,8,3,4]

my_set = {n for n in nums}
print(my_set)
type(my_set)

my_set2 = set()
for n in nums:
    my_set2.add(n)
print(my_set2)    

nums = [1,2,3,4,5,6,7,8,9,10]

my_gen = (n*n for n in nums)
print(my_gen)
for n in my_gen:
    print(n)
print(n)    

def gen_func(x):
    for n in x:
        yield n*n
 
my_gen2 = gen_func(nums)       

my_gen2

for n in my_gen2:
    print(n)
    
 ##############   
#random library
 ##############
import random    

#between 0 and with 1 non-inlcuded
value = random.random()
print(value)

value = random.uniform(1,10)
print(value)


value = random.randint(1,10)  #both values included
print(value)


letters = ['a','b','c','d','e','f','g','h','i','j']

value = random.choice(letters)  #one value from list
print(value)

colors = ['Red', 'Black', 'Green']

results = random.choices(colors, k = 10)  #one value from list equal probability with repeats
print(results)

results = random.choices(colors, weights =[18,18,2], k = 10)  #one value from list
print(results)

deck = list(range(1,53))
print(deck)

random.shuffle(deck)
print(deck)

hand = random.sample(deck, k =5) #only unique values
print(hand)


#################################
#####STRING FORMATTING###########
################################

person = {'Name': "John", 'Age': 30}
sentence = "My name is {} and age is {}.".format(person['Name'], person['Age'])
print(sentence)


sentence = "My name is {0} and age is {1}.".format(person['Name'], person['Age'])
print(sentence)

tag= 'h1'
text = 'This is the headline'

sent = "<{0}>{1}</{0}>".format(tag, text)
print(sent)

sentence = "My name is {0[Name]} and age is {1[Age]}.".format(person, person)
print(sentence)

sentence = "My name is {0[Name]} and age is {0[Age]}.".format(person)
print(sentence)

l = ['John', 23]
sentence = "My name is {0[0]} and age is {0[1]}.".format(l)
print(sentence)

class Person:
    
    def __init__(self,name, age):
        self.name = name
        self.age = age
 
p1 = Person('John', 23) 

print(p1.name)
print(p1.age)      

sentence = "My name is {0.name} and age is {0.age}.".format(p1)
print(sentence)

sentence = "My name is {name} and age is {age}.".format(name = 'John', age = 30)
print(sentence)


sentence = 'My name is {Name} and age is {Age}'.format(**person)
print(sentence)

print('').format(**person)

#numbers
for i in range(11):
    sent = "the number is {:03}".format(i)
    print(sent)
    
pi = 3.142353124    
sent = "Pi is equal to {:.5f}".format(pi)   
print(sent)  

sent = "1 MB is equal to {:,.2f}".format(1000**2)
print(sent)   

import datetime
my_date = datetime.datetime.now()
print(my_date)
sent = "today's date is {:%B %d, %Y}".format(my_date)
print(sent)

sent = "{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of year.".format(my_date)
print(sent)


#####################
##Context Manager####
#####################

from contextlib import contextmanager
import os

with open('sample_text.txt', 'w') as f:
    f.write('alpha beta. gammma')
    
class open_file():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()
        
with open_file('sample.txt','w') as f:
    f.write('Testing')        
    
@contextmanager
def Open_file(file, mode):
    try:
        f = open(file, mode)
        yield f
    finally:
        f.close()
    
with Open_file('sample.txt','w') as f:
    f.write('alpha beta gamma and more to go')
    
