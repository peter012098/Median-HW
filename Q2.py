class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        return self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


q = Queue()
print(q)
print(q.isEmpty())
q.enqueue('Melon')
q.enqueue(3323)
print(q.isEmpty())
print(q.size())
q.dequeue()
print(q.size())
