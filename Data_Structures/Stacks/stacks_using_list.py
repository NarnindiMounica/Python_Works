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


stacks_from_list = StacksFromList()

print(stacks_from_list.is_empty())
print(stacks_from_list.push(10))
print(stacks_from_list.push(20))
print(stacks_from_list.push(30))
print(stacks_from_list.size())
print(stacks_from_list.top())
print(stacks_from_list.pop())
print(stacks_from_list.is_empty())

           