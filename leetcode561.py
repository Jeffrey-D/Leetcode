class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        result = 0
        n = len(nums)
        if n % 2 != 0:
            return
        for x in nums[::2]:
            result += x
        return result


nums = [2,1,3,4]

Solution().arrayPairSum(nums)