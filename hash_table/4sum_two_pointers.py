"""
18. 4Sum

Given an array nums of n integers, return an array of all the unique quadruplets
[nums[a], nums[b], nums[c], nums[d]] such that:

    0 <= a, b, c, d < n
    a, b, c, and d are distinct.
    nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.
"""
from collections import defaultdict
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 4:
            return None
        return self.four_sum(nums, target)

    def four_sum(self, nums, target):

        # Initialising the hash map
        hash_map = defaultdict(list)
        result = set()

        # Consider each element
        for i in range(len(nums) - 1):
            for k in range(i + 1, len(nums)):
                sum = nums[i] + nums[k]
                add_value = target - sum
                # If the remaining pair is found in the map we have to find the quadruplets
                pair_list = hash_map.get(add_value)
                if pair_list:
                    #print(sum, add_value, pair_list)
                    for pair in pair_list:
                        if pair[0] != i and pair[0] != k and pair[1] != i and pair[1] != k:
                            res = [nums[pair[0]], nums[pair[1]], nums[i], nums[k]]
                            res.sort()
                            result.add(tuple(res))

                # Add the new pair of indices to the current sum
                hash_map[sum].append([i, k])
        return [list(x) for x in result] if result else None


if __name__ == '__main__':

    s= Solution()

    nums = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
    target = 8

    print(s.four_sum(nums, target))

