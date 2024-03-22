"""
480. Sliding Window Median

The median is the middle value in an ordered integer list. If the size of the list is even,
there is no middle value. So the median is the mean of the two middle values.

    For examples, if arr = [2,3,4], the median is 3.
    For examples, if arr = [1,2,3,4], the median is (2 + 3) / 2 = 2.5.

You are given an integer array nums and an integer k. There is a sliding window of size k
 which is moving from the very left of the array to the very right. You can only see the k numbers
 in the window. Each time the sliding window moves right by one position.

Return the median array for each window in the original array. Answers within 10-5 of the actual
value will be accepted.
"""


class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        result = []
        for i in range(0, len(nums) - k+1):

            arr = sorted(nums[i:k+i])


            arr_len = len(arr)
            if arr_len % 2 == 0:
                median = round((arr[arr_len // 2]+arr[arr_len // 2-1])/2,5)
            else:
                median = round(arr[arr_len //2],5)

            result.append(median)

        return result

if __name__ == '__main__':

    sol= Solution()

    nums = [1,4,2,3]
    k = 4

    print(sol.medianSlidingWindow(nums, k))