'''
Street Fighter V tools
--

should be pretty obvious what to do. check the bottom for an example.

NOTE: there are some brittle spots, but I'm erring on the side of savvy user so
I don't have to burn cycles being defensive.
'''

import glob
import itertools
import os
# import sys
from pprint import pprint as pp


def get(only=None):
    '''
    returns dictionary of character data
    only optionally specifies the charcode for one character to load
    '''
    data = {}

    if only:
        charname, chardata = load_char_from_path('./OKI/{}.txt'.format(only))
        data[charname] = chardata
    else:
        for fn in glob.glob('./OKI/???.txt'):
            charname, chardata = load_char_from_path(fn)
            data[charname] = chardata

    return data


def parse_data(k, v):
    '''
    accepts a key and a value from a move and returns a reformatted value if
    appropriate.
    '''
    # XXX may not be complete.
    # int?
    try:
        return int(v)
    except ValueError:
        # XXX brittle
        _k = k.lower().strip()
        if _k == 'active':
            if '(' in v:
                return _split_ints(v)

        if _k == 'cancel ability':
            return v.split(',')

        if _k == 'attack level':
            return v.split('*')

        if '*' in v:  # NOTE: this can clobber attack level
            return _split_ints(v)

    return v


def load_char_from_path(fn):
    '''
    returns charname(str), chardata(dict)
    '''
    with open(fn) as f:  # XXX brittle
        charname = os.path.basename(fn).split('.')[0]  # XXX brittle
        keys = []
        cdata = {}
        idx = 0

        for line in f:
            line = line.strip()
            els = line.split('\t')
            if els[0] == 'Move':
                keys = [e.strip().lower() for e in els]
                continue

            row = dict(zip(keys, els))
            row['index'] = idx
            for prop, val in row.items():
                row[prop] = parse_data(prop, val)

                # sometimes total isn't present even though startup, active, and recovery are known
                if row.get('total') in ('', '-', '?', '??'):
                    try:
                        row['total'] = row['startup'] + row['active'] + row['recovery'] - 1
                    except TypeError:
                        pass

            mvname = row['move']

            # add tags to make queries possible
            tags = set()
            if mvname not in ('stun', 'taunt', 'health', 'v-trigger'):
                if mvname.startswith('jump'):
                    tags.add('jump')
                elif mvname.startswith('dash'):
                    tags.add('dash')
                else:
                    tags.add('oki')
            else:
                tags.add('stats')

            if row.get('hit advantage') == 'KD':
                tags.add('kd')

            cdata[mvname] = row
            cdata[mvname]['tags'] = tags

            idx += 1

        return charname, cdata


def _split_ints(v):
    r = [int(''.join(x)) for isnum, x in itertools.groupby(v, key=str.isdigit) if isnum]
    if not r:
        return v
    return r


if __name__ == '__main__':
    d = get('GUL')
    pp(d)
    # for charname, moves in d.items():
    #     for move, props in moves.items():
    #         for prop, val in props.items():
    #             d[charname][move][prop] = parse_data(prop, val)
