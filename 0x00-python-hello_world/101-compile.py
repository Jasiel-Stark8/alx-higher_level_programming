#!/usr/bin/python3
import os
import sys

# Assuming the python file name is passed as a command-line argument
PYFILE = sys.argv[1]

# Execute the python file
os.system(f'python3 {PYFILE}')

# Get the base name without extension
base = os.path.splitext(PYFILE)[0]

# Append 'c' at the end of the filename
os.rename(PYFILE, base + 'c')
