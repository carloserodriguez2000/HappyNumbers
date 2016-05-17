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
def buildHappySqrArray(digitList):
    happyArray=list()
##    happyArray=[[1],[2],[3]]
    index=0
    listLength=len(digitList)
    #print(listLength)
    while ( index < listLength):
        digit = digitList[index]
        happyArray.append(int(digit)**2)
        index+=1
                                                ##    for digit in digitList:
                                                ##        happyArray.append(int(digit))
    #print ('built',happyArray)

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
    #print( happySumList)
    #iterate until first 4 is found
    #iterated for pattern "4,16,37,58,89,145,42,20,4"
   
    notHappyPattern=[4,16,37,58,89,145,42,20,4]
    if(notHappyPattern[0] in happySumList):
        startIndex = happySumList.index(4)          #find the first occurrance of 4
        if( (len(happySumList)-startIndex) >= len(notHappyPattern)):
            for num in notHappyPattern:
                #print( num,happySumList[startIndex])
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
    continueLoop    = True
    while (continueLoop == True):
        sLine = input( 'Enter a Number: ')
        if (checkValidNumber(sLine) == True):
            moreNums        = True
            while (moreNums == True) :
                digitList     = makeNumList( sLine)                      # list of separated digits
                happySquares  = buildHappySqrArray(digitList)        # List of squared digits
                sumOfSqr      = calcHappySum(happySquares)
                happySumList.append(sumOfSqr)    # Sum the squares and append to list
##                print( digitList)
##                print(happySquares)
##                print(sumOfSqr   )
##                print(happySumList)
                sLine         = sumOfSqr
                if(sumOfSqr == 1):
                    print('Happy found', happySumList)
                    moreNums = False
                else:
                    if( CyclicSeqFound(happySumList)== True):
                        print('NOT happy found', happySumList)
                        moreNums = False
                    
        happySumList.clear()
        continueLoop = (input("Press 1 to run again: ") == '1')
    else :
        print("Thank you for Playing.  Bye.")
         
################################################################################
#
################################################################################
main()
