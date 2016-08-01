#!/usr/bin/python

import sys, re

m = re.compile('true', flags=re.I)

def main(args):
    s = args[0] if len(args) > 0 else "Umm"
    exclaim = True if len(args) > 1 and m.match(args[1]) else False
    print sayit(s, exclaim)

def sayit(s, exclaim):
    result = s + ", " + s + ", " + s
    if exclaim:
        result += "!!!"
    return result

if __name__ == "__main__":
    main(sys.argv[1:])
