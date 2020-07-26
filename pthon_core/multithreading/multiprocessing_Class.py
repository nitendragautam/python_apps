import multiprocessing



class MyClass:
    def fun(self, myList):
        print('Printing My List')
        print myList

def unwrap_fun(myList):
    obj = MyClass()
    return obj.fun(myList)



if __name__ == '__main__':
    mlp = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    mlp.imap(unwrap_fun, range(1, 10))
    mlp.close()
    mlp.join()