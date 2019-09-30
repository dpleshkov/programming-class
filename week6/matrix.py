#A matrix is a multidimensional array for storing data

matrix = [[2, 3, 9, 5], 
          [5, 9, 6, 3]]

print(matrix[1][3])

print('\n')

for y in range(len(matrix[0])):
    print((matrix[0][y], matrix[1][y]))