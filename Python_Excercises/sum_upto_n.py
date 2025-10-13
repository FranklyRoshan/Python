def sum_upto_n():
    print("The sum of the first n natural numbers by using \"For Loop\"")
    a = int(input("Enter a number: "))

    sum = 0
    for i in range(1, a+1):
        sum += i
    
    print(f"The sum of the first {a} natural numbers is:  {sum}")

sum_upto_n()


''' The sum of the first n natural numbers is calculated using the formula:

    Sum = n(n + 1) / 2

    For example:

    If n = 5, Sum = 5 × 6 / 2 = 15
    If n = 10, Sum = 10 × 11 / 2 = 55
    This formula efficiently adds all integers from 1 to n. '''

''' Here is a Python program to calculate the sum of the first n natural numbers 
    using the mathematical formula:    '''


def sum_upto_n_by_using_formula():
    print("\nThe sum of the first n natural numbers by using \"Mathematical Formula\"")
    n = int(input("Enter a number: "))
    sum_n = n * (n + 1) // 2
    print(f"The sum of the first {n} natural numbers is: {sum_n}")   
sum_upto_n_by_using_formula()