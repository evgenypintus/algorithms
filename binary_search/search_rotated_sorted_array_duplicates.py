"""
81. Search in Rotated Sorted Array II

There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length)
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
 For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums,
or false if it is not in nums.

You must decrease the overall operation steps as much as possible.
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.search_bi_rotated(nums, target)

    def search_bi_rotated(self, row, target, left=0, right=None):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if right is None:
            right = len(row)-1

        mid = (left+right) // 2

        print('mid=', mid, 'left=', left, 'right=', right)
        if left <= right:
            if row[mid] == target:
                return True

            # Check if left part is sorted
            if row[mid] >= row[left]:
                print('left sorted')
                # Target can be in sorted part usual search, strong greater, because row[mid]
                # cannot be equal to target
                if row[mid] > target >= row[left]:
                    print('target in sorted part')
                    return self.search_bi_rotated(row, target, left, mid - 1)
                else:
                    print('target in unsorted part')
                    return self.search_bi_rotated(row, target, mid+1, right)

            # Otherwise right part is sorted
            else:
                print('right sorted')
                # Target can be in sorted part usual search
                if row[mid] < target <= row[right]:
                    print('target in sorted part')
                    return self.search_bi_rotated(row, target, mid + 1, right)
                # Target can be in unsorted part, searching the left part
                else:
                    print('target in unsorted part')
                    return self.search_bi_rotated(row, target, left, mid - 1)
        else:
            return False


if __name__ == '__main__':

    s= Solution()

    nums = [2,5,6,0,0,1,2]
    target = 0

    print(s.search(nums, target))