"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water
it can trap after raining.
"""
import math
from typing import List

class Solution:

    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        volume: int = 0
        length = len(height)

        left_max = []
        right_max = []

        left_max.append(height[0])
        for k, v in enumerate(height):
            if k == 0: continue
            left_max.append(max(left_max[k-1], v))

        right_max.append(height[-1])
        for k, v in enumerate(reversed(height)):
            if k == 0: continue
            right_max.append(max(right_max[k-1], v))
        right_max = list(reversed(right_max))

        water_volumes = []
        for k, v in enumerate(height):
            m = min(left_max[k], right_max[k])
            water_volumes.append(m - v)

        return (sum(water_volumes))


s = Solution()
assert s.trap([4, 2, 0, 3, 2, 5]) == 9
assert s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
