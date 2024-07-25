
class Solution:
    def isValid(self, i, j, row, col, mat):
        if i >= 0 and i < row and j >= 0 and j < col and mat[i][j] == 'O':
            return True
        return False    
        
    def convertXToO(self, i, j, row, col, mat, dp):
        dp[i][j] = 'O'
        mat[i][j] = 'X'
        ptr_x = [0, 0, -1, 1]
        ptr_y = [1, -1, 0, 0]
        for x in range(4):
            new_i = i + ptr_x[x]
            new_j = j + ptr_y[x]
            if self.isValid(new_i, new_j, row, col, mat):
                self.convertXToO(new_i, new_j, row, col, mat, dp)
    def fill(self, n, m, mat):
        # code here
        dp = [['X' for i in range(m)] for i in range(n)]
        
        for i in range(0, n):
            if mat[i][0] == 'O':
                self.convertXToO(i, 0, n, m, mat, dp)
            if mat[i][m-1] == 'O':
                self.convertXToO(i, m-1, n, m, mat, dp)
        
        for j in range(0, m):
            if mat[0][j] == 'O':
                self.convertXToO(0, j, n, m, mat, dp)
            if mat[n-1][j] == 'O':
                self.convertXToO(n-1, j, n, m, mat, dp)
        
        return dp
