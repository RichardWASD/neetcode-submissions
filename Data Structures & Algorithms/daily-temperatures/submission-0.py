class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures) # [0,0,0,...0]
        stack = [] # pair : [temp,index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]: # stack isnt empty & (top stack: -1 ; index: 1st val in pair : 0)
                stackT, stackInd = stack.pop() # (temp, index)
                res[stackInd] = (i - stackInd)
            stack.append([t,i])
        return res