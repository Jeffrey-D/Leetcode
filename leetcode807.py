class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_top_bottom = []
        max_left_right = []
        result =  []
        last = 0
        for i in range(len(grid)):
            #max_top_bottom.append(max(grid[i]))
            max_left_right.append(max(grid[i]))  #get the biggest list from left to right

        for j in range(len(grid)):
          temp = 0
          for k in range(len(grid)):
            temp = max(temp,grid[k][j])
          max_top_bottom.append(temp)           #get the biggest list from top to bottom

        #create the list of the answer
        for i in range(len(grid)):
          result.append(max_top_bottom.copy())
          #print(result)
          for j in range(len(grid)):
            result[i][j] = min(result[i][j],max_left_right[i])
            #print(max_left_right[i] , result[i][j])
            #print(result)
            
        #calculate the sum of the add
        #last = sum(map(sub(),result,grid)
        for i in range(len(grid)):
          for j in range(len(grid)):
            if result[i][j] > grid[i][j]:
              last = last + result[i][j] - grid[i][j]

        #print(last)
 
        #print(max_left_right,max_top_bottom)