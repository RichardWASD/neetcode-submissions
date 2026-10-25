class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        U:
            I: List of ints
            O: boolean
            C:
            E: Empty list
        I: 
        '''
        
        # map or set works here

        seen = set()
        for i in range(len(nums)):

            if(nums[i] in seen):
                return True
            seen.add(nums[i])
        return False