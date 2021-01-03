class Solution:
    def maxProfit(self, prices: list) -> int:
        low_mark: int = float("Inf")
        retVal: int = 0
        for p in prices:
            if p < low_mark:
                low_mark = p
            else:
                retVal = max(p - low_mark, retVal)
        return retVal


s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
print(s.maxProfit([7, 6, 4, 3, 1]))
print(s.maxProfit([2, 4, 1]))
