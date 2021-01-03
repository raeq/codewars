"""
Input: 15
Output: 4
Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
"""


class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        i, ans = 1, 0

        while N > (i * (i - 1)) // 2:

            if (N - (i * (i - 1)) // 2) % i == 0:

                ans += 1

            i += 1
        return ans


s = Solution()
print(s.consecutiveNumbersSum(15))
