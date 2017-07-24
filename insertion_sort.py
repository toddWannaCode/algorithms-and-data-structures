def insertion_sort(l):
    for i in range(1, len(l)):
        j = i
        while j > 0 and l[j] < l[j - 1]:
            l[j], l[j-1] = l[j-1], l[j]
            j = j - 1
            print(l)
    return l
