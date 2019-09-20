#!/usr/bin/env python3
# Program to print first 10 prime numbers in Python 3
# Program by Satyam Faujdar
# Contribute to the open Repository 

def main():
	count = 0		#Count to counter the Prime Numbers for printing only first 10 Prime Numbers
	# N is set to 0 so that we can check from prime numbers from 0 
	n = 0
	# while loop to output only 10 results
	while count < 10:
		# check if is_prime function return True for n
		# if it return true print n
		# and increase count and n by 1 
		if is_prime(n):
			print(n)
			count += 1
			n += 1
		# if the fucntion dosent return True
		# increase the n by 1 so that we can check next for next number 
		else:
			n += 1

def is_prime(n):
	# Check whether number is 1 or smaller than 1
	# If it is Smaller than one return False
	if n <= 1:
		return False
	#Check if number is equal to 2
	#If it is equal to 2 return True because 2 is also a prime number
	if n == 2:
		return True
	# Run a loop form 2 to n-1
	# If any number between 2 to n-1 divides n completely it is not a prime number
	# Hence Return False 
	for x in range(2, n):
		if n % x == 0:
			return False
	#If none of the above conditions apply True then the number is a prime number
	# Hence Return True 
	else:
		return True

	
if __name__ == '__main__':
	main()
	
	