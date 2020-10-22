from typing import List

class Solution:
    def twoSum(self, n: int) -> List[float]:
        num_possible_dict = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1}
        if n == 1:
            return [1/6 for _ in range(6)]

        x = 2
        while x <= n:
            temp_dict = {}
            for i in range(x, 6*x+1):
                temp = 0
                for j in range(i-6, i):
                    if j < x-1 or j > (x-1)*6:
                        continue
                    else:
                        temp += num_possible_dict[j]
                temp_dict[i] = temp
            num_possible_dict = temp_dict
            x += 1

        num = sum(num_possible_dict.values())
        return [x/num for x in num_possible_dict.values()]

Solution().twoSum(2)