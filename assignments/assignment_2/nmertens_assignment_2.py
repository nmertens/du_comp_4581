# DAC Stock Problem; find the best stock to buy, when to buy it, when to sell it, and the profit
# Last updated: 2/18/2022
# For this version of the DAC I didn't end up using the change in price. However, I did check the processing time for this version the old DAC algorithm
# and the two were matched in terms of processing time.

import csv

def getData(ticker):
    ticker = ticker
    date   = []
    price  = []

    with open('./nyse/prices-split-adjusted.csv') as csvfile:
        readerObject = csv.reader(csvfile)
        next(readerObject) # get rid of the header
        for row in readerObject:
            if row[1] == ticker:
                date.append(row[0]) # date
                price.append(float(row[3])) # closing price
    
    return ticker, date, price

def getNames():

    stockNames = dict()

    with open('./nyse/securities.csv') as csvfile:
        readerObject = csv.reader(csvfile)
        next(readerObject)
        for row in readerObject:
            stockNames[row[0]] = row[1]
    
    return stockNames

def MSSDAC(A, low=0, high=None):
    if high == None:
        high = len(A) - 1
    # Base case: this will return the values needed to find when to buy and sell stock
    if low == high:
        return(0, A[low], A[high])
    # Divide
    mid = (low+high)//2
    # Conquer
    leftProfit , leftMin ,  leftMax = MSSDAC(A, low, mid)
    rightProfit, rightMin, rightMax = MSSDAC(A, mid+1, high)
    middleProfit = rightMax - leftMin
    # Combine
    maxProfit = max(leftProfit, rightProfit, middleProfit)
    return maxProfit, min(leftMin, rightMin), max(leftMax, rightMax)

def bestStock():
    stockNames = getNames()

    # initialize values
    bestProfit = 0
    bestTicker = None
    bestStart  = None
    bestEnd    = None

    # loop through the tickers
    for key in stockNames.keys():
        ticker, date, price = getData(key)
        if len(price) == 0:
            next
        else:
            profit, minVal, maxVal = MSSDAC(price)
            # if new bestProfit found update values
            if profit > bestProfit:
                bestProfit = profit
                bestTicker = ticker
                bestStart  = date[price.index(minVal)]
                bestEnd    = date[price.index(maxVal)]

    print(f'Best stock to buy: "{stockNames[bestTicker]}" on {bestStart} and sell on {bestEnd} with a profit of {bestProfit}')


# Initial test case
# ticker, date, price = getData('AAPL')
# profit, min, max = MSSDAC(price)
# print(profit)

bestStock()

## Dynamic Programing Version ##

# def maxProfit(prices):
#     if not prices:
#         return 0

#     maxProf = 0
#     minPrice = float(prices[0])
#     maxPrice = float(prices[0])

#     for i in range(1, len(prices)):
#         if float(prices[i]) < minPrice:
#             minPrice = float(prices[i])
#             minPrice_id = i
#         if float(price[i]) > maxPrice:
#             maxPrice = float(price[i])
#             maxPrice_id = i - 1
#         maxProf = max(maxProf, maxPrice - minPrice)
#     return (maxProf, minPrice_id, maxPrice_id)

# profitDP, minDP, maxDP = maxProfit(price)
# print("Max Profit: ",profitDP," in time: ",round((t2-t1)*1000,1),"ms")
# print(date[minDP], date[maxDP])

## Old DAC ###
# def MSSDAC(A, low=0, high=None):
#     if high == None:
#         high = len(A) - 1
#     # Base case
#     if low == high:
#         if A[low] > 0: return A[low]
#         else: return 0
#     # Divide
#     mid = (low+high)//2
#     # Conquer
#     maxLeft = MSSDAC(A, low, mid)
#     maxRight = MSSDAC(A, mid+1, high)
#     # Combine
#     maxLeft2Center = left2Center = 0
#     for i in range(mid, low-1, -1):
#         left2Center += A[i]
#         maxLeft2Center = max(left2Center, maxLeft2Center)
#     maxRight2Center = right2Center = 0
#     for i in range(mid + 1, high+1):
#         right2Center += A[i]
#         maxRight2Center = max(right2Center, maxRight2Center)
#     maxProfit = max(maxLeft, maxRight, maxLeft2Center+maxRight2Center)
#     return maxProfit