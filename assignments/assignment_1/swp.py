# Breadth First Search for Small World Problem
# Last edited: 1/28/2022

from collections import defaultdict, Counter, OrderedDict

def loadGraph(edgeFilename):
    ''' Load in edge data and sort into adjacency list
    '''
    with open(edgeFilename) as f:
        lines = f.read().strip().split("\n")

    adjacencyList = defaultdict(list)

    for line in lines:
        ls = line.split(" ")
        # Make sure to append the pair both ways (ex. 15 to 33 & 33 to 15)
        adjacencyList[ls[0]].append(ls[1])
        adjacencyList[ls[1]].append(ls[0]) 
    
    return adjacencyList

class MyQueue(object):
    def __init__(self):
        ''' initialize an empty queue object
        '''
        self.queue = []

    def __str__(self):
        myString = ' '.join(str(i) for i in self.queue)
        return myString

    def enqueue(self, item):
        ''' Add item to the end of the queue 
        '''
        self.queue.insert(0, item)

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

    def checkFirst(self):
        ''' See the first element at the start of the queue 
        '''
        if(self.isEmpty() != True):
            return self.queue[-1]
        else:
            print('Queue is Empty!')

def BFS(G, s):
    ''' Breadth-First Search algorithm
    '''
    visited = {}
    for key in G.keys():
        visited[key] = float('inf')
    
    queue = MyQueue()
    
    distance = 0
    visited[s] = 0
    
    queue.enqueue(s)
    while not queue.isEmpty():
        s = queue.dequeue()
        distance = visited[s]
        for neighbour in G[s]:
            if visited[neighbour] == float('inf'):
                queue.enqueue(neighbour)
                visited[neighbour] = int(distance + 1)
    
    return visited

def distanceDistribution(G):
    ''' Get the overall distribution of distances between vertices
    '''
    frequencies = defaultdict(list)
    
    for key in G.keys():
        visitedDict = BFS(G, key)
        visitedCounts = Counter(visitedDict.values())
        for number in visitedCounts.keys():
            if (number != float('inf')) and (number != 0):
                frequencies[number].append(visitedCounts[number])
    
    summed = {k: sum(v) for (k, v) in frequencies.items()}
    total = sum(summed.values())
    percentages = {k: round((v/total)*100, 1) for (k,v) in summed.items()}
    
    return percentages


# Test case
adjacencyList = loadGraph('edges.txt')
test = distanceDistribution(adjacencyList)
test2 = dict(OrderedDict(sorted(test.items())))
for key, value in test2.items():
    print(key, value)

##### Comment Section #####
# To what extent does this network satisfy the small world phenomenon?
# The network created here statifies the small world problem since most of connections between nodes are at 6 or below.
# To be more specific, 98% of all the distances in the sample Facebook data were at or below 6 edges away from any starting node. 
# Clearly, 98% is not 100%, but it is very, very close. Therefore, this network satisfies the small world phenomenon.