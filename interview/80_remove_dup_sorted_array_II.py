class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # If the string is short no need to bother
        if len(nums) < 3:
            return nums.length

        i = 0
        k = 1
        res = 0

        while i < len(nums) and k < len(nums):

            i += 1
            nums[i] = nums[k]
            k += 1

            # Check only if k>1
            if k>1:
                while k < len(nums) and nums[k] == nums[i] and nums[k] == nums[i-1]:
                    k += 1
                    res += 1

        d = len(nums) - res
        print(nums)
        return d


if __name__ == '__main__':
    s = Solution()
    nums =[1,1,1,2,2,2,3]
    print(s.removeDuplicates(nums))
