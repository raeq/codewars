"""
In this kata, you will write a function that returns the positions and the values of the "peaks" (or local maxima) of
a numeric array.

For example, the array arr = [0, 1, 2, 5, 1, 0] has a peak at position 3 with a value of 5 (since arr[3] equals 5).

The output will be returned as an object with two properties: pos and peaks. Both of these properties should be
arrays. If there is no peak in the given array, then the output should be {pos: [], peaks: []}.

Example: pickPeaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3]) should return {pos: [3, 7], peaks: [6, 3]} (or equivalent in
other languages)

"""


def pick_peaks(arr):
    prev, cur = 0, 0
    result = {"pos": [], "peaks": []}

    for next in range(1, len(arr)):
        if arr[next] > arr[cur]:
            prev = cur
            cur = next
        else:
            if arr[next] < arr[cur]:
                if arr[prev] < arr[cur]:
                    result["pos"].append(cur)
                    result["peaks"].append(arr[cur])
                prev = cur
                cur = next

    return result


assert (pick_peaks([1, 2, 2, 6, 4, 1, 2, 3, 2, 1]) == {"pos": [3, 7], "peaks": [6, 3]})
assert (pick_peaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3]) == {"pos": [3, 7], "peaks": [6, 3]})
assert (pick_peaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 2, 2, 1]) == {"pos": [3, 7, 10], "peaks": [6, 3, 2]})
assert (pick_peaks([2, 1, 3, 1, 2, 2, 2, 2, 1]) == {"pos": [2, 4], "peaks": [3, 2]})
assert (pick_peaks([2, 1, 3, 1, 2, 2, 2, 2]) == {"pos": [2], "peaks": [3]})
assert (pick_peaks([2, 1, 3, 2, 2, 2, 2, 5, 6]) == {"pos": [2], "peaks": [3]})
assert (pick_peaks([2, 1, 3, 2, 2, 2, 2, 1]) == {"pos": [2], "peaks": [3]})
assert (pick_peaks([]) == {"pos": [], "peaks": []})
assert (pick_peaks([1, 1, 1, 1]) == {"pos": [], "peaks": []})
