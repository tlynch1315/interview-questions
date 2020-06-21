


testCases = [('hi', 'hi')]

def minesweeper(inputString):
    return 'ho'

def runTestCase(testCase, function):
    inputString = testCase[0]
    expectedOutput = testCase[1]
    result = function(inputString)
    assert result == expectedOutput, f'{result} != {expectedOutput}'
    print(f'\nTest case passed \n\t Input:\t{testCase[0]}\n\tOutput:\t{result}')

def test_minesweeper():
    [runTestCase(testCase, minesweeper) for testCase in testCases]
