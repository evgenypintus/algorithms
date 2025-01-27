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

        i = 0
        j = 0
        nums_r = nums1[0:m]

        while i < m or j < n:

            while i < m and (j == n or nums_r[i] <= nums2[j] ):
                res.append(nums_r[i])
                i = i+1

            while j < n and (i == m or nums_r[i] > nums2[j] ):
                res.append(nums2[j])
                j = j+1



        nums1[:len(res)] = res



if __name__ == '__main__':

    s = Solution()

    nums1 = [0,0,0,0,0]
    m = 0
    nums2 = [1,2,3,4,5]
    n = 5

    s.merge(nums1, m, nums2, n)

    print(nums1)



