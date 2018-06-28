
# coding: utf-8

# In[2]:


class Employee:
    pass


# In[ ]:


class Employee:
    pass


# In[4]:


emp_1 = Employee()
emp_2 = Employee()


# In[5]:


print(emp_1)
print(emp_2)


# In[7]:


emp_1.first = "Test1"
emp_1.last = "User1"
emp_2.first = "Test2"
emp_2.last = "User2"


# In[10]:


print(emp_1.first)


# In[62]:


class Employee():
    
    num_emps = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
            self.first = first
            self.last = last
            self.pay = pay
            self.email = first + '.' + last +'@company.com'
        
            Employee.num_emps+= 1
            
    def fullname(self):
        return self.first + ' ' + self.last
        #return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        #self.pay = int(self.pay * 1.04)
        self.pay = int(self.pay * self.raise_amount)
        #self.pay = int(self.pay * Employee.raise_amount)


# In[63]:


emp_1 = Employee('Aakash', 'sahu', 20000)
emp_2 = Employee('Test', 'User', 25000)
print(emp_1.email)
print(emp_2.email)


# In[64]:


emp_1.fullname()


# In[65]:


Employee.fullname(emp_1)


# ##Class variables

# In[66]:


print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)


# In[67]:


print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)


# In[68]:


print(emp_1.__dict__)


# In[69]:


print(Employee.__dict__)


# In[70]:


Employee.raise_amount = 1.05
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
emp_2.apply_raise()
print(emp_2.pay)


# In[71]:


emp_1.raise_amount = 1.06
emp_1.__dict__


# In[72]:


print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)


# In[73]:


print(Employee.num_emps)


# In[75]:


print(emp_2.num_emps)


# #Class methods, static methods

# In[91]:


class Employee():
    
    num_emps = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
            self.first = first
            self.last = last
            self.pay = pay
            self.email = first + '.' + last +'@company.com'
        
            Employee.num_emps+= 1
            
    def fullname(self):
        return self.first + ' ' + self.last
        #return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        #self.pay = int(self.pay * 1.04)
        self.pay = int(self.pay * self.raise_amount)
        #self.pay = int(self.pay * Employee.raise_amount)
        
    @classmethod
    def set_raise_amt(cls, amount):
        #pass
        cls.raise_amount = amount
    @classmethod
    def from_string(cls,emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


# In[92]:


emp_1 = Employee('Aakash', 'sahu', 20000)
emp_2 = Employee('Test', 'User', 25000)


# In[93]:


print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)


# In[94]:


Employee.set_raise_amt(1.06) 
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)


# In[104]:


emp_1.raise_amount = 1.09
print(emp_1.raise_amount)
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)


# In[106]:


print(emp_2.raise_amount)
print(Employee.raise_amount)


# In[95]:


emp3_str = 'john-doe-30000'
emp4_str = 'steve-smith-4000'
emp_3 = Employee.from_string(emp3_str)
emp_4 = Employee.from_string(emp4_str)


# In[96]:


print(emp_3.pay)
print(emp_3.email)
print(emp_4.email)


# In[99]:


#static methods
import datetime
my_date = datetime.date(2016, 7, 11)
print(my_date)

print(Employee.is_workday(my_date))


# ## Inheritance and subclass

# In[100]:


class Developer(Employee):
    pass

dev1 = Developer("Aakash", "Sahu", 20000)
dev2 = Developer("Test", "User", 30000)


# In[102]:


print(dev1.email)
print(help(Developer))


# In[110]:


class Developer(Employee):
    raise_amount = 1.1    
    
dev1 = Developer("Aakash", "Sahu", 20000)
dev2 = Employee("Test", "User", 30000)    


# In[111]:


print(dev1.pay)
dev1.apply_raise()
print(dev1.pay)


# In[112]:


print(dev2.pay)
dev2.apply_raise()
print(dev2.pay)


# In[117]:


class Developer(Employee):
    raise_amount = 1.1 
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        #Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang


# In[119]:


dev1 = Developer("Aakash", "Sahu", 20000, 'Python')
dev2 = Developer("Test", "User", 30000, 'Java') 


# In[120]:


