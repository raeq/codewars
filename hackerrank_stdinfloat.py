import fileinput


c = 0
for line in fileinput.input():
    if c == 0:
        pass
    elif not '.' in line:
        print(False)
    else:
        try:
            f = float(line)
            print(True)
        except Exception as e:
            print(False)

    c += 1
