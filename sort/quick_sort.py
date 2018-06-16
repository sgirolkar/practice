
def quick_sort(l, start, end):
    if start < end:
        pivot = partition(l, start, end)
        quick_sort(l, start, pivot-1)
        quick_sort(l, pivot+1, end)


def partition(l, start, end):
    pivot = l[end]
    p_ind = start

    for i in range(start, end):
        if l[i] <= pivot:
            tmp = l[i]
            l[i] = l[p_ind]
            l[p_ind] = tmp
            p_ind += 1
    tmp = l[p_ind]
    l[p_ind] = l[end]
    l[end] = tmp

    return p_ind


ls = [9, 3, 5, 1, 6, 9, 3, 4, 0]
quick_sort(ls, 0, len(ls)-1)
print(ls)

ls = [0, 0, 0, 0, 0]
quick_sort(ls, 0, len(ls)-1)
print(ls)

ls = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
quick_sort(ls, 0, len(ls)-1)
print(ls)

ls = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
quick_sort(ls, 0, len(ls)-1)
print(ls)

ls = []
quick_sort(ls, 0, len(ls)-1)
print(ls)

ls = ["a", "b", "w", "d", "x", "s", "j", "e", "k", "o"]
quick_sort(ls, 0, len(ls)-1)
print(ls)
