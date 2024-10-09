"""
Do you want to become a true pythonista?
Read through this file to learn intermediate python

Becoming a pytonista, tips and tricks to write beatiful python code
"""

# Dunders
"""Every Python variable is an object or derives from object even things like numbers. 

Every variable has special methods and properties on them which come from object. 
But only special because the python machine looks for them.

You can see all the things that a variable has with 
"""


# Propper file iteration

"""I often see that people read a file like this:"""

with open("file.txt") as file:
    for line in file.readline():
        print(line)

"""Doing the with is nice but the readlines is super bad
The file variable is already an iterator. Which means that 

"""

"""
propper file iteration in plaats van lelijke en slechte .readlines()
enumerate
poetry, of uv
list generators, te grote list generators,
if met negative case in plaats van else
hoe werkt with?
decorators
een bytes is gewoon een list van int van 0 tot 256
typed python
generic types in python
dunder methods
generators
yield from
2 way generators
Maak een persistant dict
Easy multiprocessing zonder dependencies
set and generator comprehensions
Watch video on two from mcoding about 15 features or code smells
"""