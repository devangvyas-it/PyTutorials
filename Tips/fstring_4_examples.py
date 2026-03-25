# Example 1: Basic variable interpolation
name = "Alex"
print(f"Hello {name}")
# Output: Hello Alex

# Example 2: Formatting a float to 2 decimal places
pi = 3.14159265
print(f"{pi:.2f}")
# Output: 3.14

# Example 3: Padding a number with leading zeros
num = 7
print(f"{num:03}")
# Output: 007

# Example 4: Self-documenting expressions (Python 3.8+)
# This is great for debugging
x = 10
y = 5
print(f"{x=}, {y=}")
# Output: x=10, y=5