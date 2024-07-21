class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backta(board,i,j,index):
            if index == len(word):
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[index]:
                return False
            c = board[i][j]
            board[i][j] = "#"
            fo = backta(board, i+1, j, index+1) or backta(board, i-1, j, index+1) or backta(board, i, j+1, index+1) or backta(board, i, j-1, index+1)
            board[i][j] = c
            return fo    
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backta(board,i,j, 0):
                    return True
        return False
