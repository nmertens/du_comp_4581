from time import time
import random

def merge(A, B):
    out = []
    i,j = 0,0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            out.append(A[i])
            i += 1
        else:
            out.append(B[j])
            j += 1
    while i < len(A):
        out.append(A[i])
        i += 1
    while j < len(B):
        out.append(B[j])
        j += 1
    return out

def mergeSort(L):
    if len(L) < 2:
        return L[:]
    else:
        mid = len(L)//2
        Left = mergeSort(L[:mid])
        Right = mergeSort(L[mid:])
        return merge(Left, Right)

def insertionSort(L):
    for i in range(len(L)):
        key = L[i]
        j = i-1
        while j >= 0 and L[j] > key:
            L[j+1] = L[j]
            j = j-1
        L[j+1] = key
    return L

def bubbleSort(L):
    # loop through list
    for i in range(len(L)):
        # loop to compare list elements
        for j in range(0, len(L) - i - 1):
            # compare two list elements
            if L[j] > L[j+1]:
                temp = L[j]
                L[j] = L[j+1]
                L[j+1] = temp
    return L

def main():

    # generate list of numbers to operate on
    L = [i for i in range(100, 5100, 100)]

    # print headers
    print(f'N\tMerge\tInsert\tBubble')
    
    # loop through list L
    for j in L:
        # generate and shuffle list
        numList = [i for i in range(j)]
        random.shuffle(numList)
        
        # merge method
        mergeT1 = time()
        mergeData = mergeSort(numList)
        mergeT2 = time()
        mergeTime = round((mergeT2 - mergeT1)*1000, 1)

        # insertion method
        insertionT1 = time()
        insertionData = insertionSort(numList)
        insertionT2 = time()
        insertionTime = round((insertionT2 - insertionT1)*1000, 1)

        # bubble method
        bubbleT1 = time()
        bubbleData = bubbleSort(numList)
        bubbleT2 = time()
        bubbleTime = round((bubbleT2 - bubbleT1)*1000, 1)

        # print results
        print(f'{j}\t{mergeTime}\t{insertionTime}\t{bubbleTime}')

if __name__ == '__main__':
    main()