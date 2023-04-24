import time
import threading


"""
Multi Threading in Python
"""

def calc_square(numbers):
    print("Calculating Squares of Numbers")
    for n in numbers:
        time.sleep(1)
        print('Square:', n*n)


def calc_cubes(numbers):
    print("Calculating Cubes of Numbers")
    for n in numbers:
        time.sleep(1)
        print('Cubes:',n*n*n)



array = [2,3,8,9]

current_time = time.time()

t1 = threading.Thread(target=calc_square, args=(array,))
t2 = threading.Thread(target=calc_cubes, args=(array,))


t1.start()
t2.start()


t1.join()
t2.join()


print("Done in Time: ",time.time()-current_time)
