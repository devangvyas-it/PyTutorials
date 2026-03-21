# Normal function
def square(x):
    return x * x

print(square(5))   # 25

# Lambda function
square_lambda = lambda x: x * x

print(square_lambda(5))   # 25

# Using lambda with filter
nums = [1, 2, 3, 4, 5, 6]

evens = list(filter(lambda x: x % 2 == 0, nums))

print(evens)   # [2, 4, 6]