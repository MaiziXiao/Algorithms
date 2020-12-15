from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        给定一个二维网格和一个单词，找出该单词是否存在于网格中。

        单词必须按照字母顺序，通过相邻的单元格内的字母构成，
        其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

        示例:

        board =
        [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
        ]

        给定 word = "ABCCED", 返回 true
        给定 word = "SEE", 返回 true
        给定 word = "ABCB", 返回 false
        """

        self.found = False

        def dfs(m, n, visited, left_string):
            visited[m][n] = True
            if board[m][n] != left_string[0]:
                return
            if board[m][n] == left_string:
                self.found = True
                return
            for move in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                new_m, new_n = m + move[0], n + move[1]
                if 0 <= new_m < len(board) and 0 <= new_n < len(board[0]) and visited[new_m][new_n] is False:
                    dfs(new_m, new_n, visited, left_string[1:])
                    if self.found:
                        return
                    visited[new_m][new_n] = False

        for i in range(len(board)):
            for j in range(len(board[0])):
                visited = [[False] * len(board[0]) for _ in range(len(board))]
                dfs(i, j, visited, word)
                if self.found:
                    return True
        return False


Solution().exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED")
