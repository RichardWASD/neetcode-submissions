class Solution: # Orginal solution of thought 2 
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        components = set()
        for i in  range(0, len(nums)):
            needed = target - nums[i]

            if(needed in components):
                if( i < nums.index(needed)):
                    return [i, nums.index(needed)]
                else:
                    return [nums.index(needed),i ]
            components.add(nums[i])