#!/usr/bin/python3
import os
import py_compile

# The Python file name will be stored in the environment variable $PYFILE
PYFILE = os.environ.get('PYFILE')

# Compile the Python file
py_compile.compile(PYFILE)

# The output filename has to be $PYFILEc
base, ext = os.path.splitext(PYFILE)

# Rename file
os.rename(PYFILE + 'c', base + 'c')
