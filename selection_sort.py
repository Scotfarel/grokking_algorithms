import random
 
 
def make_row():
    return [random.randint(0, 100) for _ in range(10)]

def find_smallest(array):
	smallest = array[0]
	s_index = 0

	for index in range(len(array)):
		if array[index] < smallest:
			smallest = array[index]
			s_index = index
	return s_index

def selection_sort(array):
	sorted_arr = []
	for _ in range(len(array)):
		sorted_arr.append(array.pop(find_smallest(array)))
	return sorted_arr

if __name__ == "__main__":
	row = make_row()
	print(selection_sort(row))
