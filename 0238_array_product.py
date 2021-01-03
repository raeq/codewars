"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of
all the elements of nums except nums[i].
Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
"""


class Solution:
    def productExceptSelf(self, nums: list) -> list:
        n = len(nums)
        res = [1 for _ in range(n)]
        f, b = 1, 1
        for i in range(n):
            res[i] *= f
            res[n - 1 - i] *= b
            f *= nums[i]
            b *= nums[n - 1 - i]
        return res


s = Solution()
print(s.productExceptSelf([1, 2, 3, 4]))
