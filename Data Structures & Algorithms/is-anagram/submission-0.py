class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sLen = len(s)
        tLen = len(t)
        if(sLen != tLen): 
            return False

        countS, countT = {},{}

        for i in range(0,sLen):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT