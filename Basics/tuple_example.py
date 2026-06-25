print("\n=== TUPLE (Vault) ===")

# Create a tuple
my_tuple = ("passport", "certificate", "degree")
print("Original Tuple:", my_tuple)

# Try to change (this will cause an error)
try:
    my_tuple[0] = "license"
except TypeError as e:
    print("Error:", e)
