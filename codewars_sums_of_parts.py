"""
ls = [0, 1, 3, 6, 10]
ls = [1, 3, 6, 10]
ls = [3, 6, 10]
ls = [6, 10]
ls = [10]
ls = []
"""


def parts_sums(ls):
    results = [sum(ls)]

    while ls:
        print(results[-1])
        results.append(results[-1] - ls.pop(0))

    return results


print(parts_sums([0, 1, 3, 6, 10]))
