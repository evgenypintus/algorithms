class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        elements = dict()
        curr_max = 0

        for i in nums:
            if i in elements:
                elements[i] +=1

                if elements[i] > len(nums)/2:
                    return i
            else:
                elements[i] = 1


if __name__ == '__main__':

    s = Solution()

    nums =[3,2,3]

    print(s.majorityElement(nums))

