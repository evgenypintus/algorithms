"""
438. Find All Anagrams in a String

Given two strings s and p, return an array of all the start indices of p's anagrams in s.
You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
"""
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        arr = []
        sliding = {}
        if len(s) < len(p):
            return None
        if len(s) ==0 or  len(p) == 0:
            return None

        # Build a dictionary with all letters in anagram with their quantity
        anagram = {}
        anagram_len = len(p)

        for i in p:
            if i in anagram:
                anagram[i] += 1
            else:
                anagram[i] = 1
        # Searching through a target string
        # We don't need to go till the end
        for l in range(len(s)):
            if s[l] in sliding:
                sliding[s[l]] += 1
            else:
                sliding[s[l]] = 1

            if l>= anagram_len:
                if sliding[s[l-anagram_len]] == 1:
                    del sliding[s[l-anagram_len]]
                else:
                    sliding[s[l-anagram_len]] -= 1

            if anagram == sliding:
                arr.append(l-anagram_len+1)

        return arr

if __name__ == '__main__':

    sol= Solution()

    s = "abab"
    p = "ab"

    print(sol.findAnagrams(s, p))

