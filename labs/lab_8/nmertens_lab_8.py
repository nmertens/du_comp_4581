# DP Chain Multiplication
# Last edited: 02/21/2022

def printMatrix(m): 
    for row in m:
        print(row)

def chainMatrix(dims):
    # Create the empty 2-D table
    n = len(dims)-1
    m = [[None for i in range(n)] for j in range(n)]
    t = [[None for i in range(n)] for j in range(n)]

    # Fill in the base case values
    for i in range(n):
        m[i][i] = 0
        t[i][i] = i

    # Fill in the rest of the table diagonal by diagonal
    for chainLength in range(2,n+1): 
        for i in range(n+1-chainLength):
            j = i + chainLength - 1
            # Fill in m[i][j] with the best of the recursive options
            m[i][j] = float("inf") 
            for k in range(i,j):
                # Two previous table values plus
                # what it cost to mult the resulting matrices
                q = m[i][k]+m[k+1][j]+dims[i]*dims[k+1]*dims[j+1] 
                if q < m[i][j]:
                    m[i][j] = q
                    t[i][j] = k
    printMatrix(m) 
    parenStr(t, 0, n-1)

    return m[0][n-1]

def parenStr(traceback, i, j):
    # Base case
    if i == j:
        print(f'(A{i})', end = '')
        return
    
    # table index for parenthesis placement
    k = traceback[i][j]

    # Get the optimal breakdown based on traceback table
    print('(', end = '')
    parenStr(traceback, i, k)
    parenStr(traceback, k + 1, j)
    print(')', end = '')

dims = [30,35,15,5,10,20,25] 
result = chainMatrix(dims)
print(f'\n Optimal number of multiplications: {result}')