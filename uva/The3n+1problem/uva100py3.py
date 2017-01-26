import sys

'''Collatz Conjecture -- Problem 100 on UVa Judging System.
   Submitted and Accepted.
   Written in Python3 by Jason Hammond'''

#The meat of the program; this function is a recursive implementation of the
#Collatz Conjecture -- If n is even, divide by 2. If odd, multiply by 3
#and add 1. Stop when the base case (n=1) is reached.
#
#Returns the count (including initial value; returns 1 if n=1).
def three_n_plus_one(n):
	cache = three_n_plus_one.cache #To prevent recalculation of previously
								   #found values
	if n not in cache:
		if n == 1:				#Base case
			cache[n] = 1
		elif n % 2 == 0:		#If even, divide by 2 and go again
			cache[n] = three_n_plus_one(n >> 1) + 1
		else:						#If odd, multiply by 3, add 1, go again
			cache[n] = three_n_plus_one(n * 3 + 1) + 1
	return cache[n]				#Return count of iterations

three_n_plus_one.cache = {}			#Global cache

def main():
	for line in iter(sys.stdin.readline, ''):		#For each input pair:
		first, last = line.split()
		if int(first) > int(last):				#If unordered, sort
			first_sorted = last
			last_sorted = first
		else:
			first_sorted = first
			last_sorted = last
		max_count = 1					#Track max iteration count
		for i in range(int(first_sorted), int(last_sorted) + 1):
			max_count = max(max_count, three_n_plus_one(i))	#Update max count
		print("%s %s %s" % (first, last, max_count))	#Format output

main()
