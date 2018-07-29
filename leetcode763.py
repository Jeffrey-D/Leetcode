class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        # words = list(S)
        # print(words)
        # index_left = 0
        # result = []
        # index_right = len(S) - 1
        # while index_left < len(S):
        #     index_right = S.find(len(S)-1,index_left)
        #     if index_right = -1:
        #         result.append(len(S[index_left:index_right]))
        #         index_left += 1
        #         continue
        #     for i in range(index_left,len(S)):
        max_right = len(S)
        index_left = 0
        while index_left < max_right:
            max_right = len(S) - S[len(S)-1:index_left:-1].find(S[index_left]) - 1
            print(max_right,index_left,S[len(S)-1:index_left:-1])
            break    



S = "mdiskldfam"
# print(S[len(S)-1:0:-1])
Solution().partitionLabels(S)