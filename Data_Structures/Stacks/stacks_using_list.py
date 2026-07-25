class StacksFromList:

    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data) 
        return self.stack

    def is_empty(self):
        return len(self.stack)==0

    def size(self):
        return len(self.stack)

    def top(self):
        return self.stack[-1]

    def pop(self):
        print(self.stack.pop())
        return self.stack


    
           