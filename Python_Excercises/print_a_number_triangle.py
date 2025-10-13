def print_a_number_triangle(num):
    for i in range (1, (num + 1)):
        for j in range (1, (i+1)):
            print(j, end=' ')
        print()

a = int(input("Enter a number: "))
print_a_number_triangle(a)