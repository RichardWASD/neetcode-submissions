class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")" : "(", "}" : "{", "]" :"["} # key : value -> Maps closing to the coresponding closing

        for i in range (len(s)):
            if(s[i] in closeToOpen):
                if(stack and stack[-1] == closeToOpen[s[i]]): # If stack isnt empty and TOP of stack == (coresponding key)
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
        return True if not stack else False
