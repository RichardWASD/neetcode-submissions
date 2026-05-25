class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # explain the datastruc
        freq = [[] for i in range(len(nums) + 1)] # Explain syntax

        for num in nums:
            count[num] = 1 + count.get(num,0) # explain count.get notation
        for num , cnt in count.items():
            freq[cnt].append(num)
        
        result = []
        for i in range(len(freq)-1 , 0 , -1): # Start, stop, increment by
            for num in freq[i]:
                result.append(num)
                if(len(result) == k):
                    return result
        