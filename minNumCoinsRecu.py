def minNumCoins(M, c, d):
    # This algorithm will look up how many coins (of values present in the c array)
    # are needed to give the change back for M value
    #This alg is inefficient as it doesn't reuse the previously calculated values and 
    #instead calculates them from new everytime it needs one
    if(M <= 0):
        return 0
    lowestCoinCount = float('inf')
    for i in range(len(c)):
        if(M >= c[i]):
            newLowest = minNumCoins(M-c[i], c,len(c))
            if newLowest + 1 < lowestCoinCount:
                lowestCoinCount = newLowest + 1
    return lowestCoinCount



array = [1,3,5]

print(minNumCoins(100,array,len(array)))