from linked_list_for_chaining import LLNode, LinkedList

class HashmapUsingChaining:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.buckets = self.__create_buckets(self.capacity)

    def __create_buckets(self):
        buckets = [LinkedList() for _ in range(self.capacity)]
        return buckets

    def hash_function(self, key):
        return abs(hash(key)) % self.capacity


    def insert(self, key, value):
        bucket_index = self.hash_function(key)

