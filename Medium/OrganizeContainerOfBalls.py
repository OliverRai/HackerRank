import sys
from collections import Counter


q = int(input().strip())
for a0 in range(q):
    n = int(input().strip())
    M = []
    for M_i in range(n):
       M_t = [int(M_temp) for M_temp in input().strip().split(' ')]
       M.append(M_t)
    rows = Counter()
    cols = Counter()
    for i in range(n):
        rows[sum(M[i])] += 1
        tmp = 0
        for row in M:
            tmp += row[i]
        cols[tmp] += 1
    print("Possible" if rows == cols else "Impossible")
