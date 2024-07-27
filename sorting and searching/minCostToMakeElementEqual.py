def minCostToMakeElementEqual(a):
    l = len(a)
    if (l%2 == 1):
        y = a[l//2]
    else:
        y = (a[l//2] + a[(l-2)//2])//2
    s = 0
    for i in range(l):
        s += abs(a[i]-y)
    return s
