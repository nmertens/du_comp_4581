# Divide and Conquer Distance Algorithm
# Last Updated: 1/23/2022

def cPairDist(points):
    points.sort()
    return recCPairDist(points)

def recCPairDist(points):
    if len(points) < 4:
        dist = []
        for i in range(len(points) - 1):
            dist.append(abs(points[i] - points[i+1]))
        return min(dist)
    else:
        # Divide
        mid = len(points)//2
        left = points[:mid]
        right = points[mid:]
        # Conquer & Combine
        mid_dist = abs(left[-1] - right[0])
        minimum = min([mid_dist, recCPairDist(left), recCPairDist(right)])
        return minimum

# Demo Lists
l1 = [7,4,12,14,2,10,16,6]
l2 = [7,4,12,14,2,10,16,5]
l3 = [14,8,2,6,3,10,12]

# Results of Demo
print(f'Minimum distance for l1: {cPairDist(l1)}')
print(f'Minimum distance for l2: {cPairDist(l2)}')
print(f'Minimum distance for l3: {cPairDist(l3)}')