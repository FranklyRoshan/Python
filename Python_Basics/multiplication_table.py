def print_multiplication_table(table=5, start=1, end=10): # Default Parameters
    for i in range (start, end+1):
        print(f"{table} x {i} = {table*i}")


print_multiplication_table()

print_multiplication_table (6)

print_multiplication_table(7, 1, 10)


''' Normal print: Outputs static text or concatenated strings. No dynamic value insertion.

        name = "Alice"
        print("Hello, " + name + "!")  # Concatenation

    Formatted print: Embeds variables directly into strings using formatting techniques:
        f-strings (modern): print(f"Hello, {name}!")
        .format(): print("Hello, {}!".format(name))
        % formatting: print("Hello, %s!" % name)    '''