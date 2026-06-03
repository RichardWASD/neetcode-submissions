class Solution:
    '''
    U:
        I: List of Nums ; int K = 
        O: List of k elements (k most repeated)
        C:  K <= unique elems
        E: Negative numbers
    I: Loop through list and add freq hashmap
        return 
    '''

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {};
        freq = [[] for i in range(len(nums)+1)]; #

        for num in nums:
            count[num] = 1 + count.get(num,0); # adds all occurence in map
        
        for num, cnt in count.items():
            freq[cnt].append(num);

        res = [];
        for i in range(len(freq)-1, 0 ,-1):
            for num in freq[i]:
                res.append(num);
                if(len(res) == k):
                    return res;