# =========================================================#
# If Conditions/Statements
# ========================================================#

"""
We use If statements to test particular conditions and respond appropriately
"""

#If Condition
"""
#Conditional Test
equals          x == 42
not equal       x != 42
greater than    x > 45
    or equal to x >= 45
less than       x < 45
    or equal to x <= 45
"""

#Conditional Test with List
"""
'Tiger' in animals
'Dog' not in animals
"""





## Testing Conditions

testNum = 55
## equals
if testNum == 55:
    print("{0} equals 55" .format(testNum))

# Not Equal
if testNum != 43:
    print(" {0} Not Equals to 43".format(testNum))

#Greater than
if testNum > 30:
    print("{0} is Greater than 30 ".format(testNum))

# Greater than or Equals to
if testNum >= 55:
    print("{0} is Greater than or Equals to 42".format(testNum))

# Greater than or Equals to
if testNum >= 35:
    print("{0} is Greater than or Equals to 42".format(35))

## Less than
if testNum < 90:
    print("{0} is Less than 90 ".format(90))

## Less than or euqals to

if testNum <= 90:
    print("{0} is less than or equals to 90".format(testNum))


# Using Condition for Lists
"""
Lets Make a list of different Series i have watched before.
We will use the if condition to check whether i have watched a series or not
"""

fav_series=['Game of Thrones','Into the Badlands','Breaking Bad']

# Check if Prison Break is in this list

if 'Prison Break' in fav_series:
    print("Favorite Series")
else:
    print("Not Favorite Series")

if 'Game of Thrones' in fav_series:
    print("Favorite Series")
else:
    print("Not Favorite Series")



# Boolean Values with If Condition

"""
Boolean Values are assigned using True and False Values
"""
is_eligible =True
can_play_game=False

if is_eligible: # True condition By Default
    print("Is Eligible")
elif not is_eligible:  # Check if value of is_eligible is False
    print(" Check for Negtive")
if can_play_game:
    print("Can Play Game")
else:
    print("Cannot Play Game")


# Using iF Else Statements

"""To use a If Else Statement we need to use if and elif """
person_age =19

if person_age >18 & person_age<70:
    print("A Person Can Vote")
elif person_age< 18:
    print("A Person Cannot Vote")
elif person_age> 71:
    print("Person Cannot Vote")


#Conditionals

x = 8

# If Statement
if x < 6:
    print('This is True')


# If Else

if x <6:
    print('This is true')
else:
    print('This is False')



# ElIf statement

color = 'red'
if color == 'red':
    print('Color is red')
elif color == 'blue':
    print('Color is blue')
else:
    print('Color is neither red nor blue')

#Nested If Statement

if color == 'red':
    if x < 10:
        print('Color is red and x is less than 10')

#Logical Operator
if color == 'red' and x < 10:
    print('Color is red and x is less than 10')


