class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        square = defaultdict(set) # Created hashsets for each condition 
        
        for i in range(9):
            for j in range(9):
                curr = board[i][j]
                if(curr == "."):
                    continue 
                # Check now for conditionals 
                if( curr in rows[i] 
                    or curr in cols[j]
                    or curr in square[i//3 , j //3]):
                    return False
                rows[i].add(curr)
                cols[j].add(curr)
                square[i//3 , j//3].add(curr) # breaks up the 3x3 matrix 
        return True
