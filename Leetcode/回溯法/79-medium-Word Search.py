from typing import List
class Solution:
    """
    Given a 2D board and a word, find if the word exists in the grid.
    The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those
    horizontally or vertically neighboring. The same letter cell may not be used more than once.

    Example:
    board =
    [
      ['A','B','C','E'],
      ['S','F','C','S'],
      ['A','D','E','E']
    ]

    Given word = "ABCCED", return true.
    Given word = "SEE", return true.
    Given word = "ABCB", return false.
    """
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Own solution
        # m = len(board)
        # n = len(board[0])
        # letter_list = []
        # for i in word:
        #     letter_list.append(i)
        # self.flag = False
        #
        # def find_path(curr_i, curr_j, word_letter_index):
        #     # 跳出递归!
        #     if self.flag == True:
        #         return
        #     # 已经到最后一个字母并且match
        #     print(curr_i, curr_j, word_letter_index)
        #     print(board[curr_i][curr_j] == letter_list[word_letter_index], word_letter_index == len(letter_list)-1)
        #     if (board[curr_i][curr_j] == letter_list[word_letter_index]) and (word_letter_index == len(letter_list)-1):
        #         self.flag = True
        #         return
        #     if board[curr_i][curr_j] == letter_list[word_letter_index]:
        #         # 用过了就赋值个0
        #         board[curr_i][curr_j] = 0
        #         # 向左
        #         if curr_j > 0:
        #             find_path(curr_i, curr_j-1, word_letter_index+1)
        #         # 向右
        #         if curr_j < n-1:
        #             find_path(curr_i, curr_j+1, word_letter_index+1)
        #         # 向下
        #         if curr_i < m-1:
        #             find_path(curr_i+1, curr_j, word_letter_index+1)
        #         # 向上
        #         if curr_i > 0:
        #             find_path(curr_i-1, curr_j, word_letter_index+1)
        #         # 没跳出循环把原始值再重新赋值回去
        #         board[curr_i][curr_j] = word[word_letter_index]
        #
        # for i in range(m):
        #     for j in range(n):
        #         find_path(i, j, 0)
        #         if self.flag:
        #             return True
        # return self.flag

        # Github solution:https://github.com/azl397985856/leetcode/blob/master/problems/79.word-search-en.md
        m = len(board)
        n = len(board[0])

        def dfs(board, r, c, word, index):
            print(r, c, index)
            if index == len(word):
                return True
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[index]:
                return False
            board[r][c] = '*'
            res = dfs(board, r - 1, c, word, index + 1) \
                  or dfs(board, r + 1, c, word, index + 1) \
                  or dfs(board, r, c - 1,word,index + 1) \
                  or dfs(board, r, c + 1, word, index + 1)
            board[r][c] = word[index]
            return res

        for r in range(m):
            for c in range(n):
                if dfs(board, r, c, word, 0):
                    return True

print(Solution().exist( [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], "SEE"))