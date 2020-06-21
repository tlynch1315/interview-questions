import re
testCase1 = {
    'S' : 'abpplee',
    'D' : [
        'able',
        'ale',
        'apple',
        'bale',
        'kangaroo'
    ],
    'expected' : 'apple'
}

testCase2 = {
    'S' : 'jackajackajackjackajackajackjackajackajackjackajackajackjackajackajack',
    'D' : [
        'ajack',
        'jack',
        'jackajack',
        '',
        'j'
    ],
    'expected' : 'jackajack'
}

testCase3 = {
    'S' : 'a',
    'D' : [
        'ajack',
        'jack',
        'jackajack',
        '',
        'j'
    ],
    'expected' : None
}



testCases = [testCase1, testCase2, testCase3]

def getLettersAfter(string):
    result = {}
    for i, char in enumerate(string):
        if char in result:
            continue
        else:
            result[char] = [x for x in string[i:]]
    return result

def passes(string, substring):
    if string == substring:
        return True
    lettersAfter = getLettersAfter(string)
    if not all(x in lettersAfter for x in substring):
        return False
    for i, char in enumerate(substring):
        if not all(x in lettersAfter[char] for x in substring[i:]):
            return False
    return True

def containsSubstring(string, substring):
    letterCountFull = getLetterCount(string)
    print(letterCountFull)
    currString = ''
    if len(substring) == 1 and substring in string:
        return True
    for i in range(1,len(substring)):
        if substring[i-1] in letterCountFull and substring[i] in letterCountFull:
            firstPosition = int(letterCountFull[substring[i-1]].pop(0))
            secondPosition = int(letterCountFull[substring[i]].pop(0))
            if secondPosition < firstPosition:
                return False
            currString += substring[i-1]
            currString += substring[i]
        else:
            return False
    return True

def findLongestSubstring(S, D):
    D.sort(reverse=True, key=lambda x: len(x))
    answer = False
    while not answer and len(D):
        curr = D.pop(0)
        if passes(S, curr):
            answer = curr
    return None if not answer else answer



def runTestCase(testCase, function):
    string = testCase['S']
    dictionary = testCase['D']
    expected = testCase['expected']
    result = function(string, dictionary)
    assert result == expected, f'{result} != {expected}'
    print(f'\nTest case passed \n\t Input:\n\t\tS:\t{string}\n\t\tD:{dictionary}\n\tOutput:\t{result}')
    
    
def test_substring():
    [runTestCase(testCase, findLongestSubstring) for testCase in testCases]