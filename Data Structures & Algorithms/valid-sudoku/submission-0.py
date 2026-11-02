class Solution:
    def isValid(self,hashes_list):
        return len(set(hashes_list)) == len(hashes_list)

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_hashes = dict()
        col_hashes = dict()
        boxes_hashes = dict()
        valid = True
        for i in range(len(board)):
            row = i 
            col_length = len(board[i])
            for j in range(col_length):
                col = j
                if(board[row][col]=='.'):
                    continue
                if(row not in row_hashes):
                    row_hashes[row] = list()
                if(col not in col_hashes):
                    col_hashes[col] = list()
                row_hashes[row].append(board[row][col])
                col_hashes[col].append(board[row][col])
                box_index = 3*(row//3) + (col//3)
                if box_index not in boxes_hashes:
                    boxes_hashes[box_index]= list()
                boxes_hashes[box_index].append(board[row][col])
                valid = self.isValid(row_hashes[row]) and self.isValid(col_hashes[col]) and self.isValid(boxes_hashes[box_index])
                if not valid:
                    return False
        return valid
            
            