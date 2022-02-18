import csv
from time import time

def getData(ticker):
    ticker = ticker
    date = []
    price = []

    with open('./nyse/prices-split-adjusted.csv') as csvfile:
        readerObject = csv.reader(csvfile)
        next(readerObject) # get rid of the header
        for row in readerObject:
            if row[1] == ticker:
                date.append(row[0]) # date
                price.append(float(row[3])) # closing price
    
    return ticker, date, price

    # change = [None for i in range(len(date))]

    # change[0] = 0
    # for i in range(1,len(price)):
    #     change[i] = float(price[i]) - float(price[i-1])
    
    # return date, price, change

def MSSDAC(A, low=0, high=None):
    if high == None:
        high = len(A) - 1

    # Base case
    if low == high:
        return(0, A[low], A[high])
        # if A[low] > 0: return A[low]
        # else: return 0
    # Divide
    mid = (low+high)//2
    # Conquer

    leftProfit , leftMin ,  leftMax = MSSDAC(A, low, mid)
    rightProfit, rightMin, rightMax = MSSDAC(A, mid+1, high)

    # maxLeft = MSSDAC(A, low, mid)
    # maxRight = MSSDAC(A, mid+1, high)

    maxProfit = max(leftProfit, rightProfit, rightMax - leftMin)
    return (maxProfit, min(leftMin, rightMin), max(leftMax, rightMax))

    # # Combine
    # maxLeft2Center = left2Center = 0
    # for i in range(mid, low-1, -1):
    #     left2Center += A[i]
    #     maxLeft2Center = max(left2Center, maxLeft2Center)
    # maxRight2Center = right2Center = 0
    # for i in range(mid + 1, high+1):
    #     right2Center += A[i]
    #     maxRight2Center = max(right2Center, maxRight2Center)
    # maxProfit = max(maxLeft, maxRight, maxLeft2Center+maxRight2Center)
    # # maxProfit = max(leftProfit, rightProfit, maxLeft2Center+maxRight2Center)
    # return maxProfit

date, price, change = getData('AAPL')

t1 = time()
profit, min, max = MSSDAC(price)
t2 = time()
print("Max Profit:",profit," in time: ",round((t2-t1)*1000,1),"ms")
print(date[price.index(min)])
print(date[price.index(max)])

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
#     return (maxProf, minPrice_id, maxPrice_i

# t1 = time()
# profit2, min, max = maxProfit(price)
# t2 = time()
# print("Max Profit:",profit2," in time: ",round((t2-t1)*1000,1),"ms")

# print(date[min], date[max])