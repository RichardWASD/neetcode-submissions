class Solution:
    '''
    U:
        I: Sorted array + Target
        O: Indexs if found, else return where it would supposed to be 
        C: O log n 
        E:

    '''
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1;
        while(l <= r):
            m = (l+r)//2;

            if(nums[m] == target):
                return m;  
            elif(nums[m] > target):
                r = m-1;
            else:
                l = m +1;
        
        return l;
        