from typing import List


class Solution:
    def __init__(self):
        self.final_list = []
        self.path = []

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Given a collection of candidate numbers (candidates) and a target number (target),
        find all unique combinations in candidates where the candidate numbers sums to target.
        Each number in candidates may only be used once in the combination.

        Note:
        All numbers (including target) will be positive integers.
        The solution set must not contain duplicate combinations.
        Example 1:

        Input: candidates = [10,1,2,7,6,1,5], target = 8,
        A solution set is:
        [
          [1, 7],
          [1, 2, 5],
          [2, 6],
          [1, 1, 6]
        ]
        """
        # Empty list
        if len(candidates) == 0:
            return []
        # 先排序，便于后面剪枝
        candidates.sort()
        self._find_path(target, candidates, 0)
        return self.final_list

    # Recursion
    def _find_path(self, target, candidates, start_index):
        if sum(self.path) == target:
            self.final_list.append(self.path.copy())
        else:
            for i in range(start_index, len(candidates)):
                # Conflict 剪枝
                # 超过了target要把这一整个循环给break才能把右边的叶子全剪掉, 不break就会遍历所有子节点
                if sum(self.path) + candidates[i] > target:
                    break
                # start_index < i保证了 [1, 1, 6] 这种情况不会被跳过
                if start_index < i and candidates[i] == candidates[i-1]:
                    continue
                # 没超过target 就把当前值加入路径
                self.path.append(candidates[i])
                print(self.path)
                self._find_path(target, candidates, i+1)
                # 回溯
                self.path.pop()

print(Solution().combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8))