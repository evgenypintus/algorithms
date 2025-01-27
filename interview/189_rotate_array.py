class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        res = []
        length = len(nums)

        current = 0
        next = (length - k) % length
        next_value = nums[0]


        for i in range(length):
            a = nums[next]
            nums[next] = next_value
            next_value = a
            next = (next+k) % length

if __name__ == '__main__':

    s = Solution()
    nums = [-1,-100,3,99, 5]
    k = 2

    s.rotate(nums, k)
    print(nums)