def recaman(n):
    s = set()
    a = list()
    s.add(0)
    a.append(0)

    prev = 0
    for i in range(1, n):

        curr = prev - i

        # If arr[i-1] - i is negative or
        # already exists.
        if (curr < 0 or curr in s):
            curr = prev + i

        s.add(curr)
        a.append(curr)

        prev = curr

    del a[0]
    return a


print(recaman(20))
