# Multiplication Table Generator

# Ask the user for input
number = int(input("Enter the number for multiplication table: "))
range_limit = int(input("Enter the range (e.g., 10 for table till 10): "))

print(f"\nMultiplication Table for {number}:\n")

# Generate the table
for i in range(1, range_limit + 1):
    print(f"{number} x {i} = {number * i}")
