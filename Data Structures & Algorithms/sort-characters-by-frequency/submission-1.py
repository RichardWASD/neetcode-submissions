class Solution:
    def frequencySort(self, s: str) -> str:
        '''
        U:
            I: String 
            O: String (Sorted in decreasing order BASED on Frequency)
            C:
            E:
        '''

        count = {} # char : count
        # -> convert this mapping to string 
        strs = [[] for _ in range(len(s)+1)] # index : length (string chars) ; Dont start the bucket with anything

        # 1) map the items 
        for i in range(len(s)):
            count[s[i]] = count.get(s[i] , 0 ) + 1
        
        # 2) Convert mapping to respected strings
        for i,freq in count.items(): # 95% of bugs here
            curr = ""
            strs[freq].append(i)
            # for j in range(len(s)): # shortcut : "e"*2
            #     curr += f"{i}"
            # strs[l].append(curr) # put in correct spot of the list (idx wise)

        res = []
        for i in range(len(strs) -1 , 0, -1):
            for c in strs[i]:
                res.append(c*i) # strings are immutable -> return new string -> store

        return "".join(res)

