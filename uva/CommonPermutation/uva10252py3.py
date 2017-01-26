import sys
import itertools

def compare_words(first, second):
	first_dict = {}
	second_dict = {}
	
	solution = str('')
		
	for c1 in first:
		if c1 not in first_dict:
			first_dict[c1] = 1
		else:
			first_dict[c1] += 1
	
	for c2 in second:
		if c2 not in second_dict:
			second_dict[c2] = 1
		else:
			second_dict[c2] += 1

	for key in sorted(first_dict):
		if key in second_dict:
			solution += ( str(key) * min(first_dict[key], second_dict[key]) )

	return solution
			
def main():
	with sys.stdin as lines:
	
		for line1, line2 in itertools.zip_longest(*[lines]*2):
			first_str = line1.rstrip()
			second_str = line2.rstrip()

			print(str(compare_words(first_str, second_str)))
		
		
main()
