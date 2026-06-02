class Solution:
    '''
    U:
        I: List of strings
        O: List of List of strings -> anagrams
        C: lower case letters
        E: One word/ no word ""
    '''
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hmap = {};
        for i, s in enumerate(strs):

            curr_sorted = "".join(sorted(s));

            if(curr_sorted in hmap):
                hmap[curr_sorted] += [s];
            else:
                hmap[curr_sorted] = [s]
        return list(hmap.values());
