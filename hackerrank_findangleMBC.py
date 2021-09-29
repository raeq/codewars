"""
https://www.hackerrank.com/challenges/find-angle/problem
"""

# Using SOHCAHTOA we have adjacent and hypotenuese, M needs to be halved
# https://www.mathsisfun.com/algebra/trig-finding-angle-right-triangle.html
# Cosine: cos(θ) = Adjacent / Hypotenuse

import math


adjacent = float(input())
opposite = float(input())
c = adjacent / opposite
angle = math.degrees(math.atan(c))

print(round(angle))
