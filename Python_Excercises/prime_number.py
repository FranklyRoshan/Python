
def is__prime(a):
    
    print("Check 1")
    if (a <= 1):
        return False    # Numbers <= 1 are not prime
    
    print("Check 2")
    if (a == 2):
        
        return True     # 2 is the only even prime
    
    print("Check 3")
    if (a%2 == 0):
        return False    # Other even numbers are not prime

    print("Check 4")
    for i in range(3, int(a**0.5) + 1, 2):
        if(a%i == 0):
            return False 
    return True
       
num = int(input("Enter a number: "))
if is__prime(num):
    print(f"{num} is a Prime Number.")
else:
    print(f"{num} isn't a Prime Number.")   


""" Python's range() function is exclusive of the upper bound — it stops before reaching it.

    For example:

    range(3, 10, 2)  # → 3, 5, 7, 9 (stops before 10)

    In your prime-checking loop:

    for i in range(3, int(n**0.5) + 1, 2):

    int(n**0.5) gives the largest integer ≤ √n.
    Since range excludes the upper limit, you add +1 to ensure int(n**0.5) is included in the loop.    
    
     Example: n = 25
        √25 = 5 → int(n**0.5) = 5
        Without +1: range(3, 5, 2) → checks i = 3 only
        With +1: range(3, 6, 2) → checks i = 3, 5 ✅

    So +1 compensates for range's exclusivity.  """


''' def check_all_conditions(n):
        result = None
        checked = []

        if n <= 1:
            checked.append("n <= 1")
            result = False

        if n == 2:
            checked.append("n == 2")
            result = True

        if n % 2 == 0:
            checked.append("n % 2 == 0")
            result = False

        print("Checked conditions:", checked)
        return result

    print(check_all_conditions(0))
    # Output: Checked conditions: ['n <= 1'] → returns False (still skips rest)   '''

''' A prime number is a natural number greater than 1 that has exactly two distinct positive divisors: 1 and itself. This means it cannot be formed by multiplying two smaller natural numbers.

    For example:

    ✅ Prime: 2, 3, 5, 7, 11, 13 (each divisible only by 1 and itself)
    ❌ Not prime (composite): 4 (2×2), 6 (2×3), 8 (2×4)
    Key facts:

    2 is the only even prime number.
    1 is not considered a prime number.
    Numbers greater than 1 that are not prime are called composite numbers. '''