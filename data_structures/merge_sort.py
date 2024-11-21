# Time Complelxity: O(n * log n)
def merge_sort(arr, low, high):
    if low < high:
        middle = (low + high) // 2 
        merge_sort(arr, 0, middle)
        merge_sort(arr, middle+1, high)
        merge(arr,low,middle,high)
    return arr


def merge(arr,low,middle,high):
    left = arr[low:middle]
    right = arr[middle:high]
    i=0 # pointer for left
    j=0 # pointer for right
    k=low # pointer to array
    while i < len(left) and j < len(right):
        if left[i]<=right[j]:
            arr[k]=left[i]
            i+=1
        else:
            arr[k]=right[j]
            j+=1
        k+=1
    while i < len(left):
        arr[k]=left[i]
        i+=1
        k+=1
    while j < len(right):
        arr[k]=right[j]
        j+=1
        k+=1



arr = [4,1,6,3,8,9,3,5]
print(merge_sort(arr, 0, len(arr)-1))