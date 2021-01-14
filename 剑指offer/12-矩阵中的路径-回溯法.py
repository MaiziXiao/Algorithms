from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
        路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。
        如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。

        [["a","b","c","e"],
        ["s","f","c","s"],
        ["a","d","e","e"]]

        但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。

        示例 1：
        输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
        输出：true

        示例 2：
        输入：board = [["a","b"],["c","d"]], word = "abcd"
        输出：false
        """
        m = len(board)
        n = len(board[0])

        def search(row, column, left_word, visited):
            if not left_word:
                return True
            if (
                row < 0
                or row >= m
                or column < 0
                or column >= n
                or visited[row][column]
                or board[row][column] != left_word[0]
            ):
                return False
            visited[row][column] = True
            # Or 的4种情况，如果成功了，返回true. 如果不成功，visited状态会在递归中被重置成False
            if (
                search(row, column - 1, left_word[1:], visited)
                or search(row, column + 1, left_word[1:], visited)
                or search(row - 1, column, left_word[1:], visited)
                or search(row + 1, column, left_word[1:], visited)
            ):
                return True
            # 回溯要把状态返回原始
            visited[row][column] = False
            return False

        visited = [[False] * len(board[0]) for _ in range(len(board))]
        for i in range(m):
            for j in range(n):
                if search(i, j, word, visited):
                    return True
        return False

        # def exist(self, board, word):
        #     visited = [[False] * len(board[0]) for _ in range(len(board))]
        #     for i in range(len(board)):
        #         for j in range(len(board[0])):
        #             if self.dfs(i, j, board, visited, word, 0):
        #                 return True
        #     return False
        #
        # def dfs(self, i, j, board, visited, word, index):
        #     if index >= len(word):
        #         return True
        #     if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or visited[i][j] or board[i][j] != word[index]:
        #         return False
        #     visited[i][j] = True
        #     if self.dfs(i, j + 1, board, visited, word, index + 1)\
        #             or self.dfs(i, j - 1, board, visited, word, index + 1) \
        #             or self.dfs(i + 1, j, board, visited, word, index + 1) \
        #             or self.dfs(i - 1, j, board, visited, word, index + 1):
        #         return True
        #     visited[i][j] = False
        #     return False
