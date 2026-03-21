
# ===============================================================
# Prime Number
# ===============================================================

import math

def is_prime(num):
    """Checks whether the input argument is prime number or not"""
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False

    return True

num = input("Enter a Positive integer number: ")
print(is_prime(num))

