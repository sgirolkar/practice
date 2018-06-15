import math


def merge_sort(l):
    if len(l) < 2:
        return l
    m = int(math.ceil(len(l)/2))
    lr = l[:m]
    ll = l[m:]
    merge_sort(lr)
    merge_sort(ll)

    ri = 0
    li = 0
    for i in range(0, len(l)):
        if ri < len(lr) and li < len(ll):
            if lr[ri] < ll[li]:
                l[i] = lr[ri]
                ri += 1
            else:
                l[i] = ll[li]
                li += 1
        elif ri == len(lr):
            l[i] = ll[li]
            li += 1
        elif li == len(ll):
            l[i] = lr[ri]
            ri += 1
    return l


ls = [9, 3, 5, 1, 6, 9, 3, 4, 0]
print merge_sort(ls)

ls = [0, 0, 0, 0, 0]
print merge_sort(ls)

ls = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print merge_sort(ls)

ls = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print merge_sort(ls)

ls = []
print merge_sort(ls)

ls = ["a", "b", "w", "d", "x", "s", "j", "e", "k", "o"]
print merge_sort(ls)
