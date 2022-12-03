from EmptyQueueError import EmptyQueueError
class Queue:
    'a classic queue class'
    def __init__ (self): 
        'instantiates an empty list'
        self.q = []
    def isEmpty(self):
        'returns True if queue is empty, False otherwise'
        return (len(self.q) == 0)
    def enqueue (self, item):
        'insert item at rear of queue'
        return self.q.append(item)
    def dequeue(self):
        'remove and return item at front of queue'
        if self.isEmpty():
            raise EmptyQueueError("dequeue from empty queue")
        return self.q.pop(0)
    def __str__(self) -> str:
        'returns a string representation of the queue'
        return str(self.q)