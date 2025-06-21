class Solution:
    def isValid(self, s: str) -> bool:
        complement = {"(":")" , "[":"]", "{":"}"}
        stack = list()
        
        opening = set(complement.keys())
        
        for par in s:
            if par in opening:
                stack.append(complement[par])
            else:
                if not stack: # "]]]"
                    return False
                compl = stack.pop() 
                if par != compl:
                    return False
                else:
                    continue

        # all opening parens finished
        if stack:
            return False
            
        return True
