import thread
import Queue

 # queue=Queue.queue()

def printThread(threadName, delay):
    print threadName + ": " + delay

def xyz():
    print "producer getting created"
    producer= thread.start_new_thread(printThread, ("Thread-1",1,))
    print "consumer getting created"
    consumer= thread.start_new_thread(printThread,  ("Thread-2",2,))


xyz()
