def selection_sort(l):
    for i in range(0, len(l)):
        min_index = i
        m = l[i]
        for j in range(i+1, len(l)):
            if l[j] < m:
                min_index = j
                m = l[j]
        l[min_index] = l[i]
        l[i] = m
    print(l)


ls = [9, 3, 5, 1, 6, 9, 3, 4, 0]
selection_sort(ls)

ls = [0, 0, 0, 0, 0]
selection_sort(ls)

ls = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
selection_sort(ls)

ls = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
selection_sort(ls)

ls = []
selection_sort(ls)

ls = ["a", "b", "w", "d", "x", "s", "j", "e", "k", "o"]
selection_sort(ls)

