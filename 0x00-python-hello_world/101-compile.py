#!/usr/bin/python3
import os
import py_compile

# Store Python file name in environment variable $PYFILE
PYFILE = os.getenv('PYFILE')

# Compile the Python file
py_compile.compile(PYFILE)

# Console progress reporting
print('Compiling {} ...'.format(PYFILE))
