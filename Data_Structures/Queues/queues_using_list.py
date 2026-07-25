class QueueFromList:
    def __init__(self):
        self._queue = []

    def enqueue(self, value):
        self._queue.append(value)
        return f"{value} enqueued in queue"

    def is_empty(self):
        return len(self._queue)==0  

    def get_size(self):
        return len(self._queue)

    def front(self):
        if self.get_size == 0:
            return "Queue is empty, cannot return front"
        return self._queue[0]

    def dequeue(self):
        if self.get_size == 0:
            return "Queue is empty, cannot dequeue from it"
        return self._queue.pop(0)

queue_from_list = QueueFromList()

print(queue_from_list.is_empty())
print(queue_from_list.enqueue(2))
print(queue_from_list.enqueue(3))
print(queue_from_list.get_size())
print(queue_from_list.dequeue())
print(queue_from_list.front())