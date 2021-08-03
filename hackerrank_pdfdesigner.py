"""
https://www.hackerrank.com/challenges/designer-pdf-viewer/problem
"""

import string


def designerPdfViewer(h, word):
    chars = list(string.ascii_lowercase)
    heights = []

    for char in word:
        heights.append(h[chars.index(char)])

    return max(heights) * len(word)


assert (designerPdfViewer([1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5], 'abc') == 9)
