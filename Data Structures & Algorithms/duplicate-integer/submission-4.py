class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        U:
            I: List of Int
            O: Boolean
            C:
            E:
        '''
        if(not nums):
            return False
        # inList = {} empty dict
        inList = set()

        for num in nums:
            if(num in inList):
                return True
            inList.add(num)
        return False
            