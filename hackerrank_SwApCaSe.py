import string


l_au = list(string.ascii_uppercase)
l_al = list(string.ascii_lowercase)
s_au = set(l_au)
s_al = set(l_al)


def swap_case(s):
    out = ""

    for c in s:
        if c in s_al:
            out += string.ascii_uppercase[l_al.index(c)]

        elif c in s_au:
            out += string.ascii_lowercase[l_au.index(c)]

        else:
            out += c

    return out


if __name__ == '__main__':
    print(swap_case(input()))
