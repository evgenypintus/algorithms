class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i = 0
        k = 0
        res = 0


        while i < len(nums) and k < len(nums):

            nums[i] = nums[k]
            i += 1
            k += 1

            while k < len(nums) and nums[k] == nums[k-1]:
                k += 1
                res += 1

        d = len(nums) - res
        return d


if __name__ == '__main__':
    s = Solution()
    nums = [0, 1, 2, 2, 3, 3, 4, 4]
    print(s.removeDuplicates(nums))