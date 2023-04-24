import threading
import time
import sys
import logging

logger = logging.getLogger(__name__)
def print_cube(number):
    time.sleep(5)
    cubes = number * number * number
    logger.info("Cube: {}".format(cubes))
    return "success"


def print_square(number):
    time.sleep(5)
    logger.info("Square: {}".format(number * number))



if __name__ == '__main__':

    log_file_name='sample.log'
    logging.basicConfig(filename=log_file_name,
                        format='[%(filename)s:%(lineno)s - %(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        stream=sys.stderr, level=logging.INFO)

    p1 = threading.Thread(target=print_square, args=(10,))
    p2 = threading.Thread(target=print_cube, args=(10,))


    logger.info("Starting Process 1 for Square")
    p1.start()

    logger.info("Starting Process 2 for Cube")

    p2.start()

    # Wait Until process 1 is Finished
    p1.join()
    # Wait Until Process 2 is Finished
    p2.join()

    logger.info("Both Process Done ")