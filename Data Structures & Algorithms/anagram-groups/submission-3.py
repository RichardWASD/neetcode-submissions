class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ''' 
        U:
            I: list of strings
            O: grouped anagrams -> sublists 
            C:
            E: Empty string, single char
        I:
            For each word -> seen = 

        {
        {a:1, c:1,t:1} : [] ->  ["act"] -> ["act", "cat"]
        }
        '''

        res = defaultdict(list)

        for s in strs:
        # same length -> compare letters -> add
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)

        return list(res.values())