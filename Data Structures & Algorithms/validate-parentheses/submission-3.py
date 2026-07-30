class Solution:
    '''
    U:
        I: A string of bracket type chars 
        O: Boolean 
        C: Strict requirement
        E: No Closing
    I:
    '''
    def isValid(self, s: str) -> bool:
        key  = {
            '}' : '{',
            ']' : '[',
            ')' : '('
        };
        stack = [];
        
        for c in s:

            if(c in key):

                if(stack and stack[-1] == key[c] ): # TODO
                    stack.pop();
                else:
                    return False;
            else:
                stack.append(c);
        return False if stack else True;