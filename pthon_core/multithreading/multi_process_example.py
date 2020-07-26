import os

from multiprocessing import Process

def doubler(number):
    """
    A doubling Function that can be used by the Process
    """
    results = 2 * number
    proc = os.getpid()
    print('{0} doubled to {1} by process id: {2}'.format(number, results,proc))


