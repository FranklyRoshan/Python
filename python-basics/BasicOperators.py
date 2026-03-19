
def arithmetic_operators():

    # Arthimatic Operations
    print("Arthimatic Operators")
    num_a = int(input("Enter a number(num_a): ")) 
    num_b = int(input("Enter a number(num_b): "))

    print(f"\nResults for inputs: {num_a} and {num_b}")

    # 1. Addition
    result_add = num_a + num_b
    print(f"Addition ({num_a} + {num_b}): {result_add}")

    # 2. Subtraction
    result_sub = num_a - num_b
    print(f"Subtraction ({num_a} - {num_b}): {result_sub}")

    # 3. Multiplication
    result_mul = num_a * num_b
    print(f"Multiplication ({num_a} * {num_b}): {result_mul}")

    # 4–6. Division operations (only if num_b is not zero)
    if num_b != 0: 
        # 4. Standard Division
        result_div_float = num_a / num_b
        print(f"Division ({num_a} / {num_b}): {result_div_float}")

        # 5. Floor Division
        result_div_int = num_a // num_b
        print(f"Floor Division ({num_a} // {num_b}): {result_div_int}")

        # 6. Modulo (Remainder) 
        result_mod = num_a % num_b
        print(f"Modulo ({num_a} % {num_b}): {result_mod}")

    else: 
        print("Division, floor division, and modulo are not allowed with divisor 0.")

def assignment_operators():

    # Assignment Operators
    print("\nAssignment operators")
    # Compound Assignment Operators
    a = int(input("Enter a number(a): ")) 

    a += 5      # a = a + 5
    print("After a += 5: ", a)

    a -= 2      # a = a - 2
    print("After a -= 2: ", a)

    a *= 3      # a = a * 3
    print("After a *= 3: ", a)

    a /= 2      # a = a / 2
    print("After a /= 2: ", a)

    a %= 4      # a = a % 4
    print("After a = a % 4: ", a)

    # Increment/Decrement Operators
    # Increment/Decrement (manually — no ++ or -- in Python)
    a = 5
    a = a + 1 # increment
    print("After Increment (a = a + 1): ", a)

    a = 5
    a += 1
    print("After Increment (a += 1): ", a)

    a -= 1
    print("After Decrement (a -= 1): ", a)

    # Assignment Operator (=)
    a = int(input("Enter a number(a): ")) 
    b = int(input("Enter a number(b): "))

    # comparison Operators
    print("Is a equal to b?", a == b)   # False
    print("Is a equal to 10?", a == 10) # True


# Run the function
arithmetic_operators()
assignment_operators()
