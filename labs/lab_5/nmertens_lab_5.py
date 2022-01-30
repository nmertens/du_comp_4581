from collections import deque

class MyStack():
    def __init__(self):
        ''' initialize an empty stack object
        '''
        self.elements = []

    def __str__(self):
        stackString = ' '.join(str(i) for i in self.elements)
        return stackString

    def push(self, item):
        ''' add an element to the stack
        '''
        self.elements.append(item)

    def pop(self):
        ''' remove an element from the stack
        '''
        if self.empty():
            print('Error: Popping from an empty stack!')
            # raise Exception("Cannot pop from an empty stack!")
        else:
            return self.elements.pop()
    
    def empty(self):
        ''' check if the stack is empty
        '''
        return self.elements == []
    
    def top(self):
        ''' look at the top of the stack
        '''
        if self.empty():
            print('Error: Stack is empty!')
            # raise Exception("No value: empty stack!")
        return self.elements[0]

class MyQueue():
    def __init__(self):
        ''' initialize an empty queue object
        '''
        self.queue = deque()

    def __str__(self):
        queueString = ' '.join(str(i) for i in self.queue)
        return queueString

    def enqueue(self, item):
        ''' Add item to the end of the queue 
        '''
        self.queue.insert(0, item)

    def dequeue(self):
        ''' Remove an item from the start of the queue 
        '''
        if(self.empty() != True):
            return self.queue.pop()
        else:
            print('Error: Queue is empty!')
            # raise Exception('Error: Queue is empty!')

    def empty(self):
        ''' Check if the queue is empty 
        '''
        return len(self.queue) == 0

    def front(self):
        ''' See the first element at the start of the queue 
        '''
        if(self.empty() != True):
            return self.queue[-1]
        else:
            print('Error: Queue is empty!')
            # raise Exception('Error: Queue is empty!')

# Testing code for stack
s = MyStack()
print(s.empty())
s.push(5)
s.push(8)
print(s.pop())
s.push(3)
print(s.empty())
print(s.top())
print(s.pop())
print(s.pop())
print(s.pop()) # should generate an error

# Testing code for Queue
q = MyQueue()
print(q.empty())
q.enqueue(5)
q.enqueue(8)
print(q.dequeue())
q.enqueue(3)
print(q.empty())
print(q.front())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue()) # should generate an error