# Dynamic Programming for Optimal Return on Investment
# Last updated: 3/10/2022

import csv

def loadInvestments():

    # initialize empty lists
    state = []
    cost = []
    value = []

    with open('./State_Zhvi_Summary_AllHomes.csv') as csvfile:
        readerObject = csv.reader(csvfile)
        next(readerObject) # get rid of the header
        next(readerObject) # get rid of the United States row
        for row in readerObject:
            state.append(row[2])
            cost.append(int(row[4]))
            # value = cost * 10 year estimate
            value.append(int((float(row[9])*(float(row[4]))))) 
    
    return state, cost, value


def optimizeInvestments(total, state, cost, value): 

    n=len(value)
    # initialize table
    table = [[0 for x in range(total + 1)] for x in range(n + 1)] 
 
    for i in range(n + 1): 
        for j in range(total + 1): 
            # fill in the base cases when they arise
            if i == 0 or j == 0: 
                table[i][j] = 0
            # check to see if this is the best value for cost
            elif cost[i-1] <= j: 
                table[i][j] = max(value[i-1] + table[i-1][j-cost[i-1]],  table[i-1][j]) 
            else: 
                table[i][j] = table[i-1][j] 
    
    result = table[n][total] 
    print(f'Optimal Return on Investment: {result}')
    print('States to Invest In:')

    # Traceback
    traceTotal = total
    for i in range(n, 0, -1):
        if result <= 0:
            break
        
        # If the total changes it means that the current row is included
        #   in the optimal solution
        if result == table[i-1][traceTotal]:
            continue
        else:
            # This item is included
            print(f'{state[i-1]} (Cost: {cost[i-1]}, Return: {value[i-1]})')
            # Since this cost is included deduct the value from the result
            result = result - value[i-1]
            # deduct the cost from the total
            traceTotal = traceTotal - cost[i-1]

state, cost, value = loadInvestments()
optimizeInvestments(1000000, state, cost, value)

################# Output #################
#                                        #
# Optimal Return on Investment: 49453    #
# States to Invest In:                   #
# Nevada (Cost: 293500, Return: 15434)   #
# Colorado (Cost: 380200, Return: 21764) #
# Tennessee (Cost: 167300, Return: 5724) #
# Michigan (Cost: 152000, Return: 6531)  #
#                                        #
##########################################