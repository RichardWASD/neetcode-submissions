class Solution: # Orginal solution of thought 2 
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        components = {} # val -> index (Learn dif between set and this notation)
        for i, n in enumerate(nums): #learn notation
            needed = target - n

            if(needed in components):
                return [components[needed], i]
               
            components[n] = i # Explain