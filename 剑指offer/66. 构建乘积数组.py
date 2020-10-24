from typing import List

class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        """
        给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，其中 B 中的元素
        B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。

        示例:
        输入: [1,2,3,4,5]
        输出: [120,60,40,30,24]
             [2*3*4*5, 1*3*4*5, 1*2*4*5, 1*2*3*4]
        """
        # https://blog.csdn.net/u013129109/article/details/79622261
        ans = []
        _len = len(a)
        prod = 1
        for i in range(_len):
            ans.append(prod)
            prod *= a[i]
        prod = 1
        for i in range(len(a) - 1, -1, -1):
            ans[i] *= prod
            prod *= a[i]
        return ans
