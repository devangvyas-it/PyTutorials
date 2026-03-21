# The ""SLOW WAY" (many lines!)
squares = []

for x in range(5):
    squares.append(x * x)

print(squares) 
# Output: [0, 1, 4, 9, 16]

# The "Pythonic SMART WAY" (List Comprehension)
squares = [x * x for x in range(5)]

print(squares)
# Output: [0, 1, 4, 9, 16]