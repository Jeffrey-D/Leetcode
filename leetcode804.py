class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
        morse=[
                ".-","-...","-.-.","-..",".","..-.",
                "--.","....","..",".---","-.-",".-..","--",
                "-.","---",".--.","--.-",".-.","...","-","..-",
                "...-",".--","-..-","-.--","--..",
                ]

        cards = [chr(i) for i in range(97,123)]
        #result = ""
        sol = set()
        com = dict(map(lambda x,y:[x,y],cards,morse))
        #print(com['g'])
        for word in words:
            temp = list(word)
            #print(temp)
            result = ""
            for i in range(len(temp)):
                if temp[i] in com:
                    a = temp[i]
                    result += com[a]
                    #print(result)
            sol.add(result)
        return len(sol)

        
#words = ["gin", "zen", "gig", "msg"]
#print(Solution().uniqueMorseRepresentations(words))
