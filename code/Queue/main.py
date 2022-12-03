from Queue import Queue
# initialize a queue
q = Queue()
# enqueue some items
q.enqueue("apple")
q.enqueue("banana")
q.enqueue("cherry")
# print the queue
print(q)
# dequeue some items
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
# print the queue (should be empty)
print(q)
# try to dequeue from an empty queue (should raise an exception)
print (q.dequeue())

