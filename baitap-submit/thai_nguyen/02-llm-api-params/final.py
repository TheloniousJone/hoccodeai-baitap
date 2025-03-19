import random

# Get input for matrix dimensions
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Generate a matrix of random numbers
matrix = [[random.randint(1, 10) for _ in range(cols)] for _ in range(rows)]  

# Print the matrix to the console
for row in matrix:
    print(row)