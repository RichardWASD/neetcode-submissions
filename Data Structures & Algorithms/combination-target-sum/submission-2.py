class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        '''
        DFS is used to go down the possiblity tree
        Then append if the target is satisfied

        '''
        def dfs(i, curr, total):

            # if(curr == None): # Not needed
            #     return
            if(total == target):
                res.append(curr.copy())
                return
            #Need to check ranges 
            if(total > target or i >= len(nums)):
                return
            # append ,call updated dfs poplast, ****
            curr.append(nums[i])
            dfs(i,curr, total+nums[i])
            curr.pop();
            dfs(i+1, curr, total) # passed total
        

        
    
        dfs(0,[],0)
        return res
        
        