import random
 
 
def make_row():
    return [random.randint(0, 100) for _ in range(100)]
 
 
def binary_search_recursive(sorted_lst, item):
    print(sorted_lst)
    low = 0
    top = len(sorted_lst) - 1
        
    if len(sorted_lst) == 0:
        return None

    mid = int((low + top) / 2)
    guess = sorted_lst[mid]

    
    if item == guess:
        return mid
    elif item > guess:
        return binary_search_recursive(sorted_lst[mid + 1:], item)
    else:
        return binary_search_recursive(sorted_lst[:mid - 1], item)
 
 
if __name__ == "__main__":
    row = make_row()
    sorted_row = sorted(row)
    print(binary_search_recursive(sorted_row, 10))
    