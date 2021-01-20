def twoSum(nums, target):
    """
    Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a
    specific target number.
    The function twoSum should return indices of the two numbers such that they add up to the target, where index1
    must be less than index2.

    Note:

    Your returned answers (both index1 and index2) are not zero-based.
    You may assume that each input would have exactly one solution and you may not use the same element twice.
    Example:

    Input: numbers = [2,7,11,15], target = 9
    Output: [1,2]
    Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

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
            return [nums.index(temp) + 1, yindex + 1]
        yindex = yindex + 1
        s.add(num)


assert twoSum(nums=[2, 7, 11, 15], target=9) == [1, 2]
assert twoSum(nums=[-3, 4, 3, 90], target=0) == [1, 3]
assert twoSum(nums=[0, 4, 3, 0], target=0) == [1, 4]
assert twoSum(nums=[2, 5, 5, 5], target=10) == [2, 3]
assert twoSum(nums=[3, 2, 4], target=6) == [2, 3]
