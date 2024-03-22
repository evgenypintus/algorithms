"""
18. 4Sum

Given an array nums of n integers, return an array of all the unique quadruplets
[nums[a], nums[b], nums[c], nums[d]] such that:

    0 <= a, b, c, d < n
    a, b, c, and d are distinct.
    nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.
"""

from collections import defaultdict, Counter

class Solution(object):

    def __init__(self):
        self.hash_map_count = defaultdict(int)  # Count all elements
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 4:
            return None
        return self.four_sum(nums, target)

    def validate(self, arr):
        arr_dict = Counter(arr)
        for i,k in arr_dict.items():
            val = self.hash_map_count.get(i)
            if val < k:
                return False
        return True

    def four_sum(self, nums, target):

        result_set = set()

        hash_map = {}   # Map for storing sums
        hash_map_passed_sum = {} # Passed pairs
        hash_map_passed_tuple = {} # Passed pairs

        # Consider each element and building a hash map of sums for all unique pairs
        # Also count all pairs
        self.hash_map_count[nums[len(nums) - 1]] += 1
        for i in range(len(nums) - 1):
            self.hash_map_count[nums[i]] +=1

            for j in range(i + 1, len(nums)):
                sum = nums[i] + nums[j]
                sum_array =  hash_map.get(sum)
                if sum_array:
                    if not ([nums[i] , nums[j]] in sum_array):
                        hash_map[sum].append([nums[i] , nums[j]])
                else:
                    hash_map[sum] = [[nums[i], nums[j]]]

        # Looping through all sums
        for sum1 in hash_map:
            add_value = target - sum1

            add_array = hash_map.get(add_value)

            # Search all possible pairs in array if sum1 = add_value
            if add_array:
                for first_part in hash_map[sum1]:
                    for second_part in add_array:
                        final = tuple(sorted(first_part + second_part))
                        if not final in hash_map_passed_tuple:
                            if self.validate(final):
                                # Saving results
                                result_set.add(final)
                            hash_map_passed_tuple[final] = 1

        return [list(x) for x in result_set]



if __name__ == '__main__':

    s= Solution()

    nums = [2,1,0,-1]
    target = 2

    print(s.four_sum(nums, target))

