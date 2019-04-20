#! /usr/bin/env python3

from pathlib import Path
import sys

f1 = Path(sys.argv[1]).read_text().split('\n')[:-1]
f2 = Path(sys.argv[2]).read_text().split('\n')[:-1]

for l1, l2 in zip(f1, f2):
    i, name, ty, val1 = l1.split('\t')
    _, _   , _ , val2 = l2.split('\t')
    if ty == 'NUMERIC':
        v1, v2 = val1[4:], val2[4:]
        if '.' in v1:
            v1, v2 = float(v1), float(v2)
        else:
            v1, v2 = int(v1), int(v2)
        val = f'MAX:{max(v1,v2)}'
    elif ty == 'CATEGORICAL':
        val = ' '.join(sorted(set(val1.split(' ') + val2.split(' '))))
    else:
        val = 'INVALID'
    print('\t'.join([i, name, ty, val]))


