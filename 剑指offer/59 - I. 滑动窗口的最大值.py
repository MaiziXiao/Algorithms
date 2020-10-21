from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        给定一个数组 numss 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。
        """
        # 检查队尾元素，看是不是都满足大于等于当前元素的条件。如果是的话，直接将当前元素入队。否则，将队尾元素逐个出队、直到队尾元素大于等于当前元素为止。（这一步是为了维持队列的递减性：
        # 确保队头元素是当前滑动窗口的最大值。这样我们每次取最大值时，直接取队头元素即可。）将当前元素入队检查队头元素，
        # 看队头元素是否已经被排除在滑动窗口的范围之外了。如果是，则将队头元素出队。（这一步是维持队列的有效性：确保队列里所有的元素都在滑动窗口圈定的范围以内。）
        # 排除掉滑动窗口还没有初始化完成、第一个最大值还没有出现的特殊情况。
        # 作者：前端森林
        # 链接：https://juejin.im/post/6844904183007543310

        # 递减数列
        # 如果数组 nums 不存在，则返回 []
        if not nums:
            return []
        # 如果滑动窗口的大小大于数组的大小，或者 k 小于 0，则返回 []
        if k > len(nums) or k <1:
            return []

        # 如果滑动窗口的大小为 1 ，则直接返回原始数组
        if k == 1:
            return nums

        # 存放最大值，次大值的数组，和存放输出结果数组的初始化
        temp = [0]
        res = []

        # 对于数组中每一个元素进行判断
        for i in range(len(nums)):
            # 判断第 i 个元素是否可以加入 temp 中, 如果比当前最大的元素还要大，清空 temp 并把该元素放入数组
            # 首先判断当前最大的元素是否过期
            if i - temp[0] > k-1:
                temp.pop(0)
            # 将第 i 个元素与 temp 中的值比较，将小于 i 的值都弹出
            while len(temp)>0 and nums[i] >= nums[temp[-1]]:
                temp.pop()
            temp.append(i)
            # 只有经过一个完整的窗口才保存当前的最大值
            if i >= k-1:
                res.append(nums[temp [0]])
        return res

print(Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))