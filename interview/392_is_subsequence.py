class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) == 0:
            return True

        k = 0 # index in s - subseq str

        # scan source string
        for i in range(len(t)):

            # Found match move k
            if t[i] == s[k]:
                # Found all letters
                if k==len(s) - 1:
                    return True
                k+=1

        return False

if __name__ == '__main__':

    sol = Solution()

    s = "abc"
    t = "ahbgdc"
    r = sol.isSubsequence(s, t)

    print(r)