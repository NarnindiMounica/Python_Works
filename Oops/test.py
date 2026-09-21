import ctypes
class CustomList:
    def __init__(self):
        initial_capacity = 1
        self.capacity = initial_capacity
        self.size = 0

    def __create_array(self, capacity):
        return 2*capacity * (ctypes.py_object)()

    def __resize_array(self, new_capacity):
        return self.__create_array(new_capacity)

    def append(self, item):
        if self.size == self.capacity:
            self.array = self.__resize_array()