'''
Street Fighter V tools
'''

import glob
import itertools
import os
# import sys
from pprint import pprint as pp


STATS = [
    'health',
    'stun',
    'taunt',
    'jump',
    'jump forward',
    'jump backward',
    'dash forward',
    'dash backward',
]


def get_chars(only=None):
    '''
    returns dictionary of character data
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


def _split_ints(v):
    r = [int(''.join(x)) for isnum, x in itertools.groupby(v, key=str.isdigit) if isnum]
    if not r:
        return v
    return r


def load_char_from_path(fn):
    '''
    returns charname(str), chardata(dict)
    '''
    with open(fn) as f:  # XXX brittle
        charname = os.path.basename(fn).split('.')[0]  # XXX brittle
        keys = []
        cdata = {}

        for line in f:
            line = line.strip()
            els = line.split('\t')
            if els[0] == 'Move':
                keys = [e.strip() for e in els]
                continue

            row = dict(zip(keys, els))
            for prop, val in row.items():
                row[prop] = parse_data(prop, val)

            mvname = row['Move']

            # add tags to make queries possible
            tags = set()
            if mvname not in ('stun', 'taunt', 'health', 'V-TRIGGER'):
                if mvname.startswith('jump'):
                    tags.add('jump')
                elif mvname.startswith('dash'):
                    tags.add('dash')
                else:
                    tags.add('oki')
            else:
                tags.add('stats')

            if row.get('Hit Advantage') == 'KD':
                tags.add('kd')

            cdata[mvname] = row
            cdata[mvname]['tags'] = tags

        return charname, cdata


if __name__ == '__main__':
    d = get_chars('GUL')
    pp(d)
    # for charname, moves in d.items():
    #     for move, props in moves.items():
    #         for prop, val in props.items():
    #             d[charname][move][prop] = parse_data(prop, val)
