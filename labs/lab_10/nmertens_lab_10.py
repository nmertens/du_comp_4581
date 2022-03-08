# Stack ADT with list implementation from Lab 5
class MyStack(object):
    def __init__ (self, type): # Creates an empty list
        self.elemType = type
        self.nodes = [] # Empty list 
        
    def __str__ (self): # for print
        return str(self.nodes)

    def empty(self):
        return len(self.nodes) == 0

    def push(self, elem): # Adds an element to the top of a stack
        self.nodes.append(elem)

    def pop(self): # Removes an element from the top of the stack
        if self.empty():
            raise ValueError("Requested top of an empty stack")
        else:
            return self.nodes.pop()
    
    def top(self): # Returns the top of a nonempty stack    
        if self.empty():
            raise ValueError("Requested top of an empty stack") 
        else:
            return self.nodes[-1]

def graphColoring(graph, colors):
# Each state will include only the colors that have been tried so far

    # get the length of the adjacency matrix
    n = len(graph)

    initialColoring = [] # Initial empty state
    # initialColoring = [None for i in range(n)]
    s = MyStack(list) # For a depth first search 
    s.push(initialColoring) # Push the initial state onto the Stack

    # While we still have states to explore
    while not s.empty():
        currentColoring = s.pop() # Grab the next coloring 
        currentVertex = len(currentColoring)
        # See if we found a solved state at a leaf node
        # That is, we have colored every node
        if currentVertex == n:
        # if None not in currentColoring:
            print(currentColoring) # Display the solution
            break
        else:
            for colorIndex in range(len(colors)):
                currentColor = colors[colorIndex]
                feasible = True
                for adjVertex in range(currentVertex, -1, -1):
                    if (graph[adjVertex][currentVertex]):
                        # print(adjVertex, currentVertex, currentColor, currentColoring)
                        if currentColoring[adjVertex] == currentColor:
                            feasible = False
                            break
    
                if feasible:
                    childColoring = currentColoring.copy()
                    childColoring.append(currentColor)
                    s.push(childColoring)

# Adjacency matrix representation of a graph
# This particular graph is the one from the videos
graph = [[False, True, False, False, False, True ], 
         [True, False, True, False, False, True ], 
         [False, True, False, True, True, False], 
         [False, False, True, False, True, False], 
         [False, False, True, True, False, True ], 
         [True, True, False, False, True, False]]
colors = ['r', 'g', 'b']
graphColoring(graph, colors)
