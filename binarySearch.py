def binary_search(input_array, value):
    min = 0
    max = len(input_array)
    
    while 1:
        mid = (min + max)/2
        if input_array[mid] == value:
            return mid
        
        if input_array[mid] < value:
            min = mid + 1
        elif input_array[mid] > value:
            max = mid - 1
        
        if min > max:
            return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)
