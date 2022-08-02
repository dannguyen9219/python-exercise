# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
# Create tuple
fruits = ('Apples', 'Oranges', 'Grapes')
# fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

# print(fruits, fruits2)

# Single value needs trailing comma
fruits2 = ('Apples',)
print(fruits2, type(fruits2))

# Get value
print(fruits[1])

# Can't change value
# fruits[0] = 'Pears'

# Delete tuple
del fruits2
# print(fruits2)

# Get length
print(len(fruits))

# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruits_set = {'Apples', 'Oranges', 'Mangos'}

# Check if in set
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grapes')
print(fruits_set)

# Remove from set
fruits_set.remove('Oranges')
print(fruits_set)

# Clear set
fruits_set.clear()
print(fruits_set)

# Delete set
del fruits_set
# print(fruits_set)