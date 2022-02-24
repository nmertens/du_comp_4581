# Dynamic Programing NCoins example
# Last edited: 2/14/2022

from time import time

# Algorithm 1: Divide-and-Conquer
def DACcoins(coins, amount):
    if amount == 0: # The base case
        return 0
    else: # The recursive case
        minCoins = float("inf") 
    for currentCoin in coins: #Check all coins
        # If we can give change
        if (amount - currentCoin) >= 0:
        # Calculate the optimal for currentCoin
            currentMin = DACcoins(coins, amount-currentCoin) + 1
            # Keep the best
            minCoins   = min(minCoins, currentMin) 

    return minCoins

# Algorithm 2: Dynamic Programming with Traceback
def DPcoins(coins, amount):
    # Create the intial tables
    numCoins = [None for i in range(amount + 1)]
    topCoin  = [None for i in range(amount + 1)]

    # Fill in the base case(s)
    numCoins[0] = 0
    topCoin[0]  = 0

    # Fill in the rest of the table
    for change in range(1, amount+1):

        numCoins[change] = change # worst case is all pennies
        topCoin[change]  = change

        # only include coins that are less that total change
        for coin in [c for c in coins if c <= numCoins[change]]: 
            if numCoins[change-coin] + 1 < numCoins[change]:
               numCoins[change] = numCoins[change-coin] + 1
               topCoin[change]  = coin

    # Perform the traceback to print result
    for i in range(numCoins[amount]):
        if i == 0:
            print(topCoin[amount])
            nextIndex = amount - topCoin[amount]
        else:
            print(topCoin[nextIndex])
            nextIndex = nextIndex - topCoin[nextIndex]

    # Professor's code
    # i = amount
    # while i != 0:
    #     print(topCoin[i])
    #     i = i - topCoin[i]

    return numCoins[amount]


C = [1, 5 , 10, 12, 25] # coin denominations (must include a penny)
A = int(input('Enter desired amount of change: '))
assert A >= 0

print("DAC:")
t1 = time()
numCoins = DACcoins(C,A)
t2 = time()
print("optimal:",numCoins," in time: ",round((t2-t1)*1000,1),"ms")

print()
print("DP:")
t1 = time()
numCoins = DPcoins(C,A)
t2 = time()
print("optimal:",numCoins," in time: ",round((t2-t1)*1000,1),"ms")