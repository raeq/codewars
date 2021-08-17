from collections import deque


cmds: list = list()

cmds.append(("append", 1))
cmds.append(("append", 2))
cmds.append(("append", 3))
cmds.append(("appendleft", 4))
cmds.append(("pop",))
cmds.append(("popleft",))

d = deque()
for cmd in cmds:
    print(cmd)
    if len(cmd) == 2:
        getattr(d, cmd[0])(cmd[1])
    elif len(cmd) == 1:
        getattr(d, cmd[0])()

print(d)
