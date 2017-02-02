import sys

'''Solution for uva problem 10041 - Vito's Family
   This solution takes advantage of the fact that the
   median of an ordered set of one-dimensional points
   provides the least sum of differences to all other
   points.'''

#This function calculates the sum of distances from the median
#of the (eventually ordered) list of street addresses to each other
#street address, thus returning the solution for a given test case.
def calculate_distance(line):
	first_list = line.split()		#Possibly unordered list
	num_list = [int(val) for val in first_list]		#Convert from str to int
	trash = num_list.pop(0)				#First number is useless; pop it 
	
	num_list.sort()					#Sort street addresses
	middle = int(len(num_list)/2)		#Index for median street address
	middle_val = num_list[middle]				#Median street address
	
	result = 0
	for i in range(0,len(num_list)):
		result += abs(int(middle_val) - int(num_list[i]))	#Sum distances
	return result					#Return sum of distances


def main():
	lines = sys.stdin
	number_of_test_cases = lines.readline().rstrip()
	
	for i in range(0, int(number_of_test_cases)):
		line = lines.readline().rstrip()
		print(calculate_distance(line))

main()
