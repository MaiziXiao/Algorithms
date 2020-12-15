from typing import List
import collections


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        """
        给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列的长度。转换需遵循如下规则：

        每次转换只能改变一个字母。
        转换过程中的中间单词必须是字典中的单词。
        说明:

        如果不存在这样的转换序列，返回 0。
        所有单词具有相同的长度。
        所有单词只由小写字母组成。
        字典中不存在重复的单词。
        你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
        示例 1:

        输入:
        beginWord = "hit",
        endWord = "cog",
        wordList = ["hot","dot","dog","lot","log","cog"]

        输出: 5

        解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
            返回它的长度 5。
        """
        # 拿到这个题没有什么思路，看了别人解答之后，才猛然发现这个题是走迷宫问题的变形！
        # 也就是说，我们每次变化有26个方向，如果变化之后的位置在wordList中，我们认为这个走法是合规的，最后问能不能走到endWord？
        # 很显然这个问题是BFS的问题，只是把走迷宫问题的4个方向转变成了26个方向，直接BFS会超时，
        # 所以我使用了个visited来保存已经遍历了的字符串，代表已经走过了的位置。代码总体思路很简单，
        # 就是利用队列保存每个遍历的有效的字符串，然后对队列中的每个字符串再次遍历，保存每次遍历的长度即可。
        wordset = set(wordList)
        if endWord not in wordset:
            return 0
        visited = set([beginWord])
        chrs = "abcdefghijklmnopqrstuvwxyz"
        bfs = collections.deque([beginWord])
        res = 1
        while bfs:
            len_bfs = len(bfs)
            for _ in range(len_bfs):
                origin = bfs.popleft()
                for i in range(len(origin)):
                    for c in chrs:
                        transword = origin[:i] + c + origin[i + 1:]
                        # 如果已经visited，肯定比后面广度的路径短
                        if transword not in visited:
                            if transword == endWord:
                                return res + 1
                            elif transword in wordset:
                                bfs.append(transword)
                                visited.add(transword)
            res += 1
        return 0


Solution().findLadders(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log", "cog"])
