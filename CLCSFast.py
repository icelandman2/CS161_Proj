import sys
import numpy as np

arr = np.zeros((4096, 2048), dtype=int)
pointers = np.zeros((2048, 2048), dtype=int)

def findShortestPaths(A,B,p,l,u):
        if u-1<=l:
            return
        mid = (l+u)/2
        p[mid] = singleShortestPath(A,B,mid,p[l], p[u])
        findShortestPaths(A,B,p,l,mid)
        findShortestPaths(A,B,p,mid,u)

def singleShortestPath(A, B, mid, lowerPath, upperPath):
    m = len(A) / 2
    n = len(B)

    for i in range(mid + 1, mid + m + 1):
        lowerBound = lowerPath[0].get(i, (n,n))[1]
        upperBound = upperPath[0].get(i, (1, 1))[0]
        #check that j is within these valid bounds
        for j in range(upperBound, lowerBound + 1):
            row = i - mid
            if A[i-1] == B[j-1]:
                if i == mid + 1:
                    arr[i][j] = 1
                else:
                    arr[i][j] = arr[i-1][j-1]+1
                pointers[row][j] = 2
            else:
                if i == mid + 1:
                    arr[i-1][j] = 0
                if j > lowerPath[0].get(i, (n,n))[0]:
                    arr[i][j] = arr[i][j-1]
                    pointers[row][j] = -1
                elif j == upperBound: 
                    arr[i][j] = arr[i-1][j]
                    pointers[row][j] = 1
                elif arr[i-1][j] >= arr[i][j-1]:
                    arr[i][j] = arr[i-1][j]
                    pointers[row][j] = 1
                else:
                    arr[i][j] = arr[i][j-1]
                    pointers[row][j] = -1

    path = backtrace(m, len(B), mid)
    length = arr[mid + m][n]

    return (path, length)


def backtrace(m, n, mid):
  path = {}

  while m != 0 and n != 0:
    if m + mid not in path:
      path[m + mid] = [n, n]
    else:
      path[m + mid] = [n, path[m + mid][1]]
    if pointers[m][n] == 1:
      n = n - 1
      m = m - 1
    elif pointers[m][n] == -1:
      n = n - 1
    elif pointers[m][n] == 2:
      m = m - 1
  return path


def main():
    if len(sys.argv) != 1:
        sys.exit('Usage: `python LCS.py < input`')
    
    for l in sys.stdin:
        A,B = l.split()
        m = len(A)
        A = A+A

        #Set up paths
        paths = [(0,0) for i in range(m + 1)]
        paths[0] = singleShortestPath(A, B, 0, ({}, 0), ({}, 0))
        paths[m] = ({}, paths[0][1])
        for key in paths[0][0].keys():
            paths[m][0][key + m] = paths[0][0][key]

        findShortestPaths(A, B, paths, 0, m)
        maximum = 0
        for path in paths:
            maximum = max(path[1], maximum)

        print(maximum)

if __name__ == '__main__':
    main()