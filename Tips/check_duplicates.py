
nums = [1, 2, 3, 2, 5]
has_duplicates = False

# check for duplicates by loop
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

# check for duplicates using sets
has_duplicates = len(nums) != len(set(nums))             
print(has_duplicates)

