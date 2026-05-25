class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #default deals with edge case
        for s in strs:
            count = [0] * 26 # array of 26 0's 
            for c in s: 
                count[ord(c) - ord('a')] += 1 # asci value 
            res[tuple(count)].append(s) #python stuff -> makes non mutable
        return list(res.values())