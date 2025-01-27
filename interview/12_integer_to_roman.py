class Solution(object):

    letters = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}


    def translate(self, num, power):

        # three cases:
        # num < 4 - return just so many letter as num value
        # num > 5 < 9 return 5 +  so many letter as num value - 5
        s = ''
        if num < 4 or (5 < num < 9):
            if 5 < num < 9:
                s = self.letters[power*5]
                num = num - 5
            return s + ''.join([self.letters[power] for _ in range(num)])

        if num == 5:
            return self.letters[power*5]

        if num == 4:
            return self.letters[power] + self.letters[power*5]

        if num == 9:
            return self.letters[power] + self.letters[power*10]


    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = ''
        power = 1
        while num != 0:
            left = num%10
            result = self.translate(left, power) + result

            num = int(num/10)
            power = power * 10

        return result

if __name__ == '__main__':

    s = Solution()

    # r = s.romanToInt('III')
    # assert r == 3
    #
    # r = s.romanToInt('LVIII')
    # assert r == 58

    r = s.intToRoman(3749)
    print(r)



