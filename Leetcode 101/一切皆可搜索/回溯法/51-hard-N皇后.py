from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
        """
        # 我们一行一行的放下去，在放的过程中，判断这个位置是否可以放？可以就放，不可以就进行下一个位置，到头了，就回溯到上一行。
        # 放完n个皇后，就输出一组结果。直到结束。
        res, q = [], [-1] * n  # cnt 用计数，q用于已经放的位置，例如q[2]=3 表示第3行的放到了第4个位置
        # k 是放了几个皇后

        def dfs(k, n):
            # n个皇后都放了
            if k == n:
                tmp = []
                for i in range(n):  # 输出一个结果
                    s = ""
                    for j in range(n):
                        s += "Q" if q[i] == j else "."
                    tmp.append(s)
                res.append(tmp)
            else:
                # 这一行每一个位置都试下
                for j in range(n):
                    # K是行数，j是列数
                    if self.place(k, j, q):
                        # 放皇后
                        q[k] = j
                        dfs(k + 1, n)

        dfs(0, n)
        return res

    def place(self, k, j, q):  # 判断该位置是否可以放一个棋子
        for i in range(k):
            # 已经有的子(q[i], i),准备放的位置(j, k)
            if q[i] == j or abs(q[i] - j) == abs(i - k):  # 不同列，不同斜线
                return 0
        return 1


Solution().solveNQueens(4)