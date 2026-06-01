class Solution:
    '''
    U:
        I:List of numbers
        O: list of size 2 (i,j)
        E: Negative Numbers
        C:
    '''
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, num in enumerate(nums):
            
            if(target-num in hashmap):
                return [hashmap.get(target-num), i];
            hashmap[num] = i;
        return [];