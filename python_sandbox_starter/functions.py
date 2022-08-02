# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

# Create function
def sayHello(name):
    print(f'Hello {name}')

sayHello('John Doe')

# you can also run default arguments if no arguments are passed to the function like below
def sayHello2(name = 'Dan'):
    print(f'Hello {name}')

sayHello2()

# Return values
def getSum(num1, num2):
    total = num1 + num2
    return total

print(getSum(3, 5))

num = getSum(4, 5)
print(num)

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSum = lambda num1, num2 : num1 + num2

print(getSum(10, 3))