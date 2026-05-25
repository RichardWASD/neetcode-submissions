class Solution:
    '''
    U:
        I: list of nums
        O: list of 2 nums 
        C:
        E: Negative list + neg target
    I:
    '''
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i, n in enumerate(nums):
            diff = target - n 
            if(diff in hmap):
                return [hmap[diff], i];
            hmap[n] = i;

