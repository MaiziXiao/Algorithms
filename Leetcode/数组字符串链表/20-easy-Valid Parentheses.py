class Solution:
    """
    Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Note that an empty string is also considered valid.

    Example 1:

    Input: "()"
    Output: true
    Example 2:

    Input: "()[]{}"
    Output: true
    Example 3:

    Input: "(]"
    Output: false
    """
    # Stack 堆栈
    def isValid(self, s: str) -> bool:
      stack = []
      map = {
        "{":"}",
        "[":"]",
        "(":")"
      }
      for x in s:
        if x in map:
          stack.append(map[x])
        else:
          if len(stack)!=0:
            top_element = stack.pop()
            if x != top_element:
              return False
            else:
              continue
          else:
            return False
      return len(stack) == 0

print(Solution().isValid("()"))
