class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        U: 
            I: Two Strings
            O: Boolean
            C: Lower case letters
            E:
        '''

        if(len(s) != len(t)):
            return False

        mapS = {}
        mapT = {}
        for i in range(len(s)):
            mapS[s[i]] = mapS.get(s[i],0) +1 # If none then set to 0, else add 1.
            mapT[t[i]] = mapT.get(t[i],0) +1
        
        return mapS == mapT
        