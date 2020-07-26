#=====================
# TUPLES
#=============

"""
Tuples are similar to list where we can add values in pair.Tuples are similar to List whose items cannot be modified
We can add any type of value in tuple.
But the values needs to be within pair of small brackets.
Once we create a tuple, we can't modify the value in the tuple
"""


#geo_address is atuple having Latitude and Longitude
geo_address=(32.814018, -96.948894)

year_tuple = ((2009,2011,"Nitendra"),(2001,2009,"Gautam"))

print(year_tuple)

"""
(2001, 2009)
>>> year_tuple = ((2009,2011,"Nitendra"),(2001,2009,"Gautam"))
>>> print(year_tuple)
((2009, 2011, 'Nitendra'), (2001, 2009, 'Gautam'))
"""

"""
We can use the for loop to print the Value of the Tuple
"""
for val in year_tuple:
    print (val)

"""
>>> for val in year_tuple:
...     print(val)
...
(2009, 2011, 'Nitendra')
(2001, 2009, 'Gautam')
"""