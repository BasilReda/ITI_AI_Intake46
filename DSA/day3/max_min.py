def max_min(arr, left, right, Max=None, Min=None):
    if left == right:
        Max = Min = arr[left]
    elif (right - left) == 1:
        if(arr[left] > arr[right]):
            Max = arr[left]
            Min = arr[right]
        else:
            Max = arr[right]
            Min = arr[left]
    else:
        mid = left + (right - left) // 2
        Max1, Min1 = max_min(arr, left, mid, Max, Min)
        Max2, Min2 = max_min(arr, mid + 1, right, Max, Min)
        if Max1 > Max2:
            Max = Max1
        else:
            Max = Max2
        
        if Min1 < Min2:
            Min = Min1
        else:
            Min = Min2
    return Max, Min

arr = [5, 2, 8, 1, 9, 3]
max_val, min_val = max_min(arr, 0, len(arr) - 1)
print(f"Max: {max_val}, Min: {min_val}")