class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        '''
        U:
            I: Array of Ints
            O: Array "ans" = Concatenation of 2 nums array
            C:
            E:
        '''
        if not nums:
            return -1
        n = len(nums)
        ans = [None] * n*2
        # ans[i] = nums[i]
        # ans[i+n] = nums[i] for 0<= i <= n 
        for i in range (len(nums)):
            ans[i], ans[i+n] = nums[i],nums[i]
        return ans

 