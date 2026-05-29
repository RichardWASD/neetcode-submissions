class Solution:
    '''
    U: 
        I: list of num
        O: [i,j]
        C: i < j
        E: negative numbers in list
    I: hashmap  of vals in list with respected index 

    '''
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {};

        for i, num in enumerate(nums):
            needed = target- num
            if(needed in hashmap):
                return [hashmap[needed] ,i ];
            hashmap[num] = i;
        return [];