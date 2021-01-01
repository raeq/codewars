from collections import defaultdict


def tickets(people):
    register: defaultdict = defaultdict(int)

    for note in people:
        if note != 25:
            return_units = (note - 25) // 25

            # return 50$
            if return_units == 1:
                if register[25] >= 1:
                    register[25] -= 1
                else:
                    return "NO"

            # return 75$
            elif return_units == 3:
                #do we have 75$
                if register[50] > 0 and register[25]>0:
                    register[50] -= 1
                    register[25] -= 1
                elif register[25] >= 3:
                    register[25] -= 3
                else:
                    return "NO"

        register[note] += 1
    return "YES"


assert (tickets([25, 25, 50, 50, 100]), "NO")
assert (tickets([25, 25, 50]) == "YES")
assert (tickets([25, 100]) == "NO")