class Queue(object):
    def __init__(self, size):
        self.queue = []
        self.size = size

    def __str__(self):
        myString = ' '.join(str(i) for i in self.queue)
        return myString

    def enqueue(self, item):
        ''' Add item to the end of the queue 
        '''
        if(self.isFull() != True):
            self.queue.insert(0, item)
        else:
            print('Queue is Full!')

    def dequeue(self):
        ''' Remove an item from the start of the queue 
        '''
        if(self.isEmpty() != True):
            return self.queue.pop()
        else:
            print('Queue is Empty!')

    def isEmpty(self):
        ''' Check if the queue is empty 
        '''
        return self.queue == []

    def isFull(self):
        ''' Check if the queue is full 
        '''
        return len(self.queue) == self.size

    def check(self):
        ''' See the first element at the start of the queue 
        '''
        if(self.isEmpty() != True):
            return self.queue[-1]
        else:
            print('Queue is Empty!')