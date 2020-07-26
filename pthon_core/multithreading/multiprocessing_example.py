import multiprocessing


def spawn1(num):
    print("Spawn1",num)


def spawn2(num):
    print("Spawn2",num)

if __name__ == '__main__':
    for i in range(25):
        p1 = multiprocessing.Process(target=spawn1, args=(i,))
        p2 = multiprocessing.Process(target=spawn2, args=(i,))
        p1.start()
        p2.start()

        p1.join()
        p2.join()

        