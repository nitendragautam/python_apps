from multiprocessing import Pool
import time

"""
Running Multithreading with a Class
"""

def unwrap_self_f(arg,**kwarg):
    return MultiThreadingExample.f(*arg, **kwarg)


class MultiThreadingExample:
    def f(self, name):
        print('hello %s, '%name)
        time.sleep(5)
        print('Nice to Meet You')

    def run(self):
        pool = Pool(processes=2)
        names=('Niten1','Niten2','Nit3')
        pool.map(unwrap_self_f, zip([self]* len(names), names))


if __name__ == '__main__':
    c = MultiThreadingExample()
    c.run()