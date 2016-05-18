################################################################################
#
def checkValidNumber( sLine):
    if( sLine.isnumeric()):
        return True
    else:
        return False
    
################################################################################
#
def makeNumList( sLine ):
    stringInteger = str(sLine)
    digitList = list()
    for ch in stringInteger:
        digitList.append(ch)
    return digitList

################################################################################
#
#    for digit in digitList:
#        happyArray.append(int(digit))
def buildHappySqrArray(digitList):
    happyArray=list()
    index=0
    listLength=len(digitList)
    while ( index < listLength):
        digit = digitList[index]
        happyArray.append(int(digit)**2)
        index+=1
    return happyArray

################################################################################
#
def calcHappySum( happySquareList):
    sumSqr = 0
    for num in happySquareList:
        sumSqr+=num
    return sumSqr

################################################################################
#
def checkValidHappy(happyArray):
    return True

################################################################################
#
def CyclicSeqFound(happySumList):
    notHappyPattern=[4,16,37,58,89,145,42,20,4]
    if(notHappyPattern[0] in happySumList):
        startIndex = happySumList.index(4)          #find the first occurrance of 4
        if( (len(happySumList)-startIndex) >= len(notHappyPattern)):
            for num in notHappyPattern:
                if (num == happySumList[startIndex]):
                    matching = True
                else:
                    matching = False
                    break
                startIndex+=1
        else:  matching = False
    else:
         matching = False
  
    return matching
                        
################################################################################
#
def main ():
    happySumList    = list()
    moreNums        = True
    index           = 0
    while (index <=10000):
        sLine = str(index)
        moreNums        = True
        while (moreNums == True) :
            digitList     = makeNumList( sLine)                 # list of separated digits
            happySquares  = buildHappySqrArray(digitList)        # List of squared digits
            sumOfSqr      = calcHappySum(happySquares)
            happySumList.append(sumOfSqr)    # Sum the squares and append to list
            sLine         = sumOfSqr
            ##print(happySumList)
            if(sumOfSqr == 1):
                print('Number:',index, 'is HAPPY!', happySumList)
                moreNums = False
            else:
                if( (CyclicSeqFound(happySumList)== True) or (sumOfSqr==0)):
                    print('Number:',index, 'is NOT happy', happySumList)
                    moreNums = False
        index+=1
        happySumList.clear()
     
################################################################################
#
################################################################################
main()
