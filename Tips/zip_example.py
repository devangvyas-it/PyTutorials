# The zip() function is used to combine multiple iterables (like lists) element-wise.
# The itertools.zip_longest() function is similar but continues until the longest iterable is exhausted.

from itertools import zip_longest

names = ["Alice", "Bob", "Charlie"]
scores = [90, 85, 95]

# --- 1. The "Old" Way (C-style loop) ---
# This works, but it's not considered "Pythonic". It's less readable and more prone to off-by-one errors.
print("--- C-style loop ---")
for i in range(len(names)):
  print(names[i], scores[i])
# Output:
# Alice 90
# Bob 85
# Charlie 95

# --- 2. The "Pythonic" Way with zip() ---
# zip() pairs up elements from each list. It's cleaner and more direct.
print("\n--- zip() with equal length lists ---")
for name, score in zip(names, scores):
 print(name, score)
# Output:
# Alice 90
# Bob 85
# Charlie 95

# --- 3. zip() with unequal length lists ---
# What happens if one list is shorter? zip() stops as soon as the shortest list runs out of items.
scores = [90, 85]
print("\n--- zip() with unequal length lists (stops early) ---")
for name, score in zip(names, scores):
 print(name, score)
# Output:
# Alice 90
# Bob 85

# --- 4. Using zip_longest() for unequal lists ---
# If you want to iterate until the LONGEST list is done, use zip_longest().
# It fills missing values with `None` by default (or a custom `fillvalue`).
print("\n--- zip_longest() with unequal length lists ---")
for name, score in zip_longest(names, scores):
 print(name, score)
# Output:
# Alice 90
# Bob 85
# Charlie None
