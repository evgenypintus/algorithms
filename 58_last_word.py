class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        words = s.split(' ')

        for w in words[::-1]:
            if w !='':
                return len(w)

        return ''