import random
 
 
def gen_array():
    return [random.randint(0, 100) for _ in range(100)]
 
def quicksort(array):
    print(array)
    if len(array) < 2:
        return array

    pivot = array[0]
    less = [elem for elem in array[1:] if elem <= pivot]
    greater = [elem for elem in array[1:] if elem > pivot]

    return quicksort(less) + [pivot] + quicksort(greater)
 
if __name__ == "__main__":
    array = gen_array()
    print(quicksort(array))
    