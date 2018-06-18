import random


def do_rectangles_overlap(l1, r1, l2, r2):
    if (r2["y"] > l1["y"]) or (r1["y"] > l2["y"]):
        return False
    elif (l2["x"] > r1["x"]) or (l1["x"] > r1["x"]):
        return False
    else:
        return True


l1 = {"x": random.randint(0, 999), "y": random.randint(0, 999)}
r1 = {"x": random.randint(l1["x"]+5, 999), "y": random.randint(0, l1["y"]-5)}
l2 = {"x": random.randint(0, 999), "y": random.randint(0, 999)}
r2 = {"x": random.randint(l2["x"]+5, 999), "y": random.randint(0, l2["y"]-5)}
print(l1),
print(r1)
print(l2),
print(r2)
print do_rectangles_overlap(l1, r1, l2, r2)
