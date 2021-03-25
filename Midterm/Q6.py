import timeit

def total(nums):
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    else:
        return nums.pop() + total(nums)

def sum(nums):
    total = 0
    for i in nums:
        total += i
    return total

nums = [5, 3, 8, 4, 2]
print(sum(nums))
print(total(nums))