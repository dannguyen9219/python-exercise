# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries
# JS objects and JSON similar

# Create dictionary
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

print(person, type(person))

# Use constructor
person2 = dict(first_name='Dan', last_name='Nguyen')

print(person2)

# Get value
print(person['first_name'])
print(person.get('last_name'))

# Add key/value
person['phone'] = '555-555-5555'
print(person)

# Get dictionary keys
print(person.keys())

# Get dict items
print(person.items())

# Copy dict - similar to spread operator in JS
person2 = person.copy()
person2['city'] = 'Austin'

print(person2)

# Remove item
del(person['age'])
person.pop('phone')

print(person)

# Clear
person.clear()
print(person)

# Get length
print(len(person2))

# List of dict
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 25}
]

print(people)
print(people[0]['name'])