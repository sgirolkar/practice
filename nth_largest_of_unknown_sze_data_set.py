import random

curr = -1
# random.randint(0, 999)
data = [random.randint(0, 999) for p in range(0, 10)]
print "Input is \n"+str(data)


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
            for i in range(0, len(top_n)):
                if len(top_n) < n:
                    top_n.append(j)
                elif j > top_n[i]:
                    tmp = top_n[i]
                    top_n[i] = j
                    if i+1 < len(top_n):
                        top_n[i+1] = tmp
        if len(top_n) == n:
            nth_largest = top_n[-1]
        j = get_next()
    print "\n\nTop N are \n"+str(top_n)
    return nth_largest


print "\n\nNth largest is "+str(get_nth_largest(3))
