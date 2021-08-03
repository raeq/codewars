from collections import namedtuple as nt

import more_itertools


Cell: nt = nt("Cell", ["x", "y", "v"], defaults = (None, None, "-"))


def print_map(mp, short=False):
    if not short:
        print(f"mp:")
        for m in mp:
            print(m)
    else:
        print(f"mp2:")
        x: Cell
        for i, m in enumerate(mp):
            print(f"{i}{[x.v for x in m]}")


def parse_mp(m):
    grid = []
    x: int = 0
    m = m.split("\n")

    for l in m:
        row = []
        y = 0
        for c in l.split(' '):
            cell: Cell = Cell(x, y, c)
            row.append(cell)
            y += 1
        grid.append(row)
        x += 1
    return grid


def find_safe_cells(mp):
    c: Cell
    lsc = len(safe_cells)
    for c in more_itertools.flatten(mp):
        if c.v == "0":
            safe_cells.add(c)
    return max(len(safe_cells) - lsc, 0)


def open_cells(cells, mp):
    c: Cell
    for c in cells:
        if c not in bomb_cells:
            o = open(c.x, c.y)
            mp[o.x][o.y] = o


def get_highest(mp) -> int:
    c: Cell
    highest: int = 0
    for c in more_itertools.flatten(mp):
        try:
            highest = max(highest, int(c.v))
        except ValueError:
            pass
    return highest


def get_neighbours(c: Cell, mp):
    x_len = len(mp)
    y_len = len(mp[0])

    for x in range(x_len):
        for y in range(y_len):
            if x == c.x or x == c.x - 1 or x == c.x + 1:
                if y == c.y or y == c.y - 1 or y == c.y + 1:
                    yield mp[x][y]


def find_unknown_corners(mp, test="1"):
    c: Cell
    corners: set = set()
    for c in more_itertools.flatten(mp):
        if c.v == test:
            n: Cell
            count: int = 0
            temp_corners = set()
            hasx = False
            for n in get_neighbours(c, mp):
                if n.v == "?":
                    temp_corners.add(n)
                elif n.v == "x":
                    hasx = True
            if len(temp_corners) == 1 and not hasx:
                corners = temp_corners

    return corners


def make_bomb(c: Cell, mp):
    mp[c.x][c.y] = Cell(c.x, c.y, "x")
    bomb_cells.add(mp[c.x][c.y])
    for n in range(5):
        bomb_neighbours(mp)


def bomb_neighbours(mp):
    c: Cell
    n1: Cell
    n2: Cell

    for c in bomb_cells:
        neibs = list(get_neighbours(c, mp))
        for n1 in neibs:
            if n1.v == "1":
                open_cells(get_neighbours(n1, mp), mp)


def solve_mine(mp, n):
    mp = parse_mp(mp)
    print_map(mp, True)

    # Initial run to find safe cells and open their neighbours
    # find safecells
    while find_safe_cells(mp) > 0:
        for c in safe_cells:
            open_cells(get_neighbours(c, mp = mp), mp = mp)
    print_map(mp, True)

    h = get_highest(mp)
    print(h)

    corners = find_unknown_corners(mp, test = "1")

    while len(corners) > 0:
        c: Cell
        for c in corners:
            make_bomb(c, mp)
        corners = find_unknown_corners(mp, test = "1")

    print_map(mp, True)
    h = get_highest(mp)
    print(h)

    return len(bomb_cells)


def open(x, y):
    o: Cell = resultmp[x][y]
    if o.v == "x":
        raise RuntimeError()
    return o


# AFN all free neighbours
# AMN all mine neighbours
safe_cells = set()
bomb_cells = set()

h: int = 0

gamemp = """
? ? ? ? ? ?
? ? ? ? ? ?
? ? ? 0 ? ?
? ? ? ? ? ?
? ? ? ? ? ?
0 0 0 ? ? ?
""".strip()
result = """
1 x 1 1 x 1
2 2 2 1 2 2
2 x 2 0 1 x
2 x 2 1 2 2
1 1 1 1 x 1
0 0 0 1 1 1
""".strip()

resultmp = parse_mp(result)
print_map(resultmp, True)
print(solve_mine(gamemp, 6))
