"""
1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such
that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.two_sum(nums, target)

    def two_sum(self, nums, target):

        # Initialising the hash map
        hash_map = {}
        for i, value in enumerate(nums):
            add_value = target-value
            print(value, add_value, hash_map)
            k = hash_map.get(add_value)
            print(k)
            if k is not None:
                print('Found', i, k)
                return i,k
            else:
                print('Not found, adding', value, i)
                hash_map[value] = i

        return None


if __name__ == '__main__':

    s= Solution()

    nums = [2,7,11,15]
    target = 9

    print(s.two_sum(nums, target))