class Solution(object):

    digits = dict(I=1,V=5, X=10, L=50, C=100, D=500, M=1000)

    def is_greater(self, left, right) -> bool:
        """Return True if left is greater that right"""

        if self.translate(left) > self.translate(right):
            return True

        return False

    def translate(self, s) -> int:
        return self.digits[s]

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        i = 0
        while i < len(s):

            # if next symbol is greater than we have to deduct it from sum
            if i+1 != len(s) and self.is_greater(s[i+1], s[i]):
                result = result - self.translate(s[i])
                i += 1
            result += self.translate(s[i])
            i += 1

        return result

if __name__ == '__main__':

    s = Solution()

    # r = s.romanToInt('III')
    # assert r == 3
    #
    # r = s.romanToInt('LVIII')
    # assert r == 58

    r = s.romanToInt('MCMXCIV')
    print(r)



