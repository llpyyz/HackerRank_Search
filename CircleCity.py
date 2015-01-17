import math
"""
David Schonberger
Hackerrank.com
Search - Circle City
1/14/2015
"""

def is_square(n):
    if(n == 0):
        return False
    elif(n == 1):
        return True
    else:
        i = 1
        while(i ** 2 < n):
            i += 1
        if(i ** 2 == n):
            return True
        else:
            return False

eps = 0.00000001
T = input()
for i in range(T):
    x = raw_input()
    x = x.split(' ')
    radius_sq = int(x[0])
    k = int(x[1])
    min_x = int(math.floor((math.sqrt(radius_sq/2.0))))
    max_x = int(math.floor(math.sqrt(radius_sq)))
    count = 0
    if(is_square(radius_sq) or is_square(radius_sq/2.0)):
        count += 4
    res1 = [math.sqrt(radius_sq - i ** 2) for i in range(min_x + 1, max_x + 1) if (radius_sq - i ** 2) > 0]
    res2 = sum([min(abs(elt - math.floor(elt)), abs(elt - math.ceil(elt))) <= eps for elt in res1])    
    count += 8 * res2
    if(k >= count):
        print 'possible'
    else:
        print 'impossible'
