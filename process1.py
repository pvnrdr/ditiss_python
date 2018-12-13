#!/usr/bin/python3 -tt

from time import sleep
from random import choice

def new_one(random_number):
	print('Sleeping for',random_number,'seconds')
	sleep(random_number)
	for elem in range(1,6):
		print(elem)
def main():
	counter = [1,2,3,4,5,6,7,8,9,10]
	new_one(choice(counter))
	new_one(choice(counter))

if __name__ == "__main__":
	main()
