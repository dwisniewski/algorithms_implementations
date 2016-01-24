import argparse
from SelectionSort import SelectionSort

class AlgorithmException(Exception):
	pass

def main(algorithm, input_array):
	if algorithm == 'selection':
		selection_sort = SelectionSort(input_array)
		print(selection_sort.sort())


if __name__ == '__main__':
	arg_parser = argparse.ArgumentParser(description='Implementation of sorting algotihms')
	arg_parser.add_argument('-a', '--algorithm',  help='Algorithm to be used. Can be: selection/', required=True)
	arg_parser.add_argument('-i', '--input', help='Input array separated by single space (ex. 1 2 3 5)', required=True)
	args_parsed = arg_parser.parse_args()

	input_array = None
	algorithm = None
	
	try:
		input_array = [int(x) for x in args_parsed.input.split(" ")]
		if args_parsed.algorithm not in ['selection']:
			raise AlgorithmException

		main(args_parsed.algorithm, input_array)
	except ValueError:
		print("Wrong array. Input array should consist of integers separated by single space.")
	except AlgorithmException:
		print("Unsupported algorithm.")
