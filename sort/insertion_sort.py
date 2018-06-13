def insertion_sort(l):

    for i in range(0, len(l)):
        cur_ind = i
        value = l[i]
        while cur_ind > 0 and l[cur_ind-1] > value:
            l[cur_ind] = l[cur_ind-1]
            cur_ind = cur_ind-1

        l[cur_ind] = value
    print l


ls = [9, 3, 5, 1, 6, 9, 3, 4, 0]
insertion_sort(ls)

ls = [0, 0, 0, 0, 0]
insertion_sort(ls)

ls = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
insertion_sort(ls)

ls = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
insertion_sort(ls)

ls = []
insertion_sort(ls)

ls = ["a", "b", "w", "d", "x", "s", "j", "e", "k", "o"]
insertion_sort(ls)
