def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    Example:
    Given nums = [2, 7, 11, 15], target = 9,
    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
    """

    # use a set to store seen values
    # it is a fast hashmap
    s = set()

    # we need a pair, so always store the first element
    s.add(nums[0])

    yindex = 1
    for num in nums[1::]:
        temp = target - num
        if temp in s:
            return [nums.index(temp), yindex]
        yindex = yindex + 1
        s.add(num)


assert twoSum(nums=[2, 7, 11, 15], target=9) == [0, 1]
assert twoSum(nums=[-3, 4, 3, 90], target=0) == [0, 2]
assert twoSum(nums=[0, 4, 3, 0], target=0) == [0, 3]
assert twoSum(nums=[2, 5, 5, 5], target=10) == [1, 2]
assert twoSum(nums=[3, 2, 4], target=6) == [1, 2]
