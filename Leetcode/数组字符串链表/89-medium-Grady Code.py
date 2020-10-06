from typing import List
class Solution:
    """
    The gray code is a binary numeral system where two successive values differ in only one bit.
    Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

    Example 1:
    Input: 2
    Output: [0,1,3,2]
    Explanation:
    00 - 0
    01 - 1
    11 - 3
    10 - 2
    For a given n, a gray code sequence may not be uniquely defined.
    For example, [0,2,3,1] is also a valid gray code sequence.
    00 - 0
    10 - 2
    11 - 3
    01 - 1

    Example 2:
    Input: 0
    Output: [0]
    Explanation: We define the gray code sequence to begin with 0.
                 A gray code sequence of n has size = 2n, which for n = 0 the size is 20 = 1.
                 Therefore, for n = 0 the gray code sequence is [0].
    """
    def grayCode(self, n: int) -> List[int]:
        """
        递归生成码表

        这种方法基于格雷码是反射码的事实，利用递归的如下规则来构造：

        1位格雷码有两个码字
        (n+1)位格雷码中的前2n个码字等于n位格雷码的码字，按顺序书写，加前缀0
        (n+1)位格雷码中的后2n个码字等于n位格雷码的码字，按逆序书写，加前缀1
        n+1位格雷码的集合 = n位格雷码集合(顺序)加前缀0 + n位格雷码集合(逆序)加前缀1
        ————————————————
        版权声明：本文为CSDN博主「负雪明烛」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
        原文链接：https://blog.csdn.net/fuxuemingzhu/java/article/details/80664204
        """
        grays = dict()
        grays[0] = ['0']
        grays[1] = ['0', '1']
        for i in range(2, n + 1):
            n_gray = []
            for pre in grays[i - 1]:
                n_gray.append('0' + pre)
            for pre in grays[i - 1][::-1]:
                n_gray.append('1' + pre)
            grays[i] = n_gray
        return map(lambda x: int(x, 2), grays[n])

