class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        i = 0
        k = 0
        res = 0


        while i < len(nums) and k < len(nums):

            while k < len(nums) and nums[k] == val:
                k += 1
                res += 1

            if k != len(nums):
                nums[i] = nums[k]
                i +=1
                k += 1

        print(nums)
        return len(nums) - res

if __name__ == '__main__':

    s = Solution()
    nums = [0,1,2,2,3,0,4,2]
    val = 2

    print(s.removeElement(nums, val))


