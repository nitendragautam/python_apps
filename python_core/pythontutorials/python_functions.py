

"""
FUNCTIONS:
Functions are named block of code,designed to do one specific job.
I
Information passed to a function is called argument and information received by function is called a parameter.

function in Python is created by using the def word
"""


## Simple Finction

def foo():
    """Greets the User"""
    print("Hello World !")

foo()



## Passing an Argument to the function

def foo_arg(name):
    print("Hello, {0}!".format(name))


foo_arg("Nitendra")