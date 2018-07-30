class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # if this > pior and this > next------>find it 
        # if next < this <pior -----------> left 
        # if pior < this <next ------------>right
        B = A.copy()
        # length = len(B)
        print(A)
        flag = 0
        while flag != 1:
            length = len(B)
            print(B)
            if B[length//2] > B[length//2 - 1] and B[length//2] > B[length//2 + 1]:
                return length//2
                flag = 1
            elif B[length//2] > B[length//2 + 1] and B[length//2] < B[length//2 -1]:
                # peakIndexInMountainArray(A[:length//2])
                B = B[:length//2]
            else:   
                # peakIndexInMountainArray(A[length//2:])
                B= B[length//2:]




A = [0,3,2,1,0]
result = Solution().peakIndexInMountainArray(A)
print(result)