class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l,r = 0, 1 ; # i , j

        while(l<r and r < len(nums)):

            # if(nums[l] == nums[r]):
            #     if(abs(l-r) <= k): # THIS IS THE RANGE OF WINDOW
            #         return True;
            #     else:
            #         return False;
            if(abs(l-r) <= k):
                for i in range(l,r):
                    if(nums[i] == nums[r]):
                        return True;
                
            if(abs(l-r) == k):
                l += 1;
                r+=1;
            else :
                r+=1;
        return False
            