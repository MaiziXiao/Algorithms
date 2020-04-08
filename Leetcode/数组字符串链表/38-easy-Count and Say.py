class Solution:
    """
    The count-and-say sequence is the sequence of integers with the first five terms as following:

    1.     1
    2.     11
    3.     21
    4.     1211
    5.     111221
    1 is read off as "one 1" or 11.
    11 is read off as "two 1s" or 21.
    21 is read off as "one 2, then one 1" or 1211.

    Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence. You can do so recursively, in other words from the previous member read off the digits, counting the number of digits in groups of the same digit.

    Note: Each term of the sequence of integers will be represented as a string.



    Example 1:

    Input: 1
    Output: "1"
    Explanation: This is the base case.
    """
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        sequence = "1"
        for i in range(1, n):
            tmp = ""
            cur = sequence[0]
            cur_count = 0
            for i in range(len(sequence)):
                if sequence[i] == cur:
                    cur_count += 1
                # 不一样的时候加 "{cur_count}{cur}" to tmp
                else:
                    tmp += str(cur_count)
                    tmp += str(cur)
                    cur = sequence[i]
                    cur_count = 1

                # 当sequence被读完的时候
                if i == len(sequence)-1:
                    tmp += str(cur_count)
                    tmp += str(cur)
            # print(sequence)
            sequence = tmp
        return sequence

print(Solution().countAndSay(2))