

class Solution:
    def cuttingRope(self, n: int) -> int:
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
        # 一定要切绳子
        if n <= 3:
            return n-1

        product_dict = {
            1: 1,
            2: 2,
            3: 3,
        }

        def dp(n):
            if n in product_dict:
                return product_dict[n]
            max_product = 0
            for i in range(1, n//2+1):
                max_product = max(max_product, (dp(i)*dp(n-i)))
            product_dict[n] = max_product
            return max_product

        return dp(n)
print(Solution().cuttingRope(10))