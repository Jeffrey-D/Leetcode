class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        # times = []
        # url = []
        word = []
        words = ''
        result = dict()
        output = []

        for temp in cpdomains:
            # times.append(int(temp[:temp.index(' ')]))
            # url.append(temp[temp.index(' ')+1:])
            # words = ''.join(url)
            # word = words.split('.')
            # for temp1 in word:
            #     if temp1 in result:
            #         result[temp1] = times
            times = int(temp[:temp.index(' ')])
            # print(times)
            url = temp[temp.index(' ')+1:]
            words = ''.join(url)                 # Convert to a string
            # word.append()              # From string to a list that contain every choice
            index_i = 0
            while index_i < len(words):
                word.append(words[index_i:])
                index_i = words.find('.',index_i,len(words)) + 1
                # print(index_i)
                if index_i == 0:
                    break
                # print(index_i)
            # print(word)

            for temp1 in word:                   # add the result into the dictionary
                if temp1 in result:
                    # print(temp + " IN IT")
                    result[temp1] += times
                else :
                    # print(temp1 + " Not In")
                    result[temp1] = times

                # print(result)
            word.clear()
            times = 0
        for key,value in result.items():
            output.append(str(value) + ' ' + key)

        # print(result)

        # print(output)
        return output

            # word = url.split('.')
            # print(word)
            # print(url)
        # word = '.'.join(url)
        # word.split('.')
        # print(word)
        # # cpdomains_temp = list(cpdomains)
        # space_i = cpdomains_temp.index(' ')
        # times = cpdomains_temp[:space_i]
        # times = int(''.join(times))
        # print(word)
        
        



# cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
# #cpdomains_temp = list(cpdomains)

# Solution().subdomainVisits(cpdomains)