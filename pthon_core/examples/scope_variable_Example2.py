#!/usr/local/bin/python


temp = 10  # Global scope variable

def p_func():
    global temp
    temp = 20  ## Local Variable Scope
    print(temp)

print(temp)     #Output ==>10
p_func()        #Output  ==>20
print(temp)   #Output ==> 20