class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        pr = strs[0]
        ne = -1
        for j in range(1, n):
            w = strs[j]
            for i in range(min(len(pr), len(w))):
                if w[i] != pr[i]:
                    ne = i
                    break
            if ne != -1:
                pr = pr[:ne]
            elif len(pr) > len(w):
                pr = w
        return pr
