"""
dig_pow(89, 1) should return 1 since 8¹ + 9² = 89 = 89 * 1
dig_pow(92, 1) should return -1 since there is no k such as 9¹ + 2² equals 92 * k
dig_pow(695, 2) should return 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2
dig_pow(46288, 3) should return 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
"""


def dig_pow(n, p):
    ints = str(n)
    running_sum = 0

    for i, val in enumerate(ints, p):
        running_sum += int(val) ** i

    whole, remainder = divmod(running_sum, n)

    if remainder == 0:
        return whole

    return -1


assert (dig_pow(89, 1) == 1)
assert (dig_pow(92, 1) == -1)
assert (dig_pow(46288, 3) == 51)
