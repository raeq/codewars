#!/bin/python3

from collections import Counter


def do_work(logo: str):
    c = dict(Counter(sorted(logo)).most_common(3))

    for k, v in c.items():
        print(f"{k} {v}")


if __name__ == '__main__':
    s = 'szrmtbttyyaymadobvwniwmozojggfbtswdiocewnqsjrkimhovimghixqryqgzhgbakpncwupcadwvglmupbexijimonxdowqsjinqzytkooacwkchatuwpsoxwvgrrejkukcvyzbkfnzfvrthmtfvmbppkdebswfpspxnelhqnjlgntqzsprmhcnuomrvuyolvzlni'

    do_work(s)
