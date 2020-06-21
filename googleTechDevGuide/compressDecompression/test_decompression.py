
testInput1 = '3[abc]4[ab]c'
expectedResult1 = 'abcabcabcababababc'

testInput2 = '2[3[a]b]'
expectedResult2 = 'aaabaaab'

testInput3 = '10[3[a]b]'
expectedResult3 = 'aaabaaabaaabaaabaaabaaabaaabaaabaaabaaab'

cases = [
    (testInput1, expectedResult1),
    (testInput2, expectedResult2),
    (testInput3, expectedResult3)
]
# SOLUTION LOGIC HERE
def decompressString(compressedString) :
    outputString = ''
    multiplier = 1
    stringToAdd = ''
    # base case : empty string
    if len(compressedString) == 0:
        return outputString
    # case of 2[ab] - find multiplier
    if str(compressedString[0]).isdigit():
        multiplier = int(compressedString.split('[')[0])
        compressedString = compressedString[len(str(multiplier))+1:]
    # case of ab or a2[b] or ab2[b]
    if str(compressedString[0]).isalpha():
        currString = ''
        innerString = ''
        while len(compressedString) > 0 and str(compressedString[0]).isalpha():
            currString += compressedString[0]
            compressedString = compressedString[1:]
        if len(compressedString) and compressedString[0] == ']':
            innerString = decompressString(compressedString[1:])
        stringToAdd = multiplier * currString + innerString
    elif str(compressedString[0]).isdigit():
        stringToAdd = multiplier * decompressString(compressedString)
    outputString += stringToAdd
    return outputString

def runTest(testCase):
    inputString = testCase[0]
    expectedOutput = testCase[1]
    result = decompressString(inputString)
    assert result == expectedOutput, f'{result} != {expectedOutput}'
    print(f'\nTest case passed \n\t Input:\t{testCase[0]}\n\tOutput:\t{result}')

def test_answer():
    list(map(runTest, cases))
