import sys
import numpy as np

global arr
global pointers

def findShortestPaths(A,B,p,l,u):
        if u-1<=l:
            return
        mid = (l+u)/2
        p[mid] = singleShortestPath(A,B,mid,p[l], p[u], l, u)
        findShortestPaths(A,B,p,l,mid)
        findShortestPaths(A,B,p,mid,u)
                                

def main():
    if len(sys.argv) != 1:
        sys.exit('Usage: `python CLCSFast.py < input`')
    for l in sys.stdin:
        A,B = l.split()
        arr = np.zeros((len(A)*2+1, len(B)+1), dtype=int)
        pointers = np.zeros((len(A)*2+1, len(B)+1), dtype=int)
        paths = 1
        m = len(A)
        LCS(A,B, arr, pointers, is_First=True)
        #get paths[0], paths[m]
        #findShortestPaths(A,B,paths,0,m)

def LCS(A, B, arr, pointers, is_First=False, mid=0):
        m = len(A)
        n = len(B)
        A = A + A
        for i in range(mid+1, mid+m+m + 1):
            if is_First:
                nVal = n+1
            else:
                #change to bounds as defined by path
                nVal = n+1
            for j in range(1, nVal):
                if A[i - 1] == B[j - 1]:
                    arr[i][j] = arr[i - 1][j - 1] + 1
                    pointers[i][j] = 1
                else:
                    if arr[i - 1][j] > arr[i][j - 1]:
                        arr[i][j] = arr[i - 1][j]
                        pointers[i][j] = -1
                    # getting value from top
                    elif arr[i][j - 1] > arr[i - 1][j]:
                        arr[i][j] = arr[i][j - 1]
                        pointers[i][j] = 2
                    else:  # default get value from the left
                        arr[i][j] = arr[i - 1][j]
                        pointers[i][j] = -1
        print(arr[m + m][n])
        #return backtrace(m, n, 0, pointers)

def backtrace(m, n, mid):
  path ={}

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
                                      


if __name__ == '__main__':
    main()
