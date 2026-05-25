class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        Rows = len(matrix) # rows = 3
        Cols = len(matrix[0]) # Columns = 4 
        top = 0
        bot = Rows -1

        while top <= bot: # traversing Rows 
            row = (top + bot) //2 # mid row from Binary Search
            if(matrix[row][-1] < target): # [row,end of row]; Similar to left
                top = row + 1
            elif(matrix[row][0] > target): # 
                bot = row - 1 
            else:
                break
        
# Above is the main function of the 2d array manipulation 
        if not (top <= bot):
            return False
      #  row = (top + bot) // 2 # WHY is this need
        l, r = 0,Cols-1

        while l <= r: 
            m = (l+r)//2 
            if(matrix[row][m] < target): 
                l = m +1
            elif(matrix[row][m] > target):
                r = m -1
            else: 
                return True 
        return False 