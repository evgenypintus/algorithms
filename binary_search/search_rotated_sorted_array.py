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
                return mid

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
            return -1


if __name__ == '__main__':

    s= Solution()

    nums = [3,1]
    target = 1

    print(s.search(nums, target))