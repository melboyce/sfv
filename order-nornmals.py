#!/usr/bin/python2
from __future__ import print_function

import os
import sys
from operator import itemgetter
from termcolor import colored
from pprint import pprint as pp


def main():
    if len(sys.argv) < 2:
        print('usage: {} CHARCODE'.format(sys.argv[0]))
        print('e.g. : {} GUL'.format(sys.argv[0]))
        return 1

    charfn = os.path.join('.', 'OKI', '{}.txt'.format(sys.argv[1].upper()))

    if not os.path.exists(charfn):
        print('error: unable to find character data')
        print('expectation: ./OKI/CODE.txt')
        return 2

    moves = []
    longest_name = 0
    with open(charfn, 'r') as data:
        for line in data:
            els = line.split('\t')

            # TODO this whole set of guards is stinky :/
            if els[0] in ('Move', 'health', 'stun', 'taunt', 'jump'):
                continue

            if 'CHAIN' in els[0]:
                continue

            if 'somersault' in els[0] or 'sonic' in els[0]:
                continue

            if els[0].startswith('jump') or els[0].startswith('dash'):
                continue

            if 'LP+LK' in els[1] or 'HP+HK' in els[1]:
                continue

            if '(' in els[3]:
                continue

            if not els[3] or not els[4]:
                continue

            if '?' in els[2] or '?' in els[3] or '?' in els[4]:
                continue

            if els[3] == '-' or els[4] == '-':
                continue

            try:
                move = {'name': els[0], 'startup': int(els[2]), 'active': int(els[3]), 'recovery': int(els[4])}
            except Exception:
                pp(line)
                raise

            moves.append(move)

            if len(els[0]) > longest_name:
                longest_name = len(els[0])

    moves = sorted(moves, key=itemgetter('startup', 'active', 'recovery'))

    for move in moves:
        s, a, r, n = '', '', '', ''
        for i in range(move['startup']):
            s += '-'
        for i in range(move['active']):
            a += '#'
        for i in range(move['recovery']):
            r += '-'
        n = move['name']

        print(n.rjust(longest_name), end='')
        print(' {}{}{}'.format(colored(s, 'red'), colored(a, 'green'), colored(r, 'blue')))


if __name__ == '__main__':
    sys.exit(main())
