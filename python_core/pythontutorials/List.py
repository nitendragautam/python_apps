#
# ==================================================================
# LIST in Python
# ==============================================================

"""
List: It stores a series of items in particular order .
Items in a list can be accessed using an Index or Within a loop
List is an data structure which is used to Store a series of items in particular order.
We can access items in a list using an index or withing an loop
"""

## String List
#Make a List with String as Element
fruits = ['apple', 'banana','oranges','grapes']

cars_manufacture = ['Honda','Kia','Toyota','Hyundai']


"""
use the square bracket with the index within the bracket to get the item in the list 
Lets take the first item and 3rd item from the list
"""
first_fruit =fruits[0]

print(first_fruit)

first_m = cars_manufacture[0]
third_m = cars_manufacture[2]

print (first_m)
print(third_m)

#Get the last item in the list
last_fruit = fruits[-1]


"""
>>> cars_manufacture = ['Honda','Kia','Toyota','Hyundai']
>>> first_m = cars_manufacture[0]
>>> third_m = cars_manufacture[2]
>>> print (first_m)
Honda
>>> print(third_m)
Toyota
>>>

"""

#Loop through the List
for fruit in fruits:
    print(fruit)


#Adding Items to List
fruit_list =[]
fruit_list.append('Apple')
fruit_list.append('Banana')
fruit_list.append('Grapes')


#Numerical List
squares = []

#range is used for generating numbers with definitive range
for x in range(1,11):
    squares.append(x**2)

print(squares)

#List Comprehensions
#Same Squares can be generated in another way
squares = [x**2 for x in range(1,11)]

print(squares)

#Slicing a List
animals= ['Tiger','Lion','Fox']

first_two_animals=animals[:2]
print(first_two_animals)



#Copying a List
copy_of_animals = animals[:]

print(copy_of_animals)



## Gettin the last item in the list
"""We can get the last item of the list by using the last index in the square bracket or
use [-1] in the index"""
last_item1 = cars_manufacture[3]
last_item2 = cars_manufacture[-1]

print (last_item1)
print (last_item2)

"""
>>> last_item1 = cars_manufacture[3]
>>> last_item2 = cars_manufacture[-1]
>>> print (last_item1)
Hyundai
>>> print (last_item2)
Hyundai
>>>

As you can see both the value of last_item1 and last_item2 is the same.
"""

## Looping through the List

"""
to loop through the loop we use the for condition
"""
# It will print all the items in the cars_manufacture List
for car in cars_manufacture: \
    print(car)

"""
SyntaxError: unexpected character after line continuation character
>>> for car in cars_manufacture: \
...     print(car)
...
Honda
Kia
Toyota
Hyundai
"""

## Adding Items to a list

"""
Lets create a list for new Laptop Brands and add Items to it
"""

laptops = []

laptops.append('HP')
laptops.append('lenovo')
laptops.append('Dell')
laptops.append('Apple')
laptops.append('Acer')

## print the Laptop List
print(laptops)

"""
>>> laptops = []
>>> laptops.append('HP')
>>> laptops.append('lenovo')
>>> laptops.append('Dell')
>>> laptops.append('Apple')
>>> laptops.append('Acer')
>>> print(laptops)
['HP', 'lenovo', 'Dell', 'Apple', 'Acer']
"""


## Make Numerical Lists

"""
Here we make a numerical Lists using the numbers between 1 and 24
"""

num_sq1 = []

for x in range(1, 10):
    num_sq1.append(x**2)

print(num_sq1)

"""
>>> for x in range(1, 10):
...     num_sq1.append(x**2)
...
>>> print(num_sq1)
[1, 4, 9, 16, 25, 36, 49, 64, 81]
"""

## Creating the List using the Comprehension Technique

"""
We can create the same list as we created above by using the comprehension technqiues.
List Comprehension is a concise way to Create lists.

A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. 
The result will be a new list resulting from evaluating the expression in the context of the for and if clauses which follow it.
One important thing to note here is that, list comprehension always returns an result list

"""
num_squares = [x**2 for x in range(1, 10)]

"""
>>>
>>> num_squares = [x**2 for x in range(1, 10)]
>>> num_squares
[1, 4, 9, 16, 25, 36, 49, 64, 81]
"""

"""
Now we will use the if condition to filter out odd and even number
"""
num_squares_even = [x **2 for x in range(1,20) if x % 2 == 0]


num_squares_odd = [x**2 for x in range(1,20) if x% 2 !=0 ]

"""
>>> num_squares_even = [x **2 for x in range(1,20) if x % 2 == 0]
>>> num_squares_even
[4, 16, 36, 64, 100, 144, 196, 256, 324]
>>> num_squares_odd = [x**2 for x in range(1,20) if x% 2 !=0 ]
>>> num_squares_odd
[1, 9, 25, 49, 81, 121, 169, 225, 289, 361]
"""



