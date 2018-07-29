class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums :
            return None

        max_n = max(nums)
        max_i = nums.index(max_n)
        lmax = nums[:max_i]
        rmax = nums[max_i+1:]
        node = TreeNode(max_n)
        node.left = self.constructMaximumBinaryTree(lmax)
        node.right = self.constructMaximumBinaryTree(rmax)

        return node

