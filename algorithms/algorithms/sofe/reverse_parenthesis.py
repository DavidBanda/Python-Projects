string = 'a(bc(de)fg(hi)jk)'


def reverseParenthesis(string):
    string = list(string)
    brackets = []
    i = 0

    while i < len(string):

        if string[i] == '(':
            brackets.append(i)

        if string[i] == ')':
            startIdx = brackets.pop()
            reverseString(string, startIdx + 1, i - 1)
            string.pop(i)
            string.pop(startIdx)

        i += 1

    return ''.join(string)


def reverseString(string, startIdx, endIdx):

    while startIdx < endIdx:
        string[startIdx], string[endIdx] = string[endIdx], string[startIdx]
        startIdx += 1
        endIdx -= 1


print(reverseParenthesis(string))





