import sys


class SelectionSort:

	def __init__(self, array):
		self.array = array

	'''
		Return index of the smallest item in an array
	'''
	def _find_smallest(self, offset):
		min_val = sys.maxsize
		min_index = -1

		for index, item in enumerate(self.array[offset:]):
			if item < min_val:
				min_val = item
				min_index = index + offset
		return min_index

	def sort(self, array=None):
		if array != None:
			self.array = array

		for index in range(len(self.array)):
			min_index = self._find_smallest(index)
			tmp = self.array[index]
			self.array[index] = self.array[min_index]
			self.array[min_index] = tmp

		return self.array


