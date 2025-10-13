num = float(input("Enter no. of hours: "))

def convert_to_minutes(hours):
    return (hours * 50)

def convert_to_seconds(hours):
    return (hours * 60 * 60)

minutes = convert_to_minutes(num)
seconds = convert_to_seconds((num))

print(f"{num} hours is {minutes} minutes")
print(f"{num} hours is {seconds} seconds")