class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {} # Dictionary Key val pair 
        for i in range(len(nums)):
            curr = nums[i]
            needed = target - curr
            
            if(needed in complements):
                return [complements[needed], i]
            complements[curr] = i # assigns the val with index in dictionary

