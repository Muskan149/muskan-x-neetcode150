class MinStack:
    def __init__(self):
        self.minStack = []
        self.minElem = []

    def push(self, val: int) -> None:          
        self.minStack.append(val)

        if self.minElem:
            if val < self.minElem[-1]:
                self.minElem.append(val)
            else: 
                self.minElem.append(self.minElem[-1])
        else:
            self.minElem.append(val)
        return

    def pop(self) -> None:
        self.minElem.pop()
        return self.minStack.pop()
        

    def top(self) -> int:
        return self.minStack[-1]
        
    def getMin(self) -> int:
        return self.minElem[-1]
