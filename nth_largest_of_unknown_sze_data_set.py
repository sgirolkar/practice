import random

curr = -1
data = [random.randint(0, 999) for p in range(0, random.randint(0, 999))]
print data


def get_next():
    global data
    global curr
    try:
        curr += 1
        return data[curr]
    except IndexError:
        return None


def get_nth_largest(n):
    nth_largest = None
    j = get_next()
    top_n = [j]
    while j is not None:
        if nth_largest is None or j > nth_largest:

            for i in range(0, len(top_n)-1):
                if j > top_n[i]:
                    tmp = top_n[i]
                    top_n[i] = j
                    top_n[i+1] = tmp
                elif len(top_n) < n and j not in top_n:
                    top_n.append(j)
        if len(top_n) >= n-1:
            nth_largest = top_n[-1]
        j = get_next()
    print top_n
    return nth_largest


print get_nth_largest(3)
