
def moveZeroes(nums):
    count = 0
    for num in nums:
        if num == 0:
            count = count +1

    for i in range(len(nums)):
        nums.pop(nums.index(0))
        nums.append(0)

nums = [1,2,0,0,1,2]

moveZeroes(nums)

print(nums)