class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        def surrounding_count(x, y, board):
            total = 0
            for d_x, d_y in directions:
                if 0 <= x + d_x < len(board) and 0 <= y + d_y < len(board[0]):
                    if abs(board[x+d_x][y+d_y]) == 1:
                        total+=1
            
            return total
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                total_ones = surrounding_count(i, j, board)
                if board[i][j] == 1:
                    if total_ones < 2 or total_ones > 3:
                        board[i][j] = -1
                elif board[i][j] == 0:
                    if total_ones == 3:
                        board[i][j] = 10
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] >= 1:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
        
