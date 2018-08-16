
# coding: utf-8

# In[1]:


def square(x):
    return x*x


# In[4]:


f = square(5)
print(square)
print(f)


# In[6]:


f = square
print(f)
print(f(5))


# In[9]:


def cube(x):
    return x*x*x


# In[10]:


def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

squares = my_map(square, [1,2,3,4,5])
print(squares)


# In[11]:


cubes = my_map(cube, [1,2,3,4,5])
print(cubes)


# In[19]:


def logger(msg):
    
    def log_message(txt = None):
        print('Log: {} - {}'.format(msg, txt))
    
    return log_message


# In[20]:


log_hi = logger('hi!')


# In[23]:


log_hi("hello")


# In[24]:


log_hey = logger('hey!')
log_hey("how are you?")


# # Closures

# In[33]:


def outer_func():
    message = 'Hi!'
    
    def inner_func():
        print(message)
        
    return inner_func()

outer_func()


# In[38]:


def outer_func():
    message = 'Hi!'
    
    def inner_func():
        print(message)
        
    return inner_func

my_func = outer_func()

print(my_func)
my_func()


# In[43]:


def outer_func(msg):
    message = msg
    def inner_func(msg2):
        print(message)
        print(msg2)
        
    return inner_func

my_func = outer_func('Hi')

print(my_func)
my_func("hello")
my_func('yello')


# In[45]:


#Exmaple

import logging
logging.basicConfig(filename = 'example.log', level = logging.INFO)

def logger(func):
    def log_func(*args):
        logging.info('Running "{}" with arguments {}'.format(func.__name__, args))
        print(func(*args))
    return log_func

def add(*args):
    result = 0
    for i in args:
        result += i
    return result

def sub(x,y):
    return x-y

add_logger = logger(add)
sub_logger = logger(sub)

add_logger(1,2,3,4)
add_logger(4,5,3,1)

sub_logger(10,5)
sub_logger(11,9)


# ## Decorators

# In[27]:


def decorator_function(original_function):
    def wrapper_function():
        print("wrapper function executed this before {}".format(original_function.__name__))
        return original_function()
    return wrapper_function

def display():
    print('Display function ran')
    
def wrapper_function():
    print('test')
    
decorated_display = decorator_function(display)

decorated_display()
print(decorated_display.__name__)



# In[11]:


def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("wrapper function executed this before {}".format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def display():
    print('Display function ran')

#display = decorator_function(display)
display()


# In[13]:


@decorator_function
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))
    
display_info('John', '25')    


# # class decorator

# In[16]:


class decorator_class(object):
    
    def __init__(self, original_function):
        self.original_function = original_function
    
    def __call__(self, *args, **kwargs):
        print('call method executed this before {}'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)
    
@decorator_class
def display():
    print('Display function ran')

@decorator_class    
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age)) 
    
display_info('Smith','30')    
        


# In[17]:


display()


# In[25]:


#practical example

from functools import wraps

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename = '{}.log'.format(orig_func.__name__), level = logging.INFO)
    
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(
        'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper

@my_logger    
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))
    
display_info('Smith','30')      
    


# In[26]:


display_info('TOm', 25)


# In[27]:


#time taken by function

def my_time(orig_func):
    import time
    
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('The function {} took {} seconds to run'.format(orig_func.__name__, t2))
        return result
    return wrapper

import time

@my_time    
def display_info(name, age):
    time.sleep(2)
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('Smith','30')  


# In[28]:


print(display_info.__name__)


# In[31]:


@my_time 
@my_logger
def display_info(name, age):
    time.sleep(1)
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('Irfan','30')  


# ## Generators

# In[1]:


def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result

my_nums = square_numbers([1,2,3,4,5])

print(my_nums)


# In[21]:


def square_numbers(nums):
    for i in nums:
        yield (i*i)


my_nums = square_numbers([1,2,3,4,5])

print(my_nums)


# In[18]:


print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))


# In[22]:


for num in my_nums:
    print(num)


# In[23]:


my_nums2 = [x*x for x in [1,2,3,4,5]]
print(my_nums2)


# In[26]:


my_nums = (x*x for x in [1,2,3,4,5])
print(my_nums)
for num in my_nums:
    print(num)
print(list(my_nums))    


# In[15]:


#Generator example
import memory_profiler as mem_profile
import random
import time

names = ['Alpha', 'John', 'Adam', 'Steve', 'Aakash', 'Rick', 'Thomas']
majors = ['Math', 'Engg', 'CompSci', 'Arts', 'Business']

#print('Memory before: {}Mb'.format(mem_profile.memory_usage()))
print('Memory (Before): ' + str(mem_profile.memory_usage()) + 'MB' )

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)
    
    return result

def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        
        yield person
    
# t1 = time.time()   
# people = people_list(1000000)
# t2 = time.time()

t1 = time.clock()
people = people_generator(1000000)
t2 = time.clock()

#print('Memory after: {}Mb'.format(mem_profile.memory_usage()))
print('Memory (After) : ' + str(mem_profile.memory_usage()) + 'MB')

print('Took {} seconds'.format(t2-t1))


# In[ ]:


get_ipython().system('pip install mem_profiler')


# In[8]:


import memory_profiler


# In[2]:


get_ipython().system('pip install mem_profiler.whl')


# In[6]:


get_ipython().system('pip --version')
get_ipython().system('dir')


# In[7]:


get_ipython().system('pip install ./memory_profiler-0.52.0.tar.gz')


# # Decorator with arguments

# In[6]:


def prefix_decorator(prefix):
    def decorator_function(original_function):
        def wrapper_function(*args, **kwargs):
            print(prefix,"wrapper function executed this before {}".format(original_function.__name__))
            result = original_function(*args, **kwargs)
            print(prefix,"Executed after", original_function.__name__, '\n')
            return result

        return wrapper_function
    return decorator_function

@prefix_decorator('TESTING:')
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))
    
display_info('John', 30)    

