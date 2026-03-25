# This script demonstrates three different ways to merge or update dictionaries in Python.

# Starting data
profile = {"name": "Alex", "gender": "Male"}

# --- METHOD 1: The .update() method (Modifies in-place) ---
# This is the classic way. It modifies the original `profile` dictionary directly.
updates = {"email": "alex@email.com"}
profile.update(updates)
print(profile)
# Output:
# {'name': 'Alex', 'gender': 'Male', 'email': 'alex@email.com'}

# --- METHOD 2: Dictionary Unpacking `{**...}` (Creates a new dictionary) ---
# Available since Python 3.5. This creates a new dictionary by unpacking others.
# It does not modify the original dictionaries. If keys overlap, the right-most value wins.
updates = {"email": "alex_new@email.com", "plan": "Basic"}
result = {**profile, **updates}
print(result)
# Output:
# {'name': 'Alex', 'gender': 'Male', 'email': 'alex_new@email.com', 'plan': 'Basic'}

# --- METHOD 3: Merge Operator `|=` (Modifies in-place, Python 3.9+) ---
# Introduced in Python 3.9, this provides a concise syntax for an in-place update.
# It modifies the dictionary on the left of the operator (`result` in this case).
updates = {"plan": "Pro"}
result |= updates
print(result)
# Output:
# {'name': 'Alex', 'gender': 'Male', 'email': 'alex_new@email.com', 'plan': 'Pro'}