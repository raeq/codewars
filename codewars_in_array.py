"""
Given two arrays of strings a1 and a2 return a sorted array r in lexicographical order of the strings of a1 which are
substrings of strings of a2.

#Example 1: a1 = ["arp", "live", "strong"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

returns ["arp", "live", "strong"]

#Example 2: a1 = ["tarp", "mice", "bull"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

returns []
https://www.codewars.com/kata/550554fd08b86f84fe000a58/train/python
"""


def in_array(array1, array2):
    ret_list = set()

    for a1 in array1:
        for a2 in array2:
            if a1 in a2:
                ret_list.add(a1)

    return sorted(list(ret_list))