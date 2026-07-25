class StacksFromList:

    def __init__(self):
        self.__stack = []

    def push(self, data):
        self.__stack.append(data) 
        return self.__stack

    def is_empty(self):
        return len(self.__stack)==0

    def size(self):
        return len(self.__stack)

    def top(self):
        if len(self.__stack)==0:
            print("Empty Stack")
            return None
        return self.__stack[-1]

    def pop(self):
        if len(self.__stack)==0:
            print("Empty Stack")
            return None
        print(self.__stack.pop())
        return self.__stack


stacks_from_list = StacksFromList()

print(stacks_from_list.is_empty())
print(stacks_from_list.push(10))
print(stacks_from_list.push(20))
print(stacks_from_list.push(30))
print(stacks_from_list.size())
print(stacks_from_list.top())
print(stacks_from_list.pop())
print(stacks_from_list.is_empty())

#using list inbuilt operation
#print(stacks_from_list.stack.insert(0,19))
print(stacks_from_list.pop())

#we are making stack variable a private variable so that users cannot use inbuilt list operations on it.



           