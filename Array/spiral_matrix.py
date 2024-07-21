class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        n = len(matrix)
        m = len(matrix[0])
        l, r = 0, m-1
        t, b = 0, n-1
        a = []
        while t <= b and l <= r:
            for i in range(l, r+1):
                a.append(matrix[t][i])
            t += 1
            for i in range(t, b+1):
                a.append(matrix[i][r]) 
            r -= 1
            if t <= b:
                for i in range(r, l-1, -1):
                    a.append(matrix[b][i])
                b -= 1
            if l <= r:
                for i in range(b, t-1, -1):
                    a.append(matrix[i][l])
                l += 1
        return a
