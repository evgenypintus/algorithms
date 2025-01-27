class Solution(object):
    keyboard =  {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }

    def parse_digit(self, pos, current_string,  digits, result):

        if pos == len(digits):
            result.append(current_string)
            return

        for letter in self.keyboard[digits[pos]]:
            self.parse_digit(pos+1, current_string+letter, digits, result)

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        result = []

        if len(digits) == 0:
            return result

        self.parse_digit(0, '', digits, result)

        return result


if __name__ == '__main__':

    s = Solution()
    digits = "23"
    r = s.letterCombinations(digits)

    print (r)