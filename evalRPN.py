class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = []

        for c in tokens:
            if c == "+":
                result.append(result.pop() + result.pop())
            elif c == "-":
                a, b = result.pop(), result.pop()
                result.append(b - a)
            elif c == "*": 
                result.append(result.pop() * result.pop())
            elif c == "/": 
                a, b = result.pop(), result.pop()
                result.append(int(b/a))
            else:
                result.append(int(c))
            
        return result[-1]
            
        
