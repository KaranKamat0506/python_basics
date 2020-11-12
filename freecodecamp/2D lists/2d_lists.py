#2D lists
number_grid=[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[0][0])

#Nested For loops
print("Printing each column value")
for row in number_grid:
    for col in row:
        print(col)
