#!/bin/bash
for file in .; do
    python3 -c 'print(__import__("0-add_integer").__doc__)'
    python3 -c 'print(__import__("0-add_integer").add_integer.__doc__)'
done
