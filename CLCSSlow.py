import sys
import numpy as np
from LCS import LCS

def CLCS(A, B):
    m = len(A)
    maxLen = -1
    for i in xrange(0, m):
        testVal = LCS(cut(A, i), B)
        if testVal > maxLen:
            maxLen = testVal
    return maxLen


def cut(str, index):
    retStr = ""
    for i in xrange(index, len(str)):
        retStr += str[i]
    for i in xrange(0, index):
        retStr += str[i]
    return retStr

def main():
    if len(sys.argv) != 1:
        sys.exit('Usage: `python CLCSSlow.py < input`')
    for l in sys.stdin:
        A,B = l.split()
        print CLCS(A,B)
    
if __name__ == '__main__':
    main()
