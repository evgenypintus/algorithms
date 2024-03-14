"""
49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
"""


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = {}
        for s in strs:
            s_s = ''.join(sorted(s))
            if result.get(s_s):
                result[s_s].append(s)
            else:
                result[s_s] = [s]
        return [x for x in result.values()]

if __name__ == '__main__':

    s= Solution()

    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    target = 1

    print(s.groupAnagrams(strs))


