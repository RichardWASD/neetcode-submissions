class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        U: Returning a list of K elements (appear most in nums)
            I: list nums ; int k 
            O: list of k most freq elem
            C:
            E:
        '''
        res = []
        freqList = [[] for i in range(len(nums)+1)]
        freqMap = {}
        for i in range(len(nums)):
            freqMap[nums[i]] = freqMap.get(nums[i], 0) + 1

        # go through the freqMap -> determine the largest values of the keys -> those keys get added
        for num,cnt in freqMap.items(): # Read more
            freqList[cnt].append(num)

        for i in range(len(freqList) -1, 0 , -1):
            for num in freqList[i]:
                res.append(num)
                if(len(res) == k):
                    return res
         

