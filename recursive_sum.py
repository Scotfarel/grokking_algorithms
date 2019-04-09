import random
 
 
def make_row():
    return [random.randint(0, 100) for _ in range(10)]

def sum(array):
	print(array)
	if len(array) == 1:
		return array[0]
	if len(array) == 0:
		return 0	
	
	digit = array[len(array) - 1]
	del array[len(array) - 1]
	return digit + sum(array)

if __name__ == "__main__":
    row = make_row()
    print(sum(row))
    