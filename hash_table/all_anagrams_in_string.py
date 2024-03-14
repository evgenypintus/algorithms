"""
438. Find All Anagrams in a String

Given two strings s and p, return an array of all the start indices of p's anagrams in s.
You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
"""
from itertools import permutations

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(p) > len(s):
            return None
        result = []
        perm = ''.join(sorted(p))

        perm_len = len(perm)

        for k in range(len(s)):
            if (k+perm_len) > len(s):
                break

            str = s[k:perm_len+k]
            find_str = ''.join(sorted(str))
            if find_str == perm:
                result.append(k)

        return result if result else None



if __name__ == '__main__':

    sol= Solution()

    s = "cbaebabacd"
    p = "abc"

    print(sol.findAnagrams(s, p))

