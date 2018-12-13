#!/usr/bin/python3 -tt

from _thread import start_new_thread
from time import sleep
from random import choice

def time_print(t_num,ran_num):
	print("%s \nThread %d started and sleeping for %d seconds.\n%s" % ("=" * 43,t_num,ran_num,"=" * 43 ))
	sleep(ran_num)
	print("%s \nThread %d woke up\n%s" % ("*" * 16, t_num, "*" * 16))
	for elem in range(1,6):
		print("\nThread %d - Task %d" %(t_num, elem))
		sleep(1)

def main():
	counter = [1,2,3,4,5]
	start_new_thread(time_print, (1, choice(counter)))
	start_new_thread(time_print, (2, choice(counter)))
	c = input("Type something to quit.\n")

if __name__ == "__main__":
	main()
