#==========================
# Dictionaries  in Python
#=========================

"""
A dictionary is a type of collection in which we store unordered,changeable and index value.
Dictionaries have multiple values written with curly braces in which each item has keys and values.

"""

## A Simple dictionaries of Person Information
"""
We can define a dictionary using a curly Bracket and Key-Value Pairs.

We can store both String and Numeric Values in the Dictionaries key-value pairs.
"""
person_info ={'first_name':'Nitendra',
              'last_name':'Gautam',
              'location':'Dallas',
              'website':'https://www.nitendratech.com',
              'zipcode':75060}


## Accessing the Value from a Dictionary

"""
We use the dictionary key to access the value for that particular key.
"""

print("First Name is {0}".format(person_info['first_name']))

## Adding a new Key Value Pair to dictionary

person_info['new_zipcode'] =76066

print("Updated Dictionary ",person_info)

## Looping through Key-value pairs

print("Printing Key-Value pairs of ")
for keys,values in person_info.items():
    print(keys + str(values))


## Looping through all keys in a Python dictionary

for key in person_info.keys():
    print("Person Info Dictionary Key {0}".format(key))

## Looping through All the values in the dictionary

for values in person_info.values():
    print("Person Info Dictionary Value {0}".format(values))



