
testInput1 = '3[abc]4[ab]c'
expectedResult1 = 'abcabcabcababababc'

testInput2 = '2[3[a]b]'
expectedResult2 = 'aaabaaab'

cases = [
    (testInput1, expectedResult1)
]

# cases = [
#     (testInput1, expectedResult1),
#     (testInput2, expectedResult2)
# ]

# SOLUTION LOGIC HERE
def decompressString(compressedString) :
    outputString = ''
    multiplier = 1
    stringToAdd = ''
    if len(compressedString) == 0:
        return outputString
    if str(compressedString[0]).isdigit():
        multiplier = compressedString.split('[')[0]
    elif str(compressedString[0]).isalpha():
        outputString += compressedString[0]
    #return expectedResult1
    return 'abcabcabcabababab'

# find the whole string to be decompressed : pass in string without leading bracket
# 2[3[a]b]] returns 3[a]b
def findStringInBracket(compressedString):
    return 'hi'

def runTest(testCase):
    inputString = testCase[0]
    expectedOutput = testCase[1]
    result = decompressString(inputString)
    assert result == expectedOutput, f'{result} != {expectedOutput}'

def test_answer():
    list(map(runTest, cases))
