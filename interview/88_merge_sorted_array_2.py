class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        res = []
        if m == 0:
            nums1[:n] = nums2
            return
        if n == 0:
            nums1[:m] = nums1[:m]
            return

        i = m-1
        j = n-1
        end_index = len(nums1) -1

        while i >= 0 or j >= 0:

            while i >= 0 and (j < 0 or nums1[i] > nums2[j] ):
                nums1[end_index] = nums1[i]
                i = i-1
                end_index = end_index -1

            while j >= 0 and (i < 0 or nums1[i] <= nums2[j] ):
                nums1[end_index] = nums2[j]
                j = j-1
                end_index = end_index -1


if __name__ == '__main__':

    s = Solution()

    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [3,4,5]
    n = 3

    s.merge(nums1, m, nums2, n)

    print(nums1)



