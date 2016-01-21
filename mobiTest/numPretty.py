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


#This block outputs the appropriate output
if len(intNum) <= 6:
    print "Output" , intNum
else:
    if len(intNum) <= 9:

        sys.stdout.write(intNum[0:len(intNum) - 6])   #prints digits to the left of the decimal place
        if floatFlag == True:                         #if the number is a float, print the decimal place
            sys.stdout.write(".")
            if int(intNum[len(intNum) - 5]) >= 5:     #detects if rounding is necessary
                digit = int(intNum[len(intNum) - 6]) + 1 #rounds up by one
                sys.stdout.write(str(digit))
            else:
                sys.stdout.write(intNum[len(intNum) - 6]) #if rounding is not necesary, just print the digit
        sys.stdout.write("M")                             #prints regardless of int or float

    elif len(intNum) <= 12 and len(intNum) > 9:

        sys.stdout.write(intNum[0:len(intNum) - 9])
        if floatFlag == True:
            sys.stdout.write(".")
            if int(intNum[len(intNum) - 8]) >= 5:
                digit = int(intNum[len(intNum) - 9]) + 1
                sys.stdout.write(str(digit))
            else:
                sys.stdout.write(intNum[len(intNum) - 9])
        sys.stdout.write("B")


    elif len(intNum) <= 15 and len(intNum) > 12:

        sys.stdout.write(intNum[0:len(intNum) - 12])
        if floatFlag == True:
            sys.stdout.write(".")
            if int(intNum[len(intNum) - 11]) >= 5:
                digit = int(intNum[len(intNum) - 12]) + 1
                sys.stdout.write(str(digit))
            else:
                sys.stdout.write(intNum[len(intNum) - 12])
        sys.stdout.write("T")

    else:
        print "Number too large, please restart and enter a # in the trillions or less"

str = "12.56"
fl = float(str)
fl = round(fl, 1)
print fl
