class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ri = le = 0
        me = {}
        c = 0
        ma = 0
        ls = -1
        for ri , cu in enumerate(s):
            if cu in me:
                me[cu] += 1
            else:
                me[cu] = 1
            if me[cu] > ma:
                ma = me[cu]
            c += 1
            if c - ma - k <= 0:
                ls = max(ls, ri-le+1)
            while c - ma -k > 0:
                le_ch = s[le]
                if le_ch in me:
                    me[le_ch] -= 1
                    c -= 1
                le += 1
        return ls
