from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        box = defaultdict(set)



        for row_idx,row in enumerate(board):
            for col_idx,value in enumerate(row):
                if value == ".":
                    continue
                row_box = row_idx//3
                col_box = col_idx//3
                if value in rows[row_idx] or value in cols[col_idx] or value in box[(row_box,col_box)]:
                    return False
                rows[row_idx].add(value)
                cols[col_idx].add(value)
                box[(row_box,col_box)].add(value)
        print(rows)
        print(cols)
        print(box)
        return True