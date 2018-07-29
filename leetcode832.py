'''
leetcode 832 write by ish
'''

class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """

        for col in A:
            col.reverse()
        for i in range(len(A)):
            for j in range(len(A)):
                if A[i][j] == 1:
                    A[i][j] = 0
                else:
                    A[i][j] = 1

        print(A)


A = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0],]


Solution().flipAndInvertImage(A)

