"""UVa 10001 - Garden of Eden"""

import sys
import psyco


def get_case(in_line):
	automaton, num_cells, goal_state = in_line.rstrip().split()
	return automaton, num_cells, goal_state


def translate_automaton(automaton):
	binary_string = '{0:{fill}8b}'.format(int(automaton), fill='0')[::-1]	
	automaton_dict = {}
	for i in range(len(binary_string)):
		automaton_dict['{0:{fill}3b}'.format(i, fill='0')] = binary_string[i]
	return automaton_dict


def invert_automaton(auto_dict):
	inverted_dict = {}
	
	for key, value in auto_dict.items():
		if not value in inverted_dict:
			inverted_dict[value] = []
		inverted_dict[value].append(key)
	return inverted_dict


def generate_map(auto_dict):
	generated_map = {'000' : [('000', auto_dict['000']),
						      ('001', auto_dict['001'])],
					 '001' : [('010', auto_dict['010']),
						      ('011', auto_dict['011'])],
					 '010' : [('100', auto_dict['100']),
						      ('101', auto_dict['101'])],
					 '011' : [('110', auto_dict['110']),
						      ('111', auto_dict['111'])],
					 '100' : [('000', auto_dict['000']),
						      ('001', auto_dict['001'])],
					 '101' : [('010', auto_dict['010']),
						      ('011', auto_dict['011'])],
					 '110' : [('100', auto_dict['100']),
						      ('101', auto_dict['101'])],
					 '111' : [('110', auto_dict['110']),
						      ('111', auto_dict['111'])] }
	return generated_map


def dfs(invert_dict, gen_map, index, goal_state, first=None, prev=None):

	curr_val = goal_state[index]
	if curr_val not in invert_dict:
		return False
	
	if index == 0:
		for choice in invert_dict[curr_val]:
			first = prev = choice
			if dfs(invert_dict, gen_map, index+1, goal_state, first, prev):
				return True
	elif index == (len(goal_state)-1):
		for choice_tuple in gen_map[prev]:
			if curr_val == choice_tuple[1]:
				candidate = choice_tuple[0]
				for tup in gen_map[candidate]:
					if tup[0] == first:
						return True
	else:
		for choice_tuple in gen_map[prev]:
			if curr_val == choice_tuple[1]:
				temp = prev
				prev = choice_tuple[0]
				if dfs(invert_dict, gen_map, index+1, goal_state, first, prev):
					return True
	return False


def main():
	psyco.full()
	in_stream = sys.stdin.readlines()
	
	for line in in_stream:
		automaton, num_cells, end_state = get_case(line)

		automaton_dict = translate_automaton(automaton)
		inverted_dict = invert_automaton(automaton_dict)
		map_dict = generate_map(automaton_dict)


		reachable = dfs(inverted_dict, map_dict, 0, end_state)
		if reachable:
			print('REACHABLE')
		else:
			print('GARDEN OF EDEN')


if __name__ == '__main__':
	main()
