import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(module)s:%(message)s')

file_handler = logging.FileHandler('employee.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        logger.info('Created employee {} - {}'.format(self.fullname, self.email))
    
    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first, self.last)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
emp1 = Employee('John', 'Smith')
emp2 = Employee('Jane', 'Doe')   