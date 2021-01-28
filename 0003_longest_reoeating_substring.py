class Solution:
    def lengthOfLongestSubstring(self, input_string):

        longest = 0
        left, right = 0, 0
        chars = set()
        len_string = len(input_string)

        while left < len_string and right < len_string:

            if input_string[right] not in chars:
                chars.add(input_string[right])
                right += 1
                longest = max(longest, right - left)

            else:
                chars.remove(input_string[left])
                left += 1

            if len_string - left < longest:
                return longest

        return longest

s = Solution()
assert s.lengthOfLongestSubstring('abcabcbb') == 3
assert s.lengthOfLongestSubstring('bbbbb') == 1
assert s.lengthOfLongestSubstring('pwwkew') == 3
