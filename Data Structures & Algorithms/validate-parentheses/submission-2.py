class Solution:
    '''
    U:
        I: String
        O: Boolean
        C: 
        E:
    I: 
    '''
    def isValid(self, s: str) -> bool:
        # forgot to create stack
        stack = [];
        key = {
            ')':'(',
            ']':'[',
            '}':'{'
            }

        for elem in s:

            if(elem in key):
                if(stack and stack[-1] == key[elem]): # stack exist (elems in there) and first pos check == close
                    stack.pop();
                else:
                    return False;
            else: stack.append(elem);
        return True if not stack else False; 
            
        