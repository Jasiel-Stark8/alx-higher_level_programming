#!/usr/bin/python3
# This python scripts iterates though all .py files adn runs the pycodestyle on the
# It returns "PASSED" if it meets the requirements || The standard output messasge from pycodestyle for debugging.
# I am fluent with python so i created a script to auto correct the codes per the pycodestyle v2.8.0 style
# If you are a beginner do it yourself and create the script! It isnt a bas thing :D

PYFILE = "$PYFILE"
for file in PYFILE:
    pycodestyle -c "${PYFILE}"
