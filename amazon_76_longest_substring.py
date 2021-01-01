"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""

def lengthOfLongestSubstring(subject: str) -> int:

    s_length=1
    my_len = len(s)
    longest = 1

    for i in range(0, my_len):
        for y in range(i, mylen):
            if subject[i:y] == 

        pass


    return longest




assert lengthOfLongestSubstring("abcabcbb") == 3
assert lengthOfLongestSubstring("bbbbb") == 1