class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        comb = []
        exp = 2 * n
        def appe(cur, ape, ope, clo):
            if len(cur)+1 == exp:
                comb.append(cur+ape)
                return
            if ope > 0:
                appe(cur+ape, '(', ope-1, clo)
            if clo - ope > 0:
                appe(cur+ape, ')', ope, clo-1)
        appe('', '(', n-1,n)
        return comb
