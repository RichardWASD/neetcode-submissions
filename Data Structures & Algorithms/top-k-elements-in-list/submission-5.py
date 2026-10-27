class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        U:
            I: int list
            O: list of elems (size k )
            C:
            E:
        I: 
            1) map int:freq
            2) put ints in buckets (index corresponding with freq)
            3) go through array of buckets from n->1
        '''

        count = {} # map for freq
        bucket = [[] for i in range(len(nums)+1)]

        for i in range(len(nums)): #1 
            count[nums[i]] = count.get(nums[i] , 0) + 1
        
        for num,freq in count.items():# elem : count
            bucket[freq].append(num) # at each index -> appened num that appears index times.

        res = []
        for i in range(len(bucket) -1 , 0 , -1):
            for num in bucket[i]:
                if(len(res) == k):
                    return res
                res.append(num)
            # if(len(res) == k):
            #     return res
        return res
