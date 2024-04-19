class Solution:
    def calculate(self, s: str) -> int:
        def evaluate(x, y, op):
            if op == '+':
                return x
            if op == "-":
                return -x
            if op == "*":
                return x * y
            return int(x/y)
        stack = []
        curr = 0
        prev_op = "+"
        s+="@"
        for c in s:
            if c.isdigit():
                curr = curr *10 + int(c)
            elif c == "(":
                stack.append(prev_op)
                prev_op ="+"
            else:
                if prev_op in "*/":
                    stack.append(evaluate(stack.pop(), curr,prev_op))
                else:
                    #last one 
                    stack.append(evaluate(curr, 0, prev_op))
                curr = 0
                prev_op = c
                if c == ")":
                    while type(stack[-1]) == int:
                        curr += stack.pop()
                    prev_op = stack.pop()
        return sum(stack)
