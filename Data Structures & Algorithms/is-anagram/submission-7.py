class Solution:
    '''
    U:
        I: two strings 
        O: boolean
        C:
        E:

    '''
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        if(len(s) == 0 and len(t) ==0):
            return True

        freqS= {}
        freqT= {}
        size = len(s)
        for i in range(size):
            # if(s[i] in freqS):
            #     freqS[s[i]] += 1
            # else:
            #     freqS[s[i]] = 1
             freqS[s[i]] = freqS.get(s[i], 0) + 1

        for i in range(size):
            # if(t[i] in freqT ):
            #     freqT[t[i]] += 1
            # else:
            #     freqT[t[i]] =1
            freqT[t[i]] = freqT.get(t[i], 0) + 1
            
        return freqT == freqS

        