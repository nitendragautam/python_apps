import thread
import time

# Define a function for the thread

def print_time(threadName,delay):
    count=0
    while count < 5:
        time.sleep(delay)
        count +=1
        print "%s: %s" %(threadName, time.ctime(time.time()))


#Create two Threads

try:
    thread.start_new_thread(print_time, ("Thread-1",2,))
except:
    print "Error: Unable to Start Thread"


while 1:
    pass