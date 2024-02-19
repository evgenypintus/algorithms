"""
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input
string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        for i in s:
            if i in ['(', '[', '{']:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                else:
                    p = stack.pop()
                    if (i==')' and p != '(') or (i==']' and p != '[') or (i=='}' and p != '{'):
                        return False
        if len(stack) == 0:
            return True
        return False



if __name__ == '__main__':

    s = Solution()
    string = '(()[[]]{})'

    print(s.isValid(string))