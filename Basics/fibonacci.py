def fibonacci(n):
    """
    Generates the Fibonacci sequence up to n terms.

    Args:
        n (int): The number of terms to generate.

    Returns:
        list: A list containing the first n numbers of the Fibonacci sequence.
    """
    # Initialize the first two numbers of the sequence
    a, b = 0, 1
    # This list will store the resulting sequence
    result = []

    # Loop 'n' times to generate the desired number of terms
    for _ in range(n):
        # Append the current number 'a' to our result list
        result.append(a)
        # This is the core logic:
        # Update 'a' to the next number in the sequence (which is 'b')
        # and update 'b' to the sum of the previous two numbers (a + b)
        a, b = b, a + b

    # Return the final list of Fibonacci numbers
    return result

# --- Script Execution ---
# Call the function to generate the first 10 Fibonacci numbers and print them.
print(f"result: {fibonacci(10)}")
