class Solution:
    def isAlienSorted(self, words: list, order: str) -> bool:
        return words == sorted(words,
                               key=lambda word: [order.index(c) for c in word])


s = Solution()
assert (s.isAlienSorted(["word", "world", "row"], "worldabcefghijkmnpqstuvxyz") == False)
assert (s.isAlienSorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz") == True)
