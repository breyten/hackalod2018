#!/usr/bin/env python

import sys
import os
import json
from glob import glob


def main():
    all_words = {}
    for f in glob('faces/*'):
        fname = os.path.basename(f).replace('.png', '')
        fwords = fname.split('_')
        for fword in fwords:
            try:
                all_words[fword] += [fname]
            except Exception:
                all_words[fword] = [fname]
    print json.dumps(all_words)
    return 0

if __name__ == '__main__':
    sys.exit(main())
