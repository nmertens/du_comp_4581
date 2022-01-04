# Python version of Matrix Multiplication

def printMatrix(m):
    for row in m:
        print(row)

def matrixMult(A, B):
    result = []
    if len(A[0]) == len(B):
        result = []
        for m in range(len(A)): 
            rows = []
            for i in range(len(B[0])): 
                columns = 0
                for j in range(len(B)): 
                    columns += A[m][j] * B[j][i]
                rows.append(columns) 
            result.append(rows)
        return result
    else:
        raise ValueError(f'Number of columns in first matrix ({len(A[0])}) do not equal number of rows in second matrix ({len(B)})')

def main(A, B):
    print(matrixMult(A,B))

if __name__ == '__main__':
    main()