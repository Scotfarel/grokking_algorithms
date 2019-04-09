import random
 
 
def make_row():
    return [random.randint(0, 100) for _ in range(100)]
 
 
def binary_search(sorted_lst, item):
    low = 0
    top = len(sorted_lst) - 1
 
    while low <= top:
        mid = int((low + top) / 2)
        guess = sorted_lst[mid]
 
        if guess == item:
            return mid
        elif guess > item:
            top = mid - 1
        elif guess < item:
            low = mid + 1
    return None
 
 
if __name__ == "__main__":
    row = make_row()
    sorted_row = sorted(row)
    print(sorted_row)
 
    print(binary_search(sorted_row, 10))
    