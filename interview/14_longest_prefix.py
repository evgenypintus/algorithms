class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''

        shortest = min(strs, key=len)
        for i, ch in enumerate(shortest):
            for e in strs:
                if e[i] != ch:
                    return shortest[:i]

        return shortest

if __name__ == '__main__':

    s = Solution()
    strs = ["flower", "flow", "flight"]


    print(s.longestCommonPrefix(strs))