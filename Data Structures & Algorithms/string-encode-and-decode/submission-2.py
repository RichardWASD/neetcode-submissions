class Solution:
    '''
    U:
        I: List of strings
        O: encoded-> format: string ; decoded list -> format: list of string
        C: any char in ascii 256
        E: empty list / string 
    '''
    def encode(self, strs: List[str]) -> str:
        # after each word add a delimiter to (what symbol should we use)= #
        # Delimiter= length of word then '#'
        res = "";
        for word in strs:
            count = len(word);
            res+= str(count);
            res += "#";
            res += word;
        return res;
        
    def decode(self, s: str) -> List[str]:
        # turn the string to list -> append until you find num followed by #
        '''
        Two pointers: 1st @ start of word, 2nd will continue until it encounters
        a number followed by a '#'

        We will add that res: word into the return list 

        While be repeated until no more words
        '''
        l = 0;
        result_list = [];
        while (l < len(s)):
            r = l;
            while (s[r] != '#'):
                r += 1;
            length = int(s[l:r]);
            l  = r + 1;
            r = l + length
            result_list.append(s[l:r])
            l=r
        return result_list;