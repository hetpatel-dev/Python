# Exercise 7: Common Sequence Ops
# Create a list nums = [10, 20, 30, 40, 50]. Demonstrate all of these operations, printing the result of each:

# len(nums)
# 20 in nums
# nums[1]
# nums[-1]
# nums[1:3]
# nums + [60, 70]
# nums * 2
# min(nums)
# max(nums)
# Then do the same for a tuple (10, 20, 30, 40, 50) — confirm all operations work on tuples too.

# list operations

print("List Operations\n")

nums = [10, 20, 30, 40, 50]

length = len(nums)
print(f"Length/Number of Items: {length}")

# membership checking
print(20 in nums)

# item access
print(nums[1])

# accessing last item
print(nums[-1])

# slicing sublist
print(nums[1:3])

# combining two lists
newlist = nums + [60, 70]  # + creates a new list, doesn't modify in-place
print(newlist)
print(newlist is nums)

# repeating items
print(nums * 2)

# minimum
minimum = min(nums)
print(f"Minimum: {minimum}")

# maximum
maximum = max(nums)
print(f"Maximum: {maximum}")

print("----------------------------------------------------------")

print("Tuple Operations\n")

# len(nums)
# 20 in nums
# nums[1]
# nums[-1]
# nums[1:3]
# nums + [60, 70]
# nums * 2
# min(nums)
# max(nums)

t_nums = (10, 20, 30, 40, 50)
print("Length: ", len(t_nums))

print(20 in t_nums)
print(t_nums[1])
print(t_nums[-1])
print(t_nums[1:3])
print(t_nums + (60, 70))
print(t_nums * 2)
print(min(t_nums))
print(max(t_nums))
