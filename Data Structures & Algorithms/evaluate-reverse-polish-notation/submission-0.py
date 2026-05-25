class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in range (len(tokens)):
            if (tokens[i] == "+"):
                stack.append(int(stack.pop() + stack.pop()))
            elif (tokens[i] == "-"):
                a,b = stack.pop() , stack.pop() # 1st pop = greater# ,2nd pop = less
                stack.append(int(b-a))
            elif (tokens[i] == "/"):
                a,b  = stack.pop() , stack.pop()
                stack.append(int(float(b)/a))
            elif (tokens[i] == "*"):
                stack.append(int(stack.pop() * stack.pop()))
            else:
                stack.append(int(tokens[i]))
        return stack[0]