def merge_sort(arr, left, right):
    if left >= right:
        return 
    
    mid = left + (right - left) // 2
    merge_sort(arr, left, mid)
    merge_sort(arr, mid+1, right)
    merge(arr, left, mid, right)

def merge(arr, left, mid, right):
    temp = []
    list1 = left
    list2 = mid + 1
    while list1 <= mid and list2 <= right:
        if arr[list1] <= arr[list2]:
            temp.append(arr[list1])
            list1 += 1
        else:
            temp.append(arr[list2])
            list2 += 1
    
    while list1 <= mid:
        temp.append(arr[list1])
        list1 += 1

    while list2 <= right:
        temp.append(arr[list2])
        list2 += 1

    i = left
    while i <= right:
        arr[i] = temp[i - left]
        i += 1


array = [38, 27, 43, 3, 9, 82, 10]
merge_sort(array, 0, len(array)-1)
print("Sorted array is:", array)