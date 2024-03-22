"""
456. 132 Pattern

Given an array of n integers nums, a 132 pattern is a subsequence of three
integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.
"""
class Stack():
    def __init__(self):
        self.stack = []
        self.depth = 0
        self.last_number = None

    def push(self, num):
        self.stack.append(num)
        self.depth += 1
        self.last_number = self.stack[0]

    def pop(self):
        self.last_number = self.stack.pop(0)
        self.depth -= 1
        return self.last_number


class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = Stack()
        for i in nums:
            print(s.stack)
            if s.depth == 0:
                s.push(i)
                continue

            if s.depth == 1:
                if i < s.last_number:
                    s.pop()
                s.push(i)
                continue

            if s.depth == 2:
                print('s', s.stack, s.stack[s.depth-1], i, s.last_number)
                if s.last_number < i < s.stack[s.depth-1]:
                    return True
                else:
                    s.pop()
                    if i < s.last_number:
                        s.pop()
                    s.push(i)
        return False


if __name__ == '__main__':

    s= Solution()

    nums = [3,1,4,2]

    print(s.find132pattern(nums))