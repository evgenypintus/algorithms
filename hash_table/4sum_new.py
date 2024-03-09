"""
18. 4Sum

Given an array nums of n integers, return an array of all the unique quadruplets
[nums[a], nums[b], nums[c], nums[d]] such that:

    0 <= a, b, c, d < n
    a, b, c, and d are distinct.
    nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.
"""

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 4:
            return None
        return self.get_sum(nums, target)

    def build_first_part(self, nums):

        # Initialising the hash map
        hash_map = {}
        for i in range(len(nums) - 1):
            for k in range(i + 1, len(nums)):

                sum = nums[i] + nums[k]
                # If the sum doesn't exist then update with the new pairs
                if sum not in hash_map:
                    hash_map[sum] = [[i,k]]
                # Otherwise, add the new pair of indices to the current sum
                else:
                    hash_map[sum].append([i,k])
        return hash_map

    def get_sum(self, nums, target):

        result = set()
        first_part = self.build_first_part(nums)
        for sum, indices in first_part.items():
            add_value = target - sum
            pair_list = first_part.get(add_value)
            if pair_list:
                for pair in pair_list:
                    for index in indices:
                        if pair[0] != index[0] and pair[0] != index[1] and pair[1] != index[0] and pair[1] != index[1]:
                            res = [nums[pair[0]], nums[pair[1]], nums[index[0]], nums[index[1]]]
                            res.sort()
                            result.add(tuple(res))
        return [list(x) for x in result] if result else None

if __name__ == '__main__':

    s= Solution()

    nums = [2,2,2,2,2]
    target = 8

    print(s.fourSum(nums, target))