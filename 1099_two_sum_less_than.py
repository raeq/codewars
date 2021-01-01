import collections as c

def twoSum(nums, target):
    """

    Given an array A of integers and integer K, return the maximum S such that there
    exists i < j with A[i] + A[j] = S and S < K. If no i, j exist satisfying this equation, return -1.
    Example 1:

    Input: A = [34,23,1,24,75,33,54,8], K = 60
    Output: 58
    Explanation:
    We can use 34 and 24 to sum 58 which is less than 60.
    Example 2:

    Input: A = [10,20,30], K = 15
    Output: -1
    Explanation:
    In this case it's not possible to get a pair sum less that 15.
    """

    #first make sure all inputs are less than target
    candidates = [num  for num in nums if num <= target]


    max = -1
    index = 1
    for num in reversed(sorted(candidates)):
        candidates2 = list(reversed(sorted([num2 for num2 in candidates if num2 > num])))
        for num2 in candidates2:
            t = num + num2
            if t < target:
                if t > max:
                    max = t
                    break
        index=index+1
    return max



assert twoSum(nums=[2, 7, 11, 15], target=30) == 26
assert twoSum(nums = [34,23,1,24,75,33,54,8], target = 60) == 58
assert twoSum(nums=[-3, 4, 3, 90], target=80) == 7
assert twoSum(nums=[0, 4, 3, 0], target=8) == 7
assert twoSum(nums=[2, 5, 5, 5], target=10) == 7
assert twoSum(nums=[3, 2, 4], target=7) == 6
