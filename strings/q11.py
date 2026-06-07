theStr=" This is a test "
inputStr=input("enter integer: ")
inputInt=int(inputStr)
testStr=theStr
while inputInt>=0:
    testStr=testStr[1:-1]
    inputInt=inputInt-1
testBool="t" in testStr
print(theStr)
print(testStr)
print(inputInt)
print(testBool)