class Solution:
    '''
    U:
        I: Was Sorted Array -> Rotated
        O: Min number in the array
        C: Nums Wont always start at 1 
        E: Empty list
    I: Binary Search (Skewed)

    Notes
    '''
    def findMin(self, nums: List[int]) -> int:
        l,r = 0 , len(nums)-1;
        # small = nums[0];
        while (l < r):
            mid = l+(r-l) // 2;
            if(nums[mid] < nums[r] ):
                # go left 
                # small = nums[mid];
                r = mid;
            else:
                # go right 
                # small = nums[mid];
                l = mid+1;
        return nums[l];
        

