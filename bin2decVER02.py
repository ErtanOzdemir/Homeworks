def binaryToDecimal(binary):

    binaryString=str(binary)
    binaryString=binaryString[::-1]


    decimalValue=0
    counter=0

    binaryNum=len(binaryString)
    

    while binaryNum>0:
        if binaryString[counter:counter+1] == "1":
            decimalValue=decimalValue+(2**counter)
            counter=counter+1
            binaryNum=binaryNum-1
        else:
            counter=counter+1
            binaryNum=binaryNum-1
    print(decimalValue)
            
            
        
        
