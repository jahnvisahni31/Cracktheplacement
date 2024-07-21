class Solution:
    def minDeletions(self, s: str) -> int:
        h = collections.defaultdict(int)
        se = set()
        de = 0
        for c in s:
            h[c] += 1
        for k, va in h.items():
            if va in se:
                while h[k] in se and h[k] > 0:
                    h[k] -= 1
                    de += 1
            se.add(h[k])
        return de
