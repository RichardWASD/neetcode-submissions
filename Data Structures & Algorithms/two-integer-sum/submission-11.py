class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        U:
            I: Int list ; target int
            O: index (i,j) <- num[i] + num[j] == target 
            C: i!=j
            E:
        I:
        '''
        hashMap = {}
        for i in range(len(nums)):
            
            if(target-nums[i] in hashMap):
                return [hashMap[target-nums[i]],i]
            hashMap[nums[i]] = i
        return [-1,-1]