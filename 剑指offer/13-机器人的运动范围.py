class Solution:
    def __init__(self):
        self.possible = None
        self.num = 0

    def movingCount(self, m: int, n: int, k: int) -> int:
        """
        地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，
        它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。
        例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，
        因为3+5+3+8=19。请问该机器人能够到达多少个格子？

        示例 1：
        输入：m = 2, n = 3, k = 1
        输出：3

        示例 2：
        输入：m = 3, n = 1, k = 0
        输出：1
        1 <= n,m <= 100
        0 <= k <= 20
        """

        def dfs(row, column):
            if row < 0 or row >= m or column < 0 or column >= n or self.possible[row][column] != 0:
                return
            elif (row // 10) % 10 + (row // 1) % 10 + (column // 10) % 10 + (column / 1) % 10 > k:
                self.possible[row][column] = False
                return
            else:
                self.possible[row][column] = True
                self.num += 1
                dfs(row + 1, column)
                dfs(row - 1, column)
                dfs(row, column + 1)
                dfs(row, column - 1)
                # 这道题的 DFS 没有在递归调用邻居之后将其从 visit 中移除. 这是因为上道题中一个点可能出现在多条路径中,
                # 所以必须调用完之后从集合移除, 避免之后的路径无法使用该节点; 而这道题只有一个共享的运动范围,
                # 所以一个点如果出现在运动范围内的话, 那么它一定不需要再次被访问了, 直接永久加入 visit 集合中即可

        self.possible = [[0] * n for _ in range(m)]
        dfs(0, 0)

        return self.num


Solution().movingCount(1, 2, 1)
