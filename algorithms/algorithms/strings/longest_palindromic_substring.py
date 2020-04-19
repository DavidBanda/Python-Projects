str_input = 'abaxyzzyxf'


def longestPalindromicSubstring(string):
    longest_substring = [0, 1]

    for i in range(1, len(string)):
        odd = long_palindrome(string, i - 1, i + 1)
        even = long_palindrome(string, i - 1, i)
        current = max(odd, even, key=lambda x: x[1] - x[0])
        longest_substring = max(current, longest_substring, key=lambda x: x[1] - x[0])

    return string[longest_substring[0]:longest_substring[1]]


def long_palindrome(string, idxLeft, idxRight):

    while idxLeft >= 0 and idxRight < len(string):
        if string[idxLeft] != string[idxRight]:
            break
        idxLeft -= 1
        idxRight += 1

    return [idxLeft + 1, idxRight]


print(longestPalindromicSubstring(str_input))






