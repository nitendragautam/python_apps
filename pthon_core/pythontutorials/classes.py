# CLASSES & OBJECTS

"""
Double underscore means private property in Python Classes
which cannot be accessed from outside property
"""

'''Below is the Person Class with Getters and Setters'''
class Person:
    __name = ''
    __email = ''

    def __init__(self, name, email):
        self.__name= name
        self.__email = email

    def set_name(self,name):
        self._name = name

    def get_name(self):
        return self.__name

    def set_email(self,email):
        self._email = email

    def get_email(self):
        return self.__email

    def toString(self):
        return '{} can be contacted at {}'.format(self.__name,self.__email)


nitendra = Person('Nitendra','niten@gmail.com')

print(nitendra.get_name())
print(nitendra.get_email())


nitendra.set_name('Nitendra')
nitendra.set_email('niten@gmail.com')


print(nitendra.toString())


#Inheritance
class Customer(Person):
    __balance = 0

    def __init__(self, name, email, balance):
        self.__name = name
        self.__email = email
        self.__balance = balance
        super(Customer, self).__init__(name, email)
        #Calling the constructor of Person


    def set_balance(self,balance):
        self.__balance = balance

    def toString(self):
        return '{} has a balance of {} and can be contacted at {}'.format(self.__name,self.__balance,self.__email)


john = Customer(nitendra,'John Doe','jdoe@gmail.com' ,100)

print(john.toString())
