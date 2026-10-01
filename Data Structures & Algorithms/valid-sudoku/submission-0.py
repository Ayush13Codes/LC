class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # T: O(9 ^ 2), S: O(9 ^ 2)
        rows = collections.defaultdict(set)  # row no -> set of nums seen in this row
        cols = collections.defaultdict(set)  # col no -> set of nums seen in this col
        sq = collections.defaultdict(set)  # (r / 3, c / 3) -> set of nums seen in this sq

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == ".":
                    continue

                if num in rows[r] or num in cols[c] or num in sq[(r // 3, c // 3)]:
                    return False

                rows[r].add(num)
                cols[c].add(num)
                sq[(r // 3, c // 3)].add(num)
                
        return True
