from math import sqrt
from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        """
        输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
        序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。
        """
        # 譬如说如果有两个连续的数之和等于target，那么相差为1， (target - 1) % 2 == 0， 且数组一定是从(target - 1) / 2
        # 开始的，数组的元素就是2个；如果是3个连续的数组，那么三个数之间相差为1、2，(target - 1 - 2) % 3 == 0，且数组一定是从(target - 1 - 2) / 3
        # 开始的，数组元素是3个，依次类推，但是注意target必须是大于0的数，且res需要倒序。
        result = []
        #  设首项是x，末项就是x+len, (2x+len)*len = 2*target,
        #  因为x是正整数,2x>0，所以len^2<2*target, len < sqrt(2*target),
        for i in range(2, int(sqrt(2*target))):
            tmp = sum([k for k in range(i)])
            if (target-tmp) % i == 0:
                a = (target-tmp) // i
                if a > 0:
                    tmp_list = [x for x in range(a, a+i)]
                    result.insert(0, tmp_list)
        return result

        # 滑动窗口
        res = []
        l = 1
        r = 2
        while l < r:
            a = []
            sum = (l + r) * (r - l + 1) / 2
            if sum < target:
                r += 1
            elif sum > target:
                l += 1
            else:
                for i in range(l, r + 1):
                    a.append(i)
                res.append(a)
                l += 1
                r += 1
        return res
Solution().findContinuousSequence(15)