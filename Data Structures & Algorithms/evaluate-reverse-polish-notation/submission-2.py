class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        operations = ['+','-','*','/']
        total = 0
        for c in tokens:
            if c not in operations:
                stk.append(c)
            else:
                f = int(stk.pop())
                s = int(stk.pop())
                if c == '+':
                    total = s + f
                elif c == '-':
                    total = s-f
                elif c == '*':
                    total = s*f
                else:
                    total = s/f
                
                stk.append(total)
        
        return int(stk[-1])