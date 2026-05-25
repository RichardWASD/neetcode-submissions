class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1 # Pointers 
        max_area = 0
        while l < r : 
            width = r - l
            length = min(heights[l], heights[r])
            area = length * width # Find how to round down here (Python3)
            if(area > max_area):
                max_area = area
            if(heights[l] <= heights[r]):
                l +=1 
            else:
                r -=1
            
        return max_area


# Area = L * W 
# Width = r - l
# Length = minOf l and r 
