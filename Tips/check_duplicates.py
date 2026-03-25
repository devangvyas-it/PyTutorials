
nums = [1, 2, 3, 2, 5]
has_duplicates = False

# The "brute-force" way: check for duplicates using a nested loop (O(n^2) complexity)
# Loop through each number by its index
for i in range(len(nums)):
    # Compare it with every number that comes AFTER it
    for j in range(i + 1, len(nums)):
        if nums[i] == nums[j]:
            has_duplicates = True
            break
    if has_duplicates:
        break

print(has_duplicates)

# The "Pythonic" way: check for duplicates using sets (O(n) complexity)
# A set only contains unique elements. If the length of the list is different
# from the length of the set created from it, there must be duplicates.
has_duplicates = len(nums) != len(set(nums))             
print(has_duplicates)
