class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        U:
            I: list Int; int 
            O: List size k 
            C:
            E:
        I:
        variables: buckets : [] * len(k) + 1 
        1) Make hashmap elem: freq 
        2) filtering portion
        3) Formating the result
        Return res 
        '''

        count = {}
        freq = [[] for _ in range(len(nums)+1)]

        for i in range(len(nums)): #1 Counting the frequency of each elem in list
            count[nums[i]] = count.get(nums[i], 0) + 1
        
        for key,val in count.items(): #2 assign the elem to appropiate index that matches freq
            freq[val].append(key)

        res= []
        for i in range(len(freq) -1 , 0 , -1):# [[], [], [2] ,[4,3], []]

            for num in freq[i]:
                res.append(num)
                if(k == len(res)): 
                    return res
                
                
                
        
        return res

