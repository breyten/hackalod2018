#!/usr/bin/env python
import os
import json
import sys

from googletrans import Translator

def main():
    words = {}
    with open('words.json') as in_file:
        words = json.load(in_file)

    translator = Translator()
    new_words = {}
    for k, v in words.iteritems():
        nk = translator.translate(k, src='en', dest='nl')
        new_words[nk.text] = v

    print json.dumps(new_words)

    return 0

if __name__ == '__main__':
    sys.exit(main())
