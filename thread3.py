#!/usr/bin/python3

from time import sleep
from random import randint
from _thread import start_new_thread, allocate_lock

num_threads = 0
thread_started = False
lock = allocate_lock()

def print_num(elem, val1):

        global num_threads, thread_started

        lock.acquire()

        print('[[[ Function call %d - Random Value is: %d ]]]' % (elem, val1))
        print("\t<<< lock.acquire for Thread %d >>>" % (elem))
        print("\t\tActive Threads Count [Before Incrementing]: %d" % (num_threads))
        print("\t\tValue of thread_started is", thread_started)
        print("\t\tIncrementing value of active threads")
        num_threads += 1
        thread_started = True
        lock.release()
        print("\t<<< lock.release for Thread %d >>>" % (elem))
        print("\t\tActive Threads Count [After Incrementing] : %d" % (num_threads))
        print("\t\tValue of thread_started is", thread_started)

        print("\n\t%s" % ('*' * 44))
        print('\t* Function call %d - sleeping for %d seconds *' % (elem, val1))
        print("\t%s\n" % ('*' * 44))

        sleep(val1)

        print("\n\t%s" % ('=' * 40))
        print('\t| Function call %d woke up for printing |' % (elem))
        print("\t%s\n" % ('=' * 40))

        for var in range(1,4):
                print('\tFunction call %d - Task %d' % (elem, var))
                sleep(1)

        print("\t<<< lock.acquire for Thread %d >>>" % (elem))
        print("\t\tActive Threads Count [Before Decrementing]: %d" % (num_threads))
        print("\t\tValue of thread_started is", thread_started)
        print("\t\tDecrementing value of active threads")
        lock.acquire()
        num_threads -= 1
        lock.release()
        print("\t<<< lock.release for Thread %d >>>" % (elem))
        print("\t\tActive Threads Count [After Decrementing] : %d" % (num_threads))
        print("\t\tValue of thread_started is", thread_started)
        print('%s<<< THREAD %d TERMINATED >>>%s\n' % ("#" * 10, elem, "#" * 10))


def main():
        for elem in range(1,4):
                start_new_thread(print_num, (elem, randint(1,10)))

#       sleep(1)

        while not thread_started:
                pass

        while num_threads > 0:
                pass

if __name__ == '__main__':
        main()
