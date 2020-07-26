## Slicing a List

"""

Now we will learning about slicing a List and generating a new list based on that .

Slicing a list can be done by using the colon(:) inside the square bracket and indicating the position of index
which we want to slice. When we perform an slice it will return an array.
Let's consider a list containing countries
"""


countries = ['Nepal','USA','China','Thailand','India','Cambodia']

"""
Lets take only first two countries from the left by using colon sign.
"""

first_c = countries[:2]

print(first_c)

"""
>>> countries = ['Nepal','USA','China','Thailand','India','Cambodia']
>>> first_c = countries[:2]
>>> print(first_c)
['Nepal', 'USA']
"""

"""
Now we want all the elements beside the first two elements in the list
"""

last_c = countries[2:]

print(last_c)

"""
>>> last_c = countries[2:]
>>> print(last_c)
['China', 'Thailand', 'India', 'Cambodia']
"""

### Cppying a list
"""
Semi colon(:) withing the square bracket can be used to copy the list.
"""


new_count = countries[:]

print(new_count)

"""
>>> new_count = countries[:]
>>> print(new_count)
['Nepal', 'USA', 'China', 'Thailand', 'India', 'Cambodia']
"""