class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        List = []
        for i in range(len(S)):
            if S[i] == C:
                List.append(0)
                continue
            index_l = S[i::-1].find(C)
            index_r = S[i:].find(C)
            # print(i,index_l,index_r)
            # if its not exist
            if index_l == -1:
                List.append(index_r)
            elif index_r == -1:
                List.append(index_l)
            else :
                List.append(min(index_l,index_r))
        # word = list(S)
        # print(List)
        return List
        

# S = "baaaa"
# index_l = S[0:0:-1].find('e')
# # # index_r = S[7:].find('e')
# # # print(index_l,index_r)
# # print(S[2:0:-1])
# C = 'b'
# a = Solution()
# a.shortestToChar(S,C)