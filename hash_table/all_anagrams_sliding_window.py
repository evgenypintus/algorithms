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
        sl = len(s)
        pl = len(p)
        dic2 = {}
        for i in p:
            if i in dic2:
                dic2[i] += 1
            else:
                dic2[i] = 1
        #print(dic2)

        arr =[]
        dic1 = {}

        for i in range(sl):
            if s[i] in dic1:
                dic1[s[i]] += 1
            else:
                dic1[s[i]] = 1
            # print(dic1)
            if i >= pl:
                if dic1[s[i-pl]] == 1:
                    # here we are removing the 1st element
                    # after adding 4th element from
                    # the dictionary[window]
                    del dic1[s[i-pl]]
                else:
                    # here we are removing the 1st element
                    # but here we are removing the same element
                    # like: "baeb" --> {b:2, a:1, e:1}
                    # after: "b" | "aeb" --> {b:1, a:1, e:1}
                    dic1[s[i-pl]] -= 1
            if dic1 == dic2:
                # indexing starts from 0 so we have to
                # add 1 to find the actual index
                arr.append(i-pl+1)
        return arr

if __name__ == '__main__':

    sol= Solution()

    s = "cbaebabacd"
    p = "abc"

    print(sol.findAnagrams(s, p))

