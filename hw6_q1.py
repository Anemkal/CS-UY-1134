class LinkedQueue:
    def __init__(self):
        self.head = None  
        self.tail = None
        self.n = 0

    def __len__(self):
        return self.n

    def is_empty(self):
        return self.n == 0

    def enqueue(self, elem):
        new_node = {'data': elem, 'next': None}
        if self.is_empty():
            self.head = new_node
        else:
            self.tail['next'] = new_node
        self.tail = new_node
        self.n += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        result = self.head['data']
        self.head = self.head['next']
        self.n -= 1
        if self.is_empty():
            self.tail = None
        return result

    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.head['data']
