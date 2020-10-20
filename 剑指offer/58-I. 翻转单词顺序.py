class Solution:
    def reverseWords(self, s: str) -> str:
        """
        输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。为简单起见，
        标点符号和普通字母一样处理。例如输入字符串"I am a student. "，则输出"student. a am I"。
        示例 1：
        输入: "the sky is blue"
        输出: "blue is sky the"

        示例 2：
        输入: "  hello world!  "
        输出: "world! hello"
        解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
        """
        stack = []
        word = ""
        for i in s:
            if i == " ":
                if not word:
                    continue
                stack.append(word)
                word = ""
                continue
            word += i
        if word != "" and word != " ":
            stack.append(word)

        res = ""
        while len(stack) > 0:
            word = stack.pop()
            res += word + " "

        return res[:-1]

        # 大神一行法

        return " ".join(s.split()[::-1])

print(Solution().reverseWords("the sky is blue"))
