"""
153. Find Minimum in Rotated Sorted Array

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example,
the array nums = [0,1,2,4,5,6,7] might become:

    [4,5,6,7,0,1,2] if it was rotated 4 times.
    [0,1,2,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in
the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.
"""

"""
33. Search in Rotated Sorted Array

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot
index k (1 <= k < nums.length) such that the resulting array is
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target,
return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
"""


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.search_min(nums)

    def search_min(self, row, left=0, right=None):

        if right is None:
            right = len(row)-1

        # if array is sorted return first element
        if row[left] <= row [right]:
            return row[left]

        mid = (left+right) // 2

        print('mid=', mid, 'left=', left, 'right=', right)

        # Check if left part is sorted
        if row[mid] >= row[left]:
            print('left sorted')

            return self.search_min(row, mid+1, right)
        else:
            print('right_sorted')

            return  self.search_min(row, left, mid)


if __name__ == '__main__':

    s= Solution()

    nums = [3,1]

    print(s.findMin(nums))