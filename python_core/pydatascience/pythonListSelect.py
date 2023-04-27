## Selecting list Elements
## Python list are zero indexed which means first element has 0 index
# For Ranges, it includes the first element but not the last one

## Define a sample list
x = ['a' ,'b', 'c', 'd', 'e', 'f']

## Select first element in the list
x[0] # 'a'

# Select last element in the lits
x[-1] # 'f'

#Selecyt 1st(Inclusive) to 3rd(exclusive) Range
x[1:3] #['b', 'c']

#Select 3rd to the End{3rd element is not exclusive}
x[3:] # ['d','e','f']


## Select 0th element to the 4rd(Exclusive)
x[:4] #['a','b','c','d']