class Solution:
    '''
    U:
        I: List of Strings 
        O: List of list of strings that are anagrams
        C: Lower case letters
        E: single letter
    I: loop through list 
            create a hashmap for each str ing 
    '''
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {};
        
        for i, s in enumerate(strs):

            curr_sorted = "".join(sorted(s));
            
            if(curr_sorted not in hmap):
                hmap[curr_sorted] = [s];
            else:
                hmap[curr_sorted].append(s);

        return list(hmap.values());


