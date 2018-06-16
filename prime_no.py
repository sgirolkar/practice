import math
import random

def is_prime(num):
    if num < 2:
        print(str(num) + " is not Prime")
        return False
    for i in range(2, int(math.sqrt(num))):
        if num % i == 0:
            print(str(num)+" is not Prime")
            return False
    print(str(num)+" is prime")
    return True


for i in range(0, 25):
    is_prime(random.randrange(0, 99999999))
