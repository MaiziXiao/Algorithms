from typing import List

class Solution:
    """
    Given an array of strings, group anagrams together.

    Example:
    Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
    Output:
    [
      ["ate","eat","tea"],
      ["nat","tan"],
      ["bat"]
    ]
    Note:

    All inputs will be in lowercase.
    The order of your output does not matter.
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}

        for word in strs:
            # sorted("ate") = ["a","e","t"]
            # "".join(sorted("ate"))="aet"
            word_sort = "".join(sorted(word))
            if word_sort not in dict.keys():
                dict[word_sort] = [word]
            else:
                dict[word_sort].append(word)

        return dict.values()


Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])