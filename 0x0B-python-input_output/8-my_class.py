#!/usr/bin/python3
import json
dict = {
    'name': "Jonah",
    'Age': 40,
    'Class': [1, 2, 3]
}

print(json.dumps(dict))