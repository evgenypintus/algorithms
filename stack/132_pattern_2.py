"""
456. 132 Pattern

Given an array of n integers nums, a 132 pattern is a subsequence of three
integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.
"""
class Solution(object):

    def find132pattern(self, nums):
        curmin = nums[0]
        st = []
        for i in range(1, len(nums)):

            while st and nums[i] >= st[-1][1]:
                st.pop()

            if st and st[-1][0] < nums[i]:
                return True

            st.append((curmin, nums[i]))
            curmin = min(curmin, nums[i])
        return False

if __name__ == '__main__':

    s= Solution()

    nums = [3,5,0,3,4]

    print(s.find132pattern(nums))