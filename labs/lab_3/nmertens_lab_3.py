# RSA Encryption Exercise
# Last edited: 01/18/22
# Based on the trend line from the Excel curve fitter, the estimated time it would take to factor a 1024 bit number is:
#   milliseconds: ~ 3.00 x 10^301
#   years: ~ 9.51 x 10^290 

import os
import csv
import random
from time import time

def isPrime(p):
    ''' Checks if number is prime
    '''
    for i in range(2, int(p**(1/2))+1):
        if (p % i) == 0:
            return False
    return True

def nBitPrime(n):
    ''' Generates an n-bit number and checks if it is prime
    '''
    bit = 2**n # bit length
    integer = 0
    prime = False
    while prime == False:
        decimal = random.random()
        float_number = decimal * bit
        integer = round(float_number) # get round number
        if integer < 2: # check if less than 2
            next
        prime = isPrime(integer)
    return integer
    
    # Professor's code
    # while True:
    #     p = int(random.random() * (2**n))
    #     if p >= 2 and isPrime(p):
    #         return p


def factor(pq):
    ''' Factors a number generated from two n-bit prime numbers
    '''
    for i in range(2, pq):
        if (pq % i) == 0:
            p = i
            q = (pq/i)
            return p, q

def saveData(bits, times):
    ''' Saves data to csv file for use in curve fitter
    '''
    with open('nbit_times.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(zip(bits, times))

def main():
    ''' Time how long it takes to factor numbers of increasing bit size
    '''
    bits = [i for i in range(15,35,1)]
    times = []
    for bit in bits:
        t1 = time()
        pq = nBitPrime(bit) * nBitPrime(bit)
        p, q = factor(pq)
        t2 = time()
        totalTime = round((t2-t1)*1000, 1)
        times.append(totalTime)

    if not os.path.exists('nbit_times.csv'): # check if .csv file exists
        saveData(bits, times)

    return bits, times

if __name__ == '__main__':
    main()