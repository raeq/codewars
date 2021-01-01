"""
Implement atoi which converts a string to an integer.
The function first discards as many whitespace characters as necessary until the first non-whitespace character is
found. Then, starting from this character, takes an optional initial
plus or minus sign followed by as many numerical digits as possible,
and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number,
which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such
sequence exists because either str is empty or it contains only whitespace
characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Input: "42"
Output: 42

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical
             digit or a +/- sign. Therefore no valid conversion could be performed.

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.
Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.

"""
import string

class Solution(object):
    """
    >>> s = Solution


    >>> s.myAtoi(self = s, input_str = "-13+8")
    -13
    >>> s.myAtoi(self = s, input_str = "-5-")
    -5
    >>> s.myAtoi(self = s, input_str = "  -0012a42")
    -12
    >>> s.myAtoi(self = s, input_str = "3.14159")
    3
    >>> s.myAtoi(self = s, input_str = "-91283472332")
    -2147483648
    >>> s.myAtoi(self = s, input_str = "words and 987")
    0
    >>> s.myAtoi(self = s, input_str = "42")
    42
    >>> s.myAtoi(self = s, input_str = "4193 with words")
    4193
    >>> s.myAtoi(self = s, input_str = "   -42")
    -42
    """
    def myAtoi(self, input_str):
        numbers = set({str(i) for i in range(10)})
        letters = set(string.ascii_letters)

        retVal = 0
        input_str = input_str.strip().split(" ")[0]
        # find first non digit
        index = 0
        for s in input_str:
            if s in letters:
                input_str = input_str[0:index:]
                break
            index = index + 1

        index = 0
        for s in input_str:
            if index > 0:
                if s not in numbers:
                    input_str = input_str[0:index:]
                    break
            index = index + 1

        try:
            retVal = int(float(input_str))
        except ValueError as e:
            pass
        else:
            if retVal < -2147483648:
                retVal = -2147483648
            elif retVal > 2147483647:
                retVal = 2147483647
        return retVal