print(dev1.email)
print(dev1.prog_lang)


# In[157]:


class Manager(Employee):
    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
            
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
            
    def print_emp(self):
        for emp in self.employees:
            #print(emp.name)
            #print(emp)
            print('--->', emp.fullname())


# In[158]:


mgr1 = Manager('Jane', 'Doe', 50000, [])
print(mgr1.email)
print(mgr1.employees)


# In[160]:


mgr1 = Manager('Jane', 'Doe', 50000, [dev1,dev2, Developer('Gaurav', 'Sharma', 35000,'R')])
print(mgr1.email)
#mgr1.add_emp(dev2)
mgr1.print_emp()


# In[164]:


mgr1.remove_emp(dev2)
mgr1.print_emp()
mgr1.remove_emp(dev1)
mgr1.print_emp()


# In[166]:


print(mgr1.pay)
print(mgr1.raise_amount)
mgr1.apply_raise()
print(mgr1.pay)


# In[ ]:


help(Manager)


# In[168]:


print(isinstance(mgr1, Manager))
print(isinstance(mgr1, Employee))
print(isinstance(mgr1, Developer))


# In[170]:


print(issubclass(Developer, Manager))
print(issubclass(Developer, Employee))
print(issubclass(Developer, Developer))


# ## Special (Magic/Dunder) Methods

# In[196]:


class Employee():
    
    num_emps = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
            self.first = first
            self.last = last
            self.pay = pay
            self.email = first + '.' + last +'@company.com'
        
            Employee.num_emps+= 1
            
    def fullname(self):
        return self.first + ' ' + self.last
        #return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        #self.pay = int(self.pay * 1.04)
        self.pay = int(self.pay * self.raise_amount)
        #self.pay = int(self.pay * Employee.raise_amount)
        
    @classmethod
    def set_raise_amt(cls, amount):
        #pass
        cls.raise_amount = amount
    @classmethod
    def from_string(cls,emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    
    def __repr__(self):
        return "Employee('{}','{}','{}')".format(self.first, self.last, self.pay)
    
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)
    
    def __add__(self, other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())


# In[197]:


emp_1 = Employee('Aakash', 'sahu', 20000)
emp_2 = Employee('Test', 'User', 25000)

print(emp_1)


# In[198]:


print(emp_1)
print(emp_1.__repr__())
print(emp_1.__str__())
print(repr(emp_1))
print(str(emp_1))


# In[199]:


print(1+2)
print(int.__add__(1,2))
print(str.__add__('a','b'))


# In[200]:


print(emp_1 + emp_2)


# In[201]:


print(len('test'))
print('test'.__len__())


# In[203]:


print(len(emp_2))


# ## Getter, Setter, and Deleters

# In[249]:


class Employee():

    
    def __init__(self, first, last):
            self.first = first
            self.last = last
            #self.email = first + '.' + last +'@company.com'
    
    @property
    def email(self):
        return '{}.{}@compnay.com'.format(self.first, self.last)

    @property        
    def fullname(self):
        #return self.first + ' ' + self.last
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter
    def fullname(self, name):
        self.first, self.last = name.split(' ')  
        
    @fullname.deleter
    def fullname(self):
        print('Delete Name!') 
        self.first = None
        self.last = None


# In[245]:


emp_1 = Employee('John', 'Smith')
print(emp_1.first)
print(emp_1.last)
print(emp_1.email)
emp_1.first = 'Jim'
print(emp_1.first)
print(emp_1.last)
print(emp_1.email)


# In[246]:


emp_1 = Employee('John', 'Smith')
print(emp_1.first)
print(emp_1.last)
print(emp_1.email)
emp_1.first = 'Jim'
print(emp_1.first)
print(emp_1.last)
print(emp_1.email)
print(emp_1.fullname)


# In[250]:


emp_1 = Employee('John', 'Smith')
emp_1.fullname = 'Aakash Sahu'
print(emp_1.first)
print(emp_1.last)
print(emp_1.email)


# In[237]:


#del emp_1
print(emp_1.first)
print(emp_1.last)
print(emp_1.email)
print(emp_1.fullname)


# In[251]:


del emp_1.fullname

  
