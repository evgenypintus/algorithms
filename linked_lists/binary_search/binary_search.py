"""
704. Binary Search

Given an array of integers nums which is sorted in ascending order, and an
integer target, write a function to search target in nums. If target exists,
then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.search_bi(nums, target)

    def search_bi(self,nums, target, left=0, right=None):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if right is None:
            right = len(nums)-1
        mid = (left+right) // 2

        if left <= right:
            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                return self.search_bi(nums, target, left, mid-1)
            else:
                return self.search_bi(nums, target, mid+1, right)
        else:
            return -1