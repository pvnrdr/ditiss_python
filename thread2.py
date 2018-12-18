#!/usr/bin/python3

from time import sleep
from random import randint
from _thread import start_new_thread

num_threads = 0

def print_num(elem, val1):
        global num_threads
        print(">>> Active Threads Count [Before Incrementing]: %d" % (num_threads))
        print("### Incrementing value of active threads")
        num_threads += 1
        print(">>> Active Threads Count [After Incrementing] : %d" % (num_threads))

        print('Function call %d - Random Value is: %d' % (elem, val1))
        print('Function call %d - sleeping for %d seconds' % (elem, val1))

        sleep(val1)

        print('Function call %d woke up for printing' % (elem))
        for var in range(1,4):
                print('\tFunction call %d - Task %d' % (elem, var))
                sleep(1)
        print(">>> Active Threads Count [Before Decrementing]: %d" % (num_threads))
        print("### Decrementing value of active threads")
        num_threads -= 1
        print(">>> Active Threads Count [After Decrementing] : %d" % (num_threads))
        print('*' * 30 + '\n')


def main():
	for elem in range(1,4):
		start_new_thread(print_num, (elem, randint(1,10)))
	sleep(1)
	
	while num_threads > 0:
		pass

if __name__ == '__main__':
        main()
