#This is a tuple, an immutable array

letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

print(letters[2])
print(letters.index('w'))

#This should return an error, since you cannot remove items from a tuple
# letters.pop(3)

#This should also return an error, since you cannot add items to a tuple
# letters.append('1')
