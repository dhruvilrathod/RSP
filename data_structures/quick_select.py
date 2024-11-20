def partition(arr, low, high):

    p = arr[high]
    swap_index = low

    for i in range(low, high):
        if arr[i] < p:
            arr[swap_index],arr[i] = arr[i],arr[swap_index]
            swap_index+=1
    
    arr[high], arr[swap_index] = arr[swap_index], arr[high]
    return swap_index

def quick_sort(arr, low, high, k):
    if low <= high:
        p = partition(arr, low, high)
        if k == p:
            return arr[p]
        if k > p:
            return quick_sort(arr, p+1, high,k)
        else:
            return quick_sort(arr, 0, p-1,k)


arr = [4,1,6,3,8,9,3,5]
print(quick_sort(arr, 0, len(arr)-1, 0))