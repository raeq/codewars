#
# Complete the 'numCells' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY grid as parameter.
#

def numCells(grid):
    dominants = set()

    rows = len(grid) - 1
    cols = len(grid[0]) - 1

    for r in range(len(grid)):
        for c in range(len(grid[0])):

            val = grid[r][c]
            print(val, f"({r},{c})")

            nw = val - grid[max(r - 1, 0)][max(c - 1, 0)]
            n = val - grid[max(r - 1, 0)][c]
            ne = val - grid[max(r - 1, 0)][min(c + 1, cols)]
            se = val - grid[min(r + 1, rows)][min(c + 1, cols)]
            s = val - grid[min(r + 1, rows)][c]
            sw = val - grid[min(r + 1, rows)][max(c - 1, 0)]
            e = val - grid[r][min(c + 1, cols)]
            w = val - grid[r][max(c - 1, 0)]

            if r == 0:
                nw, n, ne = 100, 100, 100

            if r == rows:
                se, s, sw = 100, 100, 100

            if c == cols:
                e, se, ne = 100, 100, 100

            if c == 0:
                w, sw, nw = 100, 100, 100

            if all(i > 0 for i in [nw, n, ne, e, se, s, sw, w]):
                dominants.add((r, c))

    return len(dominants)


grid = [[1, 2, 7], [4, 5, 6], [8, 8, 9]]
print(numCells(grid))
