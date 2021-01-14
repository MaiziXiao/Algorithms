class Solution:
    def cuttingRope(self, length: int) -> int:
        """
        给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m-1] 。
        请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

        示例 1：
        输入: 2
        输出: 1
        解释: 2 = 1 + 1, 1 × 1 = 1

        示例2:
        输入: 10
        输出: 36
        解释: 10 = 3 + 3 + 4, 3 ×3 ×4 = 36

        提示：
        2 <= n <= 58
        """
        # df[n]把长度为n的绳子切成若干段后乘积最大值
        # df[n] = max(df[i] * df[n-i]) i的取值是1到n//2+1
        # 一定要切绳子

        if length < 2:
            return 0

        if length == 2:
            return 1

        if length == 3:
            return 2

        products = [0 for _ in range(length + 1)]
        # 作废
        products[0] = 0
        # 切割后两部分绳子中，长度为1的那部分最大乘积是1
        products[1] = 1
        # 切割后两部分绳子中，长度为2的那部分，不再切割乘积是2, 因为再切割后会变成1×1=1
        products[2] = 2
        # 切割后两部分绳子中，长度为3的那部分，不再切割乘积是3, 因为再切割后会变成1×2=2
        products[3] = 3

        for i in range(4, length + 1):
            for j in range(1, i // 2 + 1):
                product = products[j] * products[i - j]
                if product > products[i]:
                    products[i] = product
        return products[length]


print(Solution().cuttingRope(10))