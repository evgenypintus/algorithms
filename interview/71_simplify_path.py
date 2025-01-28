class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []

        res = ''

        dirs = path.rstrip('/').split('/')
        dirs = [x for x in dirs if x != '']

        for d in dirs:

            if d == '.':
                continue

            # pop the next level
            if d == '..':
                if len(stack) !=0:
                    next_dir = stack.pop()
                continue

            stack.append(d)


        return '/'+'/'.join(stack)

if __name__ == '__main__':

    s = Solution()

    path = '/home//user/Documents/../Pictures'

    print(s.simplifyPath(path))
