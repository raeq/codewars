class Solution:

    @staticmethod
    def isNumber(s: str) -> bool:

        if s:
            if s.strip():
                s = s.strip()
                try:
                    s = int(s)
                except BaseException as e:
                    print(e)
                else:
                    return True
                try:
                    s = float(s)
                except BaseException as e:
                    print(e)
                else:
                    return True

        return False


s:Solution = Solution()

assert Solution.isNumber("0") == True
assert Solution.isNumber(" 0.1 ") == True
assert Solution.isNumber("1 a") == False
assert Solution.isNumber("2e10") == True
assert Solution.isNumber(" 2e10 ") == True
assert Solution.isNumber(" 1e") == False
assert Solution.isNumber("e3") == False
assert Solution.isNumber(" 6e-1") == True
assert Solution.isNumber(" 99e2.5 ") == False
assert Solution.isNumber("53.5e93") == True
assert Solution.isNumber(" --6 ") == False
assert Solution.isNumber("-+3") == False
assert Solution.isNumber(" 95a54e53 ") == False
assert Solution.isNumber(" +1 ") == True
assert Solution.isNumber(" -1 ") == True
