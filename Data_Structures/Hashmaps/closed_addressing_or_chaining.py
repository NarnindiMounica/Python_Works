from linked_list_for_chaining import LLNode, LinkedList

class HashmapUsingChaining:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.buckets = self.__create_buckets(self.capacity)

    def __create_buckets(self):
        buckets = [LinkedList() for i in range(self.capacity)]
        return buckets

