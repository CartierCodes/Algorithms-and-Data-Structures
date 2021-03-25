def reverse(nums):
    for i in range(len(nums)):
        nums.insert(i, nums.pop())

nums = [1, 2, 3, 4, 5]
print("The original nums:", nums)
reverse(nums)
print("The reversed nums:", nums)