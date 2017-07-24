def selection_sort(arr):
    sorted = [arr[0]]
    for x in arr[1:]:
        if x >= sorted[len(sorted) - 1]:
            sorted.append(x)
        elif x <= sorted[0]:
            sorted.insert(0, x)
        else:
            max = len(sorted) - 1
            for i in range(max - 1, -1, -1):
                if sorted[i] <= x:
                    sorted.insert(i+1, x)
                    break
    return sorted
print(selection_sort([1,2,3,4, -1, 0]))
