class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b)
        }
        stk = []
        for c in tokens:
            if c in ops:
                b = stk.pop()
                a = stk.pop()
                stk.append(ops[c](a,b))
            else:
                stk.append(int(c))
        return stk[0]