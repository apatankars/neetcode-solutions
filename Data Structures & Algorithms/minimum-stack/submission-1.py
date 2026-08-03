class MinStack:

    def __init__(self):
        self.vals = []
        self.mins = []
        

    def push(self, val: int) -> None:
        self.vals.append(val)

        if self.mins:
            if val <= self.mins[-1]:
                self.mins.append(val)
        else:
            self.mins.append(val)
        
    def pop(self) -> None:
        val = self.vals.pop()

        if val == self.mins[-1]:
            self.mins.pop()

    def top(self) -> int:
        return self.vals[-1]
        

    def getMin(self) -> int:
        return self.mins[-1]
        
