from typing import List

# https://www.cnblogs.com/xugenpeng/p/9950007.html


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
        示例 1:

        输入: nums = [1,1,1,2,2,3], k = 2
        输出: [1,2]
        示例 2:

        输入: nums = [1], k = 1
        输出: [1]
        你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
        """
        # 1.拿到题目的时候，如果没有详细看说明的话，一般都会首先想到使用排序算法对元素按照频率由高到低进行排序，
        # 然后取前 k 个元素。但是这样做的时间复杂度是 O(nlogn) 的， 不满足题目要求。虽然不满足题目要求，但是还是将求解程序写一下。
        # 统计元素的频率 O(n)
        # freq_dict = dict()
        # for num in nums:
        #     freq_dict[num] = freq_dict.get(num, 0) + 1

        # # 按照频率进行排序 O(nlog(n))
        # freq_dict_sorted = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)

        # # 取前k个元素返回 O(k)
        # ret = list()
        # for i in range(k):
        #     ret.append(freq_dict_sorted[i][0])
        # return ret

        # 2.桶排序。时间复杂度：O(n)，其中 n 表示数组的长度。空间复杂度：O(n)
        # 统计元素的频率 O(n)
        freq_dict = dict()
        for num in nums:
            freq_dict[num] = freq_dict.get(num, 0) + 1
        # 接着，将数组中的元素按照出现频次进行分组，即出现频次为 i 的元素存放在第 i 个桶。最后，从桶中逆序取出前 k 个元素。 O(n)
        bucket = [[] for _ in range(len(nums) + 1)]
        for key, value in freq_dict.items():
            bucket[value].append(key)

        # 逆序取出前k个元素 O(n)
        ret = list()
        for i in range(len(nums), -1, -1):
            if bucket[i]:
                ret.extend(bucket[i])
            if len(ret) >= k:
                break
        return ret[:k]


Solution().topKFrequent([1, 1, 1, 2, 2, 2, 3], 2)
