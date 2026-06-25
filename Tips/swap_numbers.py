a = 5
b = 7

print(f"Before: a = {a}, b = {b}") 
# Output: Before: a = 5, b = 7
# Old way — needs a temp variable  
temp = a
a    = b
b    = temp
print(f"After:  a = {a}, b = {b}") 
# Output: After:  a = 7, b = 5

# Pythonic way
a = 5
b = 7

print(f"Before: a = {a}, b = {b}") 
# Output: Before: a = 5, b = 7
a, b = b, a
print(f"After:  a = {a}, b = {b}") 
# Output: After:  a = 7, b = 5
