"""
347. Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.
"""
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return None
        if k ==0:
            return None

        nums_dict = {}
        nums_ext = {}
        for n in nums:
            if n in nums_dict:
                nums_dict[n] += 1
            else:
                nums_dict[n] = 1
        result = []
        for n, freq in nums_dict.items():

            if freq in nums_ext:
                nums_ext[freq].append(n)
            else:
                nums_ext[freq] = [n]

        print(nums_dict)
        print(nums_ext)
        count = 0
        for i in sorted(nums_ext, reverse=True):
            print(i)
            for w in nums_ext[i]:
                print(w)
                result.append(w)
                count +=1
                if count >= k:
                    break

            if count >= k:
                break
        return result


if __name__ == '__main__':

    s = Solution()

    nums = [1,2]
    k = 2

    print(s.topKFrequent(nums, k))