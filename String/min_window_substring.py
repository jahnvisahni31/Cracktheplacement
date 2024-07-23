class Solution:
    def minWindow(self, s: str, t: str) -> str:
        c = 0
        mi = float('inf')
        si = -1
        fre = defaultdict(int)
        for k in range(len(t)):
            fre[t[k]] += 1
        j = 0
        i = 0
        while j < len(s):
            if fre[s[j]] > 0:
                c += 1
            fre[s[j]] -= 1
            while c == len(t):
                if j-i+1 < mi:
                    mi = j-i+1
                    si = i
                fre[s[i]] += 1
                if fre[s[i]] > 0:
                    c -= 1
                i += 1
            j += 1
        if si == -1:
            return ""
        return s[si:si+mi]
