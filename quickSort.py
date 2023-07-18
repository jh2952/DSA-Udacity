def swap_positions(arr, pos1, pos2):
    temp = arr[pos1]
    arr[pos1] = arr[pos2]
    arr[pos2] = temp

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap_positions(arr, i, j)
    
    swap_positions(arr, i + 1, high)
    return i + 1
            
def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)
    
    return arr
