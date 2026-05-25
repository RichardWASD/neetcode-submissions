class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,1
        longestSub = 1
        currSub = 1
        seen = set() # O(n) clear and space

        if(len(s) == 0):
            return 0

        while(r < len(s)):

            if(s[l] not in seen):
                seen.add(s[l])
            if(s[r] not in seen):
                seen.add(s[r])
                currSub += 1
                r +=1
                longestSub = max(longestSub, currSub)
            else:
                longestSub = max(longestSub, currSub)
                currSub = 1 
                l += 1
                r = l + 1
                seen.clear()
        return longestSub

