class Solution:
    '''
    U:Sorted array + target = binary search 
        I: Sorted array And Target
        O: index of target
        C: 
        E:
    '''
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1;
        while(l <= r ):
            mid = (l+r) // 2; # Explain why floored

            # if(mid > len(nums)):
            #     if(nums)
            if(nums[mid] == target):
                return mid;
            elif (nums[mid] > target):
                r = mid -1;
            else: 
                l = mid +1;

       
        return -1;