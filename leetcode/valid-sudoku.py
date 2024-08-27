"""
LC: https://leetcode.com/problems/valid-sudoku

Approach:
- note that the problem is to find if the board is just valid, NOT solvable
- so, the only thing we need to ensure is that there are NO duplicates in any:
    * row
    * column
    * sub-box

- the trick is to view each sub-box in a 9x9 board as one index in a 3x3 board

    ...   ...   ...
    0,0   0,1   0,2
    ...   ...   ...

    ...   ...   ...
    1,0   1,1   1,2
    ...   ...   ...

    ...   ...   ...
    2,0   2,1   2,2
    ...   ...   ...

- then, for each cell, after checking for duplicates in its row group and column group:
    * find its sub-box and check for duplicates
    * TRICK to finding the sub-box is [row//3, column//3]

Time complexity: O(1)
- since the board's size is fixed, which is 9x9

Space complexity: O(1)
- since the board's size is fixed, the sizes of the groups for rows, cols, and sub-boxes will remain fixed

Note:
- the "trick" is essentially a way to map any cell in the 9x9 Sudoku grid to its corresponding sub-box in a 3x3 grid of sub-boxes.
- the operation r // 3 and c // 3 effectively reduces the 9x9 grid into a 3x3 grid,
- where each cell in this smaller grid represents a sub-box in the original Sudoku board. 
"""

from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # track duplicates in each row, column, and sub-box
        rows = defaultdict(set)
        cols = defaultdict(set)
        sub_box = defaultdict(set)

        # iterate over each row
        for r in range(9):
            # iterate over each column in this row
            for c in range(9):
                # this is the number we're evaluating
                num = board[r][c]
                # cell is NOT filled, so ignore
                if num == ".":
                    continue

                # check if the number is duplicate within its row, column, or sub-box
                if num in rows[r] or num in cols[c] or num in sub_box[(r // 3, c // 3)]:
                    return False

                # add number to its appropriate row, col, and sub-box
                rows[r].add(num)
                cols[c].add(num)
                sub_box[(r // 3, c // 3)].add(num)

        # reached here when NO duplicates are found, so the board is valid
        return True
