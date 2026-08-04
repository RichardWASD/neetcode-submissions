class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        '''
        U:
            I:Sorted array (May be rotated but still sorted)
            O: Index of target (-1: not in list)
            C: No Repeated items
            E: Negative numbers, 1 item
        I:
        1) How to split the array into less and greater
        2) how to pick which side to pick/ conditional
        '''
        l,r= 0, len(nums) - 1 ;
        while (l<=r): 
            mid = (l+r) // 2;
            if(nums[mid] == target):
                return mid;

            if(nums[l] <= nums[mid]): 
                if(nums[mid] < target or nums[l] > target):
                    l = mid+1;
                else:
                    r = mid - 1;  
            else: 
                if(nums[mid] > target or nums[r] < target):
                    r = mid-1;   
                else:
                    l = mid + 1;

        return -1;