from typing import List
import collections


class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        """
        在给定的二维二进制数组 A 中，存在两座岛。（岛是由四面相连的 1 形成的一个最大组。）

        现在，我们可以将 0 变为 1，以使两座岛连接起来，变成一座岛。
        返回必须翻转的 0 的最小数目。（可以保证答案至少是 1。）


        示例 1：
        输入：[[0,1],
              [1,0]]
        输出：1

        示例 2：
        输入：[[0,1,0],
              [0,0,0],
              [0,0,1]]
        输出：2

        示例 3：
        输入：[[1,1,1,1,1],
              [1,0,0,0,1],
              [1,0,1,0,1],
              [1,0,0,0,1],
              [1,1,1,1,1]]
        输出：1
        """

        # 首先用DFS来确定其中一个岛，把这个岛所有的1变成了2，这么做的目的是和另一个岛作为区分。
        # 需要注意的是把找到的这个岛的每个位置都添加到队列里面，我们会用这个队列去做BFS.

        # 找出了岛之后，使用BFS，来找出这个岛离1最近的距离是多少。每次循环是相当于走了一步，把所有走了一步仍然是水路的位置设置成2，
        # 并放到队列里；如果找到了1，就可以直接结束了，因为我们的BFS没走一步会向前走一些，第一次寻找到的就是最近的距离；
        # 如果找到的是2，那说明这个位置已经遍历过了，直接不要管了。
        M, N = len(A), len(A[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = [[0] * N for _ in range(M)]
        hasfind = False
        que = collections.deque()

        def dfs(self, A, i, j, visited, que):
            if visited[i][j]:
                return
            visited[i][j] = 1
            M, N = len(A), len(A[0])
            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            if A[i][j] == 1:
                que.append((i, j))
                A[i][j] = 2
                for d in dirs:
                    x, y = i + d[0], j + d[1]
                    if 0 <= x < M and 0 <= y < N:
                        self.dfs(A, x, y, visited, que)

        # 找第一个小岛
        for i in range(M):
            if hasfind:
                break
            for j in range(N):
                if A[i][j] == 1:
                    self.dfs(A, i, j, visited, que)
                    # 有第一个1以后小岛已经找到了，设置True可以防止浪费时间
                    hasfind = True
                    break
        # 广度搜索
        step = 0
        while que:
            size = len(que)
            for _ in range(size):
                i, j = que.popleft()
                # 广度左右上下
                for d in dirs:
                    x, y = i + d[0], j + d[1]
                    if 0 <= x < M and 0 <= y < N:
                        if A[x][y] == 1:
                            return step
                        # 如果是水
                        elif A[x][y] == 0:
                            A[x][y] = 2
                            que.append((x, y))
            step += 1
        return -1
