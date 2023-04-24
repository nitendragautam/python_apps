import multiprocessing
import time

def print_cube(number):
    time.sleep(20)
    print("Cube: {}".format(number * number * number))


def print_square(number):
    time.sleep(10)
    print("Square: {}".format(number * number))



if __name__ == '__main__':
    p1 = multiprocessing.Process(target=print_square, args=(10,))
    p2 = multiprocessing.Process(target=print_cube, args=(10,))


    print("Starting Process 1 for Square")
    p1.start()

    print("Starting Process 2 for Cube")

    p2.start()

    # Wait Until process 1 is Finished
    p1.join()
    # Wait Until Process 2 is Finished
    p2.join()

    print("Both Process Done ")