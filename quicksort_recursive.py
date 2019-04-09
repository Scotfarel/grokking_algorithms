import random
 
 
def gen_array():
    return [random.randint(0, 100) for _ in range(100)]
 
def quicksort(array):
    print(array)
    if len(array) < 2:
        return array

    pivot = array[random.randint(0, len(array) - 1)]

    less = [elem for elem in array if elem <= pivot and elem is not pivot]
    greater = [elem for elem in array if elem > pivot and elem is not pivot]

    return quicksort(less) + [pivot] + quicksort(greater)
 
if __name__ == "__main__":
    array = gen_array()
    print(quicksort(array))
    