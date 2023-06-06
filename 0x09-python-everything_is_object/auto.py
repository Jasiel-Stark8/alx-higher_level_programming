#!/usr/bin/python3
import os

files = []
nums = range(6, 35)

# Populate the files list with file names
for num in nums:
    files.append(str(num) + '-answer.txt')

# Create the files if they don't exist
for file in files:
    if not os.path.exists(file):
        open(file, 'w').close()
