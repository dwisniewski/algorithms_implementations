import argparse

class InputArrayException(Exception):
	pass


def prepare_array(str_representation):
	try:
		return sorted([int(i) for i in str_representation.split(" ")])
	except:
		raise InputArrayException


def binary_search(sorted_array, to_search):
	low = 0
	high = len(sorted_array) -1 
	
	if len(sorted_array) == 1:
		if sorted_array[0] == to_search:
			return 0

	while low < high:
		middle = low + int((high - low) / 2)
		
		if to_search < sorted_array[middle]:
			high = middle - 1
		elif to_search > sorted_array[middle]:
			low = middle + 1
		else: 
			return middle

	return -1


def main(array, search_val):
	print(binary_search(array, search_val))


if __name__ == '__main__':
	arg_parser = argparse.ArgumentParser(description='Implementation of binary search algorithm, for given integers array and value to search it returns the index of a value in a sorted version of that array.')
	arg_parser.add_argument('-i', '--input', help='Array to search for selected item, should be a sequence of integers separated by space', required=True)
	arg_parser.add_argument('-s', '--search_val', help='Value to search for in an array', required=True)
	arguments = arg_parser.parse_args()
	input_array_processed = None
	value_to_search = None

	try:
		input_array_processed = prepare_array(arguments.input)
		value_to_search = int(arguments.search_val)
		
		main(input_array_processed, value_to_search)
	except InputArrayException:
		print("Your input array is wrong. Does it consist of only numbers separated by single space?")
	except ValueError:
		print("Your value to search is probably not a single integer. Please provide correct integer.")
	

