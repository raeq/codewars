"""
likes([]) # must be "no one likes this"
likes(["Peter"]) # must be "Peter likes this"
likes(["Jacob", "Alex"]) # must be "Jacob and Alex like this"
likes(["Max", "John", "Mark"]) # must be "Max, John and Mark like this"
likes(["Alex", "Jacob", "Mark", "Max"]) # must be "Alex, Jacob and 2 others like this"

https://www.codewars.com/kata/5266876b8f4bf2da9b000362/train/python
"""


def likes(names):
    my_len = len(names)

    if my_len == 0:
        return "no one likes this"
    elif my_len == 1:
        return f"{names[0]} likes this"
    elif my_len == 2:
        return f"{names[0]} and {names[1]} like this"
    elif my_len == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {my_len - 2} others like this"


# your code here
assert (likes([]) == 'no one likes this')
assert (likes(['Peter']) == 'Peter likes this')
assert (likes(['Jacob', 'Alex']) == 'Jacob and Alex like this')
assert (likes(['Max', 'John', 'Mark']) == 'Max, John and Mark like this')
assert (likes(['Alex', 'Jacob', 'Mark', 'Max']) == 'Alex, Jacob and 2 others like this')
