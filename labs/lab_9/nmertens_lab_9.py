# Prim's MST Alogrithm
# Last updated: 3/1/2022

def extractMin(key, processed):

    # initialize min value to be infinity
    min = float("inf")

    for v in range(len(processed)):
        # only look at nodes that aren't processed
        if key[v] < min and processed[v] == False:
            min = key[v]
            min_index = v

    return min_index

def mst(g):

    nVerts = len(g) # number of vertices

    key = [float("inf") for i in range(nVerts)] # array to store minimum weight
    parent = [None for i in range(nVerts)]  # array to store parent nodes
    processed = [False for i in range(nVerts)] # array to indicate what's been processed

    # Set the root node and parent
    key[0] = 0
    parent[0] = -1

    for i in range(nVerts):

        # find the vertex with minimum distance vertex
        u = extractMin(key, processed)

        # once processed update status
        processed[u] = True

        for v in range(nVerts):
            # only look at nodes that are adjacent and have not been processed
            if g[u][v] > 0 and processed[v] == False:
                # update key and parent if current weight is less than the value
                if g[u][v] < key[v]:
                    key[v] = g[u][v]
                    parent[v] = u

    # put everything together and return the output
    output = []
    for j in range(nVerts): 
        output.append([j, parent[j]])
    
    return output

# Adjacency matrix representation of a graph
# This particular graph is the one from the videos 
# The vertices didn't have labels in the videos
# so I'm using the following vertex labels: 
#   2
#  / \
# 3---1--7
# |\  |
# 4 | 0--6
#  \|/
#   5

graph = [[0, 7, 0, 0, 0, 10, 15, 0],
         [7, 0, 12, 5, 0, 0, 0, 9], 
         [0, 12, 0, 6, 0, 0, 0, 0], 
         [0, 5, 6, 0, 14, 8, 0, 0], 
         [0, 0, 0, 14, 0, 3, 0, 0], 
         [10, 0, 0, 8, 3, 0, 0, 0], 
         [15, 0, 0, 0, 0, 0, 0, 0], 
         [0, 9, 0, 0, 0, 0, 0, 0]]

print(mst(graph))