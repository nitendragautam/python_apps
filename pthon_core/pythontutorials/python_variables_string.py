

msg = 'Hello World!'
print(msg)

# Concatenate String
first_name = 'Nitendra'
second_name = 'Gautam'
full_name = first_name +second_name
print(full_name)

# A String
print("My Name is Nitendra Gautam")
print('This is my Blog')

"""
>>> print("My Name is Nitendra Gautam")
My Name is Nitendra Gautam
>>> print('This is my Blog')
This is my Blog
"""

# A String with a Variable
"""To define a String with a variable, we can directly use the variable name.
Python will infer the data type automatically"""
first_name = "Nitendra"
last_name = "Gautam"
blog_tag = 'This is my Blog'

# Printin using print command
"""Here we use the print command to print the  varialbles we prevously defined"""
print("{0} {1} {2}".format(first_name,last_name,blog_tag))

"""
>>> first_name = "Nitendra"
>>> last_name = "Gautam"
>>> blog_tag = 'This is my Blog'
>>> print("{0} {1} {2}".format(first_name,last_name,blog_tag))
Nitendra Gautam This is my Blog
"""


# Defining a number with a variable
"""We can define a numerical variable similar to String without using the single or double quotes"""

lucky_num=3

print("{0} is my lucky Number ".format(lucky_num))

"""
>>> lucky_num=3
>>> print("{0} is my lucky Number ".format(lucky_num))
3 is my lucky Number

"""


"""
We can define the String in Pythin in single, double and triple quote
"""
myStr = 'Hello World!'

print("Hello World")
print('''Hello there
blah
''')

print("Hello There")

## Pring String in Upper Case
print(" Upper Case Format{0}".format(myStr.upper()))


# Print String in Lower Case

print(" Lower Case: {0}".format(myStr.lower()))

#Capitalize
print(myStr.capitalize())

#Swap Case (Changes the case of all the Letters)
print(myStr.swapcase())

#Get Length of String
print(len(myStr))

# Replace words in string
print(myStr.replace('World', 'Everyone'))


# Count Substring in a string
print(myStr.count('l'))

#Startswith : Returns true if a string starts with given input parameters
print(myStr.startswith('Hello'))

#EndsWith: Returns true if a String ends with given input parameters
print(myStr.endswith('World'))
print(myStr.endswith('!'))
#Split String to List
print(myStr.split())

#Find positions of Substring
print(myStr.find('World'))

#Find Index of SubString
print(myStr.index('W')) #Gives Index of W

#Check if String has alphanumeric characters
print('Hello'.isalnum())


dog_name = "Benny"

# Python has replaced all the value of the variable dog_name with Benny

print("""My dog's name is {dog_name}. {dog_name} is cute and good boy""".format(**locals()))
