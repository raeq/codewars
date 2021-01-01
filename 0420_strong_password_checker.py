"""
A password is considered strong if below conditions are all met:

It has at least 6 characters and at most 20 characters.
It must contain at least one lowercase letter, at least one uppercase letter, and at least one digit.

It must NOT contain three repeating characters in a row ("...aaa..." is weak, but "...aa...a..."
is strong, assuming other conditions are met).

Write a function strongPasswordChecker(s), that takes a string s as input, and return the MINIMUM change
required to make s a strong password. If s is already strong, return 0.
"""
import string


class Solution(object):
    """
    >>> s = Solution
    >>> s.strongPasswordChecker(self=s, s = "1111111111")
    3
    >>> s.strongPasswordChecker(s, s = "AAAbbb")
    2
    >>> s.strongPasswordChecker(s, s = "AAAbbb")
    2
    >>> s.strongPasswordChecker(s, s = "aaa111")
    2
    >>> s.strongPasswordChecker(s, s = "000a")
    2
    >>> s.strongPasswordChecker(s, s = "000")
    3
    >>> s.strongPasswordChecker(s, s = "a")
    5
    >>> s.strongPasswordChecker(s, s = "aBC012")
    0
    >>> s.strongPasswordChecker(s, s = "aBC-12")
    0
    >>> s.strongPasswordChecker(self=s, s = "1111111111")
    3
    >>> s.strongPasswordChecker(s, s = "AAAbbb")
    2
    >>> s.strongPasswordChecker(s, s = "aaa111")
    2
    >>> s.strongPasswordChecker(s, s = "aA1")
    3
    >>> s.strongPasswordChecker(s, s = "      ")
    3
    >>> s.strongPasswordChecker(s, s = "aaa123")
    1
    >>> s.strongPasswordChecker(s, s = "aB1")
    3
    >>> s.strongPasswordChecker(s, s = "aB12")
    2
    >>> s.strongPasswordChecker(s, s = "ab")
    4
    >>> s.strongPasswordChecker(s, s = "a")
    5
    >>> s.strongPasswordChecker(s, s = "0123456")
    2
    >>> s.strongPasswordChecker(s, s = " - - -")
    3
    >>> s.strongPasswordChecker(s, s = "")
    6
    >>> s.strongPasswordChecker(s, s = "0123456")
    2
    >>> s.strongPasswordChecker(s, s = "ABCDEF")
    2
    >>> s.strongPasswordChecker(s, s = "ABC012")
    1
    >>> s.strongPasswordChecker(s, s = "aBC012")
    0
    >>> s.strongPasswordChecker(s, s = "aBC000")
    1
    >>> s.strongPasswordChecker(s, s = "aBC000-111-222-3333")
    4
    >>> s.strongPasswordChecker(s, s = "0123456789012345678901234567aB")
    10
    >>> s.strongPasswordChecker(s, s = "012345678901234567890123456789")
    12

    """

    def strongPasswordChecker(self, s):
        """
        :type s: str
        :rtype: int
        """
        missing_type = 3
        if any('a' <= c <= 'z' for c in s): missing_type -= 1
        if any('A' <= c <= 'Z' for c in s): missing_type -= 1
        if any(c.isdigit() for c in s): missing_type -= 1

        change = 0
        one = two = 0
        p = 2
        while p < len(s):
            if s[p] == s[p - 1] == s[p - 2]:
                length = 2
                while p < len(s) and s[p] == s[p - 1]:
                    length += 1
                    p += 1

                change += length / 3
                if length % 3 == 0:
                    one += 1
                elif length % 3 == 1:
                    two += 1
            else:
                p += 1

        if len(s) < 6:
            return int(max(missing_type, 6 - len(s)))
        elif len(s) <= 20:
            return int(max(missing_type, change))
        else:
            delete = len(s) - 20

            change -= min(delete, one)
            change -= min(max(delete - one, 0), two * 2) / 2
            change -= max(delete - one - 2 * two, 0) / 3

            return int(delete + max(missing_type, change))