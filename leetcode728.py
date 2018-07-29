class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        List = []
        flag = 1
        for x in range(left,right+1):
            temp = x
            while temp >= 1:
                every_bit = temp % 10
                if every_bit == 0:
                    flag = 0
                    break
                if x % every_bit != 0:
                    flag = 0
                    break
                else:
                    flag = 1
                    temp = temp//10

            if flag == 1:
                List.append(x)

        print(List)

Solution().selfDividingNumbers(1,22)
