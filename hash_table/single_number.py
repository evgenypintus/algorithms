"""
136. Single Number

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.search(nums)

    def search(self, nums):
        result = {}
        for i in nums:
            print(result)
            if result.get(i):
                print(i, 'exist, removing')
                del result[i]
                print(result)
            else:
                result[i] = 1
        for i in result.keys():
            return i

if __name__ == '__main__':

    s= Solution()

    nums = [4,1,2,1,2]

    print(s.search(nums))