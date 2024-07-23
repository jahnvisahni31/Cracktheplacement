class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        re, cu , num = [], [], 0
        for w in words:
            if num + len(w) + len(cu) > maxWidth:
                for i in range(maxWidth - num):
                    cu[i% (len(cu) - 1 or 1)] += ' '
                re.append(''.join(cu))
                cu, num = [], 0
            cu += [w]
            num += len(w)
        return re + [' '.join(cu).ljust(maxWidth)]
