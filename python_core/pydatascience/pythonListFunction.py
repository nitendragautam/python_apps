## List is an ordered and changeable sequence of elements.
# It can holds integers , characters, floats, strings and even objects


#List is created by using [] with elemnts seperated by comma
x = [1, 3, 2]


## List Functaion

# Returns sorted copy of the List
sorted(x) # Returns [1, 2, 3]

#Sorts the list in-place
x.sort() #returns none

#Reverse the order of element in X
reversed(x) # Returns [2, 3, 1]

## Reverse the List in Place
x.reverse() # Returns None

# Gives the length of the list
print(len(x))

# Counts the number of elements 2 in list
x.count(2)

print(x.count(2))



