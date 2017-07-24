def binary_search(v, arr):
    """binary searches for a value, 
    v : the value to be searched
    arr: the arr to be searched
    """
    if not len(arr):
        return -1
    if arr[0] == v:
        return 0
    if arr[len(arr) -1] == v:
        return len(arr) - 1
    elif len(arr) == 1:
        return -1
    mid = (len(arr)) // 2
    if v > arr[mid]:
        index = binary_search(v, arr[mid:])
        index = mid+index if index > 0  else -1
    elif v < arr[mid]:
        index = binary_search(v, arr[:mid])
    else:
        index = mid
    return index
