
################################################################################
#
def CyclicSeqFound(happySumList):

    print( happySumList)
    #iterate until first 4 is found
    #iterated for pattern "4,16,37,58,89,145,42,20,4"
    notHappyPattern=[4,16,37,58,89,145,42,20,4]
    startIndex = happySumList.index(4)          #find the first occurrance of 4
    if( (len(happySumList)-startIndex) >= len(notHappyPattern)):
        for num in notHappyPattern:
            print( num,happySumList[startIndex])
            if (num == happySumList[startIndex]):
                matching = True
            else:
                matching = False
                break
            startIndex+=1
            
    return matching


################################################################################
#
def main():

    happySumList=[4,4,37,58,89,145,42,20,4]
    found = CyclicSeqFound(happySumList)
    if (found == True):
        print ( 'cyclic found')
    else:
        print ( 'cyclic not found')


main()
