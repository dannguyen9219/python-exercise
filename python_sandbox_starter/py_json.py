# JSON is commonly used with data APIs. Here how we can parse JSON into a Python dictionary

import json

# Sample JSON
userJSON = '{"first_name": "Dan", "last_name": "Nguyen", "age": 30}'

# Parse to dict
user = json.loads(userJSON)

print(user)