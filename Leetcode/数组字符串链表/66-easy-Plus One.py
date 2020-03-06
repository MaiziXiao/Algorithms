from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 如果要进位
        i = len(digits)-1
        while i >= 0:
            if digits[i] + 1 != 10:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
                if i == 0:
                    digits.insert(0, 1)
            i -= 1
        return  digits


print(Solution().plusOne([9]))