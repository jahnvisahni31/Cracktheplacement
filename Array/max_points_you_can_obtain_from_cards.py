n = len(cardPoints)
        l = 0
        r = n-1
        su = sum(cardPoints[:k])
        b = su
        for i in range(k):
            su += cardPoints[r-i] - cardPoints[k-1-i]
            b = max(b, su)
        return b
