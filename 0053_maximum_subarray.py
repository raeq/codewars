"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum
and return its sum.
"""


class Solution:
    @staticmethod
    def maxSubArray(nums: list) -> int:
        """
        Kadane's algorithm.
        """

        n = len(nums)

        if 0 >= n:
            return 0
        elif 1 == n:
            return nums[0]

        maximum_sum = float("-Inf")
        current_sum: int = 0

        for val in nums:
            current_sum = max(val, current_sum + val)
            maximum_sum = max(maximum_sum, current_sum)

        return maximum_sum


if __name__ == '__main__':
    s = Solution()
    assert (s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6)
