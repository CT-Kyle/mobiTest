import sys
#This program will take numbers and make them look all pretty


#This block accepts any input as raw input and stores as a string. It is stored as a string so that
#it can be sliced later for output.
print "********** Welcome to the Number Prettifier **********"
rawNum = raw_input('Enter a numerical value in the trillions or less: ')
print "Input" , rawNum

#This block will remove digits after the decimal from the string and set floatFlag = true
#This is done so that the len() method works correctly and to get output with a decimal place for float input


if "." in rawNum:
    intNum = rawNum[0:rawNum.find(".")]
    floatFlag = True
    print "Initial: ", intNum
else:
    floatFlag = False
    intNum = rawNum
if not intNum.isdigit():
    print "You inputed a non int or float. Please restart and input an int or float."


#This block prints the appropriate output
if len(intNum) <= 6:
    print "Output" , intNum
else:
    if len(intNum) <= 9:
        if floatFlag == True:
            #slices string to get appropriate value
            finalNum = intNum[0:len(intNum) - 6] + "." + intNum[len(intNum) - 6:len(intNum) - 4]
            print (str(round(float(finalNum), 1))) + "M" #converts str to float, rounds, and converts back to str
        else:
            print intNum[0:len(intNum) - 6] + "M" #simple print if it is not a float

    elif len(intNum) <= 12 and len(intNum) > 9:
        if floatFlag == True:
            finalNum = intNum[0:len(intNum) - 9] + "." + intNum[len(intNum) - 9:len(intNum) - 7]
            print (str(round(float(finalNum), 1))) + "B"
        else:
            print intNum[0:len(intNum) - 9] + "B"

    elif len(intNum) <= 15 and len(intNum) > 12:
        if floatFlag == True:
            finalNum = intNum[0:len(intNum) - 12] + "." + intNum[len(intNum) - 12:len(intNum) - 12]
            print (str(round(float(finalNum), 1))) + "T"
        else:
            print intNum[0:len(intNum) - 12] + "T"

    else:
        print "Number too large, please restart and enter a # in the trillions or less"

