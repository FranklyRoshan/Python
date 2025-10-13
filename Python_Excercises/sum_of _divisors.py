def sum_of_divisor():
    a = int(input("Enter a number: "))

    sum_div = 0
    for i in range (1, a+1):
        if(a%i == 0):
            sum_div += i
    
    print(f"Sum of Divisor of {a} is: {sum_div}")

sum_of_divisor()

def divisors_and_sum(n):
    divisors = [i for i in range(1, n + 1) if n % i == 0]
    return divisors, sum(divisors)

# Example usage
num = int(input("Enter a number: "))
div_list, div_sum = divisors_and_sum(num)
print(f"Divisors of {num}: {div_list}")
print(f"Sum of divisors: {div_sum}")   