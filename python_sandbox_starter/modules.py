# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# Core modules
import datetime
from datetime import date
import time
from time import time

# Pip module
from camelcase import CamelCase

# Import custom module
import validator
from validator import validate_email

today = datetime.date.today()
today2 = date.today() # when you import a function from a file
# timestamp = time.time()
timestamp2 = time()

print(today)
print(today2)
# print(timestamp)
print(timestamp2)

c = CamelCase()
print(c.hump('hello there world'))

# Using custom modules that you created
email = 'test@test.com'
if validate_email(email):
    print('Email is valid')
else:
    print('Email is not valid')