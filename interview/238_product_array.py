class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        prefix = 1
        suffix = 1
        result = [1]*n

        for i in range(len(nums)):
            result[i] *= prefix  # prefix product from one end
            prefix *= nums[i]
            result[-1-i] *= suffix  # suffix product from other end
            suffix *= nums[-1-i]

        return result

if __name__ == '__main__':
    s = Solution()

    nums = [1, 2, 3, 4]

    print(s.productExceptSelf(nums))