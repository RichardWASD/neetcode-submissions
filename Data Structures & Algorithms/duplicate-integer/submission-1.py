class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       seen = set() # Create hashtable
       for num in nums: #traverse Array -> not seen then add 
        if(num in seen):
            return True
        seen.add(num)    
       return False 