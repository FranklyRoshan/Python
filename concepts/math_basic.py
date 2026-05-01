def print_squares_of_numbers_upto(n):
    for i in range(1, n+1):
        print(i*i)


def print_squares_of_even_numbers_upto(n):
    for i in range(2, n+1, 2):
        print(i*i)


def print_numbers_in_reverse(n):
    for i in range(n,0,-1):
        print(i)


# Function with return value (Normal return)	
def sum_of_two_number(num1, num2):
    sum = num1 + num2
    return sum


# Function without return (Implicit return)
def null_return_type():
    print("Hello, World!") # only prints, no return

result = null_return_type()
print("Returned Value: ", result)


# Function with return None (Explicit return)
def check_even(number):
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")
        return None # Explicitly return None when number is odd

result = check_even(7)
print("Returned value: ", result)

 
# print_squares_of_numbers_upto(10)
# print_squares_of_even_numbers_upto(10)
# print_numbers_in_reverse(10)
print(sum_of_two_number(7, 5))

'''  ⚙️ Summary
    Case	                    Returns	    Description
    Function without return	    None	    Implicit return
    Function with return None	None	    Explicit return
    Function with value	        That value	Normal return   '''

