class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        n = len(adjacentPairs)
        ha = {}
        on = []
        an = [0] * (n+1)
        for i in range(n):
            a, b = adjacentPairs[i][0], adjacentPairs[i][1]
            if a not in ha:
                ha[a] = [b]
            else:
                ha[a] += [b]
            if b not in ha:
                ha[b] = [a]
            else:
                ha[b] += [a]
        for k in ha.keys():
            if len(ha[k]) == 1:
                on.append(k)
            if len(on) == 2:
                break
        an[0], an[n] = on[0] , on[1]
        pr = on[0]
        an[1] = ha[on[0]][0]
        for i in range(1, n-1):
            x,y = ha[an[i]][0], ha[an[i]][1]
            if x != pr:
                an[i+1] = x
            else:
                an[i+1] = y
            pr = an[i]
        return an
