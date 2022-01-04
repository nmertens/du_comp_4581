# Python version of Matrix Multiplication

def printMatrix(m):
    # iterate over rows
    for row in m:
        print(row)

def matrixMult(A, B):
    # check if matrices are compatiable
    if len(A[0]) == len(B):
        # initialize results matrix
        result = []
        # iterate over rows in A
        for i in range(len(A)): 
            rows = []
            # iterate over columns in B
            for j in range(len(B[0])): 
                columns = 0
                # iterate over values in each column of B
                for k in range(len(B)): 
                    columns += A[i][k] * B[k][j]
                rows.append(columns) 
            result.append(rows)
        return result
    else:
        # raise error if inner dimensions do not match
        raise ValueError(f'Number of columns in first matrix ({len(A[0])}) do not equal number of rows in second matrix ({len(B)})')

def main(A, B):
    print(matrixMult(A,B))

if __name__ == '__main__':
    main()