class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(' ')
        res = ''
        for w in words[::-1]:
            if w != '':
                res += w +' '

        return res.strip()

if __name__ == '__main__':

    s = Solution()

    string = "   the   sky is blue   "

    print(s.reverseWords(string))