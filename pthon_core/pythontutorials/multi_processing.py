import time
import multiprocessing

"""
MultiProcessing in python 
"""
def calc_square(numbers):
    for n in numbers:
        print('square ' + str(n*n))
        time.sleep(2)


def calc_cube(numbers):
    for n in numbers:
        print('cube ' + str(n*n*n))

if __name__ == "__main__":
    array = [2,4,6,7]

    p1 = multiprocessing.Process(target=calc_square, args=(array,))
    p2 = multiprocessing.Process(target=calc_cube, args=(array,))

    #Start the Thread
    p1.start()
    p2.start()

    print("Is P1 Alive", p1.is_alive())
    print("Is P2 Alive", p2.is_alive())
    p1.join()
    p2.join()

    print('Done')