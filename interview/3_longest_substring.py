class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        i=0
        k=0
        cur_str = set()
        l = 0

        while k < len(s):
            letter = s[k]

            if letter in cur_str:
                cur_len = len(cur_str)

                if cur_len > l:
                    l = cur_len

                cur_str.clear()
                i+=1
                k=i
            else:
                cur_str.add(letter)
                k+=1

        if len(cur_str) > l:
            return len(cur_str)
        return l


if __name__ == '__main__':

    s = Solution()

    str = "dvdf"

    print(s.lengthOfLongestSubstring(str))