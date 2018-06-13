def bubble_sort(l):
    for i in range(0, len(l)):
        for j in range(0, len(l)-1):
            if l[j+1] < l[j]:
                tmp = l[j+1]
                l[j+1] = l[j]
                l[j] = tmp

    print l


ls = [9, 3, 5, 1, 6, 9, 3, 4, 0]
bubble_sort(ls)

ls = [0, 0, 0, 0, 0]
bubble_sort(ls)

ls = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
bubble_sort(ls)

ls = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
bubble_sort(ls)

ls = []
bubble_sort(ls)

ls = ["a", "b", "w", "d", "x", "s", "j", "e", "k", "o"]
bubble_sort(ls)
