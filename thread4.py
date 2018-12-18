#!/usr/bin/python3 -tt

from time import sleep
from random import randint
from _thread import start_new_thread, allocate_lock


num_threads = 0
thread_started = False
lock = allocate_lock()

def print_num(elem,val1):
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

def main():
	for elem in range(1,4):
		start_new_thread(print_num, (elem, randint(1,5)))
	
	while not thread_started > 0:
		pass 
	while num_threads > 0:
		pass



if __name__ == "__main__":
	main()
