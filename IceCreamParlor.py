"""
David Schonberger
Hackerrank.com
Search - Ice Cream Parlor
1/14/2015
"""

T = input()
for j in range(T):
    
    M = input()
    N = input()
    ar = raw_input()
    ar = ar.split(' ')
    ar = [int(t) for t in ar]
    i = 0
    done = False
    while(i < len(ar) and not done):
        if(M - ar[i] in ar and ar.index(M - ar[i]) != i):
            done = True
            minidx = min(i + 1, ar.index(M - ar[i]) + 1)
            maxidx = max(i + 1, ar.index(M - ar[i]) + 1)
            print minidx, maxidx
        i += 1
