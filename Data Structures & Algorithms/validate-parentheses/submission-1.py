class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ('(', '[', '{'):
                stack.append(c)
            else:
                if not stack: 
                    return False
                if c in (')', ']', '}'):
                    if stack[-1] == '(' and c == ')' or stack[-1] == '{' and c == '}'  or stack[-1] == '[' and c == ']':
                        stack.pop()
                    else:
                        return False
        return len(stack) == 0