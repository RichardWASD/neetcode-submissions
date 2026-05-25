class Solution:
    '''
    U:
        I: 2 strings
        O: bool
        C:
        E: different amount of letters
    '''
    def isAnagram(self, s: str, t: str) -> bool:
        Ls = len(s);
        Lt = len(t);
        if(not s or not t or Ls != Lt):
            return False;
        
        book1 = {};
        book2 = {};
        for i in range (Ls):
            book1[s[i]] = book1.get(s[i],0) + 1;
        
        for i in range(Lt):
            # if(t[i] not in book1):
            #     return False;
            # else:
                book2[t[i]] = book2.get(t[i],0) + 1;
            
        return True if book1 == book2 else False;
            