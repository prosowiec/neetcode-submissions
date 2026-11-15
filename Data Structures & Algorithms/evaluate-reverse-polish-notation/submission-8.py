class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0
        elif len(tokens) == 1:
            return int(tokens.pop())

        res = 0
        tokens_stack = []
        for e in tokens:
            if e == "+":
                res = tokens_stack.pop() + tokens_stack.pop()
                tokens_stack.append(res)
            elif e == "-":
                first = tokens_stack.pop()
                last = tokens_stack.pop()
                res = last - first
                tokens_stack.append(res)

            elif e == "*":
                res = tokens_stack.pop() * tokens_stack.pop()
                tokens_stack.append(res)

            elif e == "/":
                first = tokens_stack.pop()
                last = tokens_stack.pop()
                res = int(last / first)
                tokens_stack.append(res)

            else:
                tokens_stack.append(int(e))
            
            #print(tokens_stack)
        return int(res)