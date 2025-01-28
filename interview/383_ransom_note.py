from collections import Counter

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        # create a dict of source letters
        from_str = Counter(magazine)

        # check if we can take a letter from source
        for i in ransomNote:
            if i not in from_str:
                return False

            if from_str[i] > 1:
                from_str[i] -=1
            else:
                del(from_str[i])

        return True


if __name__ == '__main__':

    s = Solution()

    r = s.canConstruct("aa", "aab")

    print(r)