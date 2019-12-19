from typing import List


class Solution:
    def __init__(self):
        self.final_list = []
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all
        unique combinations in candidates where the candidate numbers sums to target.
        The same repeated number may be chosen from candidates unlimited number of times.
        Note:
        All numbers (including target) will be positive integers.
        The solution set must not contain duplicate combinations.

        Example 1:
        Input: candidates = [2,3,6,7], target = 7,
        A solution set is:
        [
          [7],
          [2,2,3]
        ]
        """
        # 对数组里面的每个数，用递归的方式相加，每次递归将和sum与target作比较，若相等则加入结果vector，sum>target则舍弃，
        # 并返回false，若sum<target，则继续进行递归。若sum>target，则回溯到上一层，重新以数组中的下一个数开始递归。
        # 第一种sum=target的情况下，在加入结果vector后回溯（此时不应再累加），要将当前一种结果最后加入的元素pop_back()，
        # 并继续对后面的元素进行递归；
        # 第二种sum>target的情况下，则需要将当前结果的最后加入的元素pop_back()，并继续对后面的元素进行递归。
        # 第三种sum<target的情况下，直接以当前数继续递归。
        # 注意元素可以重复，所以下一次递归总是从当前递归元素开始。
        # ————————————————
        # 版权声明：本文为CSDN博主「EbowTang」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
        # 原文链接：https://blog.csdn.net/EbowTang/article/details/51570317

        # Empty list
        if len(candidates) == 0:
            return []
        # 先排序，便于后面剪枝
        candidates.sort()
        path = []
        self._find_path(path, target, candidates, 0)
        return self.final_list

    # Recursion
    def _find_path(self, path, target, candidates, start_index):
        if target == 0:
            self.final_list.append(path.copy())
        else:
            for i in range(start_index, len(candidates)):
                # 剪枝
                # My mistake: if sum(path) + candidates[i] > target:
                if target - candidates[i] < 0:
                    break
                # 没超过target 就把当前值加入路径
                path.append(candidates[i])
                # My mistake: self._find_path(path, target - sum(path), candidates, i)
                self._find_path(path, target - candidates[i], candidates, i)
                path.pop()

print(Solution().combinationSum(candidates = [2,3,6,7], target = 7))
