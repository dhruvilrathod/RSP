def partition(arr, low, high):

    p = arr[high]
    swap_index = low

    for i in range(low, high):
        if arr[i] < p:
            arr[swap_index],arr[i] = arr[i],arr[swap_index]
            swap_index+=1
    
    arr[high], arr[swap_index] = arr[swap_index], arr[high]
    return swap_index

def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, 0, p-1)
        quick_sort(arr, p+1, high)
    return arr


arr = [4,1,6,3,8,9,3,5]
print(quick_sort(arr, 0, len(arr)-1))