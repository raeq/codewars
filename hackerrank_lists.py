z = 29
l1 = [['append', 1], ['append', 6], ['append', 10], ['append', 8], ['append', 9], ['append', 2], ['append', 12],
      ['append', 7],
      ['append', 3], ['append', 5], ['insert', 8, 66], ['insert', 1, 30], ['insert', 6, 75], ['insert', 4, 44],
      ['insert', 9, 67],
      ['insert', 2, 44], ['insert', 9, 21], ['insert', 8, 87], ['insert', 1, 75], ['insert', 1, 48], ['print'],
      ['reverse'], ['print'],
      ['sort'], ['print'], ['append', 2], ['append', 5], ['remove', 2], ['print']]

if __name__ == '__main__':
    N = z
    i = 0
    inputs = []
    data = []
    cmd: str

    for cmd in l1:
        i += 1
        inputs.append(cmd)
        if i == N:
            break

    for cmd in inputs:
        c: str = ""
        d: int = 0
        e: int = 0

        try:
            c = cmd[0]
            d = int(cmd[1])
            e = int(cmd[2])
        except Exception:
            pass

        if c == "insert":
            pos = int(d)
            data[pos:pos] = [e]
        elif c == "print":
            print(data)
        elif c == "remove":
            data.remove(d)
        elif c == "sort":
            data = sorted(data)
        elif c == "append":
            data.append(d)
        elif c == "pop":
            data.pop()
        elif c == "reverse":
            data = data[::-1]
