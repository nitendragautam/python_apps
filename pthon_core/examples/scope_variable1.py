#!/usr/local/bin/python


## Scope Resolution

temp= 10 # Global scope variable

def p_func():
    temp = 20 # Local scope variable
    print(" From p_func")
    print(temp)


print(temp)    #==>10
p_func()       # ===> 20
print(temp)    #===>10